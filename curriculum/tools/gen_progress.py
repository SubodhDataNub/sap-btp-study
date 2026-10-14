import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules import M, LEVELS

OUT = sys.argv[1]
# progress.md holds your statuses and notes: never overwrite it by accident.
if os.path.exists(OUT) and "--force" not in sys.argv:
    sys.exit(f"{OUT} already exists and may contain your notes. Re-run with --force to overwrite it.")
lvlname = {k: v for k, v, _ in LEVELS}
out = ["# Progress Tracker", "",
       "Status values: `not started` · `in progress` · `done`. Tick the box when a module is done.",
       "Lessons are written one at a time; a lesson link only works once that lesson exists.", "",
       "## Checklist", "",
       "| ✓ | # | Level | Module | Status | Lesson |",
       "|---|---|---|---|---|---|"]
for m in M:
    tag = f" *({m.get('tag', 'awareness only')})*" if m.get('awareness') else ""
    out.append(f"| [ ] | M{m['n']:02} | {lvlname[m['lvl']]} | {m['title']}{tag} | not started | "
               f"[{m['n']:02}-{m['slug']}.md](modules/{m['n']:02}-{m['slug']}.md) |")
out += ["", f"**Done:** 0 / {len(M)}", "", "---", "", "## My notes", ""]
for m in M:
    out += [f"### M{m['n']:02} · {m['title']}", "",
            "- **Key takeaways:** ",
            "- **Questions / confusions:** ",
            "- **Hands-on log (what I ran, what happened):** ",
            ""]
open(OUT, 'w', encoding='utf-8').write("\n".join(out))
print("written", OUT)
