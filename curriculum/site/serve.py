"""Local study site for the SAP BTP curriculum.

Serves the whole "BTP content" folder (curriculum + SAP docs) on http://127.0.0.1:8765
and exposes a tiny API so the site can read and update curriculum/progress.md.

Usage (PowerShell):
    python "curriculum\\site\\serve.py"              # opens your browser
    python "curriculum\\site\\serve.py" --no-browser
    python "curriculum\\site\\serve.py" --port 8800

Standard library only. Listens on localhost only, never on the network.
"""
import argparse
import json
import os
import re
import socket
import sys
import threading
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
CURRICULUM_DIR = os.path.dirname(SITE_DIR)
ROOT_DIR = os.path.dirname(CURRICULUM_DIR)          # the "BTP content" folder
PROGRESS_MD = os.path.join(CURRICULUM_DIR, "progress.md")

ROW_RE = re.compile(
    r"^\| \[(?P<chk>[ xX])\] \| (?P<id>M\d\d) \| (?P<level>[^|]+?) \| (?P<title>[^|]+?) \| "
    r"(?P<status>[^|]+?) \| \[[^\]]*\]\((?P<lesson>[^)]+)\) \|\s*$"
)
DONE_RE = re.compile(r"\*\*Done:\*\* \d+ / \d+")
STATUSES = ("not started", "in progress", "done")
LOCK = threading.Lock()


def read_progress():
    # newline="" keeps the file's own line endings (CRLF on Windows) so writes don't rewrite every line.
    with open(PROGRESS_MD, encoding="utf-8", newline="") as f:
        return f.read()


def parse_modules(text):
    modules = []
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        title = m.group("title").strip()
        tag = ""
        t = re.search(r"\s*\*\((.+?)\)\*\s*$", title)
        if t:
            tag, title = t.group(1), title[: t.start()].strip()
        lesson = "curriculum/" + m.group("lesson").strip()
        modules.append({
            "id": m.group("id"),
            "level": m.group("level").strip(),
            "title": title,
            "tag": tag,
            "status": m.group("status").strip(),
            "lesson": lesson,
            "exists": os.path.isfile(os.path.join(ROOT_DIR, *lesson.split("/"))),
        })
    return modules


def update_status(module_id, status):
    with LOCK:
        text = read_progress()
        lines = text.splitlines(keepends=True)
        found = False
        for i, line in enumerate(lines):
            m = ROW_RE.match(line.rstrip("\r\n"))
            if m and m.group("id") == module_id:
                ending = line[len(line.rstrip("\r\n")):]
                chk = "x" if status == "done" else " "
                body = line.rstrip("\r\n")
                body = "| [" + chk + "]" + body[len("| [ ]"):]
                s, e = m.span("status")
                body = body[:s] + status + body[e:]
                lines[i] = body + ending
                found = True
                break
        if not found:
            return False
        text = "".join(lines)
        mods = parse_modules(text)
        done = sum(1 for x in mods if x["status"] == "done")
        text = DONE_RE.sub(f"**Done:** {done} / {len(mods)}", text, count=1)
        tmp = PROGRESS_MD + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.replace(tmp, PROGRESS_MD)
        return True


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".md": "text/markdown; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
    }

    def end_headers(self):
        # Always serve fresh content so edits to lessons/progress show up on reload.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if args and str(args[1]).startswith(("4", "5")) and "favicon" not in str(args[0]):
            sys.stderr.write("  [%s] %s\n" % (args[1], args[0]))

    def _host_ok(self):
        raw = self.headers.get("Host") or ""
        host = raw[1:raw.find("]")] if raw.startswith("[") else raw.split(":")[0]
        return host in ("127.0.0.1", "localhost", "::1")

    def _json(self, code, payload):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if not self._host_ok():
            return self._json(403, {"error": "forbidden host"})
        path = self.path.split("?", 1)[0]
        if path in ("/", "/index.html"):
            self.send_response(302)
            self.send_header("Location", "/curriculum/site/")
            self.end_headers()
            return
        if path == "/api/status":
            try:
                mods = parse_modules(read_progress())
            except OSError as e:
                return self._json(500, {"error": str(e)})
            done = sum(1 for m in mods if m["status"] == "done")
            return self._json(200, {"modules": mods, "done": done, "total": len(mods)})
        return super().do_GET()

    def do_POST(self):
        if not self._host_ok():
            return self._json(403, {"error": "forbidden host"})
        if self.path != "/api/progress":
            return self._json(404, {"error": "not found"})
        # A custom header forces a CORS preflight, so other websites can't post here.
        if self.headers.get("X-Requested-With") != "btp-study":
            return self._json(403, {"error": "missing header"})
        try:
            length = min(int(self.headers.get("Content-Length", "0")), 1024)
            body = json.loads(self.rfile.read(length) or b"{}")
            module_id, status = body.get("id", ""), body.get("status", "")
        except (ValueError, AttributeError):
            return self._json(400, {"error": "bad json"})
        if not re.fullmatch(r"M\d\d", str(module_id)) or status not in STATUSES:
            return self._json(400, {"error": "invalid id or status"})
        if not update_status(module_id, status):
            return self._json(404, {"error": "module not found"})
        return self._json(200, {"ok": True})


def main():
    ap = argparse.ArgumentParser(description="SAP BTP curriculum study site")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args()

    handler = partial(Handler, directory=ROOT_DIR)
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except OSError as e:
        print(f"Could not start on port {args.port}: {e}")
        print(f"Try another port, e.g.:  python serve.py --port {args.port + 1}")
        sys.exit(1)

    # Also listen on IPv6 localhost, because some browsers try "localhost" as ::1 first.
    server6 = None
    try:
        class V6Server(ThreadingHTTPServer):
            address_family = socket.AF_INET6
        server6 = V6Server(("::1", args.port), handler)
        threading.Thread(target=server6.serve_forever, daemon=True).start()
    except OSError:
        server6 = None

    url = f"http://127.0.0.1:{args.port}/curriculum/site/"
    print("SAP BTP study site is running.")
    print(f"  Open:  {url}")
    print(f"   (or:  http://localhost:{args.port}/ )")
    print("  Stop:  press Ctrl+C in this window")
    if not args.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()
        if server6:
            server6.shutdown()
            server6.server_close()


if __name__ == "__main__":
    main()
