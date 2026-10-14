import sys, os, math, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolve import *

OUT = sys.argv[2]
L = "../btp-cloud-platform/docs/"
SKIM = {"f344a57", "08d1103"}   # long lookup tables: skim, not counted as reading time
NOTES_H = 0.75                  # time for lesson notes, interview Q&A and quiz
NL = "\n"

def rid(t): return t.rstrip('!')
def link(f): return f"[{title[f]}]({L}{f})"
def ceil_half(x): return math.ceil(x * 2) / 2

lvlname = {k: v for k, v, _ in LEVELS}
rows, body, cov = [], [], set()
total_h, lvl_h = 0, {}

for m in M:
    core = [res(t) for t in m['core']]
    read_w = sum(words(f) for f, t in zip(core, m['core']) if t not in SKIM)
    read_h = read_w / 150 / 60
    tot = ceil_half(NOTES_H + read_h + m['hands'])
    total_h += tot
    lvl_h[m['lvl']] = lvl_h.get(m['lvl'], 0) + tot
    cov |= set(core)
    tag = (" · *" + m.get('tag', 'awareness only') + "*") if m.get('awareness') else ""
    rows.append(f"| M{m['n']:02} | {lvlname[m['lvl']]} | {m['title']}{tag} | {len(core)} | ~{tot:g} h |")

    b = [f"### M{m['n']:02} · {m['title']}", ""]
    b.append(f"**Level:** {lvlname[m['lvl']]}{tag}  ·  **Estimated study time:** ~{tot:g} h "
             f"(lesson notes & Q&A ~{NOTES_H:g} h · source reading ~{read_h:.1f} h · hands-on ~{m['hands']:g} h)  ·  "
             f"**Lesson file:** `modules/{m['n']:02}-{m['slug']}.md`")
    b += ["", f"**Why it matters:** {m['why']}", "", "**Learning objectives:** after this module you can…"]
    b += [f"- {o}" for o in m['obj']]
    b += ["", "**Prerequisites:** " + "; ".join(m['pre']), ""]
    b += [f"**Core source files** ({len(core)} files, ~{read_w:,} words):", ""]
    for f, t in zip(core, m['core']):
        b.append(f"- {link(f)}" + (" — *lookup table: skim*" if t in SKIM else ""))
    if m.get('revisit'):
        owner = {res(t): mm_['n'] for mm_ in M for t in mm_['core']}
        b += ["", "**Revisit with a comparison lens** (core reading in other modules):", ""]
        for t in m['revisit']:
            f = res(t)
            b.append(f"- {link(f)} *(core in M{owner[f]:02})*")
    if m.get('ref'):
        b += ["", "**Optional deep reference:**", ""]
        for r, lab in m['ref']:
            f = res(rid(r))
            s = {f} if r.endswith('!') else subtree(f)
            cov |= s
            cnt = f" ({len(s)} pages incl. sub-pages)" if len(s) > 1 else ""
            b.append(f"- {lab}: [{f.split('/')[-1]}]({L}{f}){cnt}")
    if m.get('flags'):
        b += ["", "**⚠️ Flags:**", ""] + [f"- {x}" for x in m['flags']]
    b += ["", "---", ""]
    body += b

# Mermaid overview: one column per level, modules stacked inside, levels flowing left to right.
# (A full per-module prerequisite graph is too wide to read; exact prerequisites are listed per module.)
mm = ["```mermaid", "flowchart LR"]
for k, name, _ in LEVELS:
    mm.append(f'  subgraph {k}["{k} · {name}"]')
    mm.append("    direction TB")
    ids = []
    for m in M:
        if m['lvl'] == k:
            short = m['title'].split(':')[0]
            for ch in '"()':
                short = short.replace(ch, '')
            short = short.replace('&', 'and')
            mm.append(f'    M{m["n"]:02}["M{m["n"]:02} {short}"]')
            ids.append(f"M{m['n']:02}")
    mm.append("    " + " ~~~ ".join(ids))   # invisible links keep modules stacked in order
    mm.append("  end")
mm.append("  " + " --> ".join(k for k, _, _ in LEVELS))
mm.append("  classDef aware stroke-dasharray: 4 3")
mm.append("  class " + ",".join(f"M{m['n']:02}" for m in M if m.get('awareness')) + " aware")
mm.append("```")

core_files = len({res(t) for m in M for t in m['core']})
l123 = lvl_h['L1'] + lvl_h['L2'] + lvl_h['L3']

hdr = f"""# 01 — SAP BTP Learning Syllabus

> **For:** a fresher full-stack developer at an SAP partner (CAP + Fiori on Cloud Foundry, plus Node.js) who has a Python/FastAPI/AWS background and works on Windows.
>
> **Built from:** the 2,065 pages in `btp-cloud-platform/docs/` (see [00-doc-map.md](00-doc-map.md)). Every page in the repo is assigned to a module, either as **core reading** ({core_files} pages) or as **optional deep reference**. Coverage: **{len(cov)} / {len(files)} pages**.
>
> **Next step:** Phase 3 writes one lesson per module in `curriculum/modules/`, only when you say **"next"**. Progress is tracked in [progress.md](progress.md).

## How to read this syllabus

- **Levels** go from Foundation → Core → Developer → Advanced/Admin → Optional/Reference. Study in module order. The diagram shows the levels left to right; each module lists its exact prerequisites. Dashed boxes are awareness/reference-only.
- **Core source files** are the pages each lesson is based on. Read the lesson first, then open the originals. **Optional deep reference** covers everything else in that branch of the docs; use it as a lookup, not as reading homework.
- **Study time** = lesson notes, Q&A and quiz (~{NOTES_H:g} h) + reading the core source pages (at ~150 words/min, measured from the actual files) + hands-on in a BTP trial. Rounded up to the nearest half hour.
- **Awareness only** modules (dashed in the diagram) are for interview-level understanding: what it is, when it's used, how it compares. **Reference only** modules are lookups for when a project needs them. Neither has required hands-on.
- **Two kinds of questions in every lesson.** *Interview Q&A* tests your understanding. *Customer questions* are what a customer asks during delivery workshops or presentations ("why", "which", "what if", "who is responsible", "what does it cost"). Their answers are framed for business value: recommendation, then reason, then trade-off, then evidence. Anything that goes beyond this repo (pricing, competitive positioning, roadmap) is labelled as general knowledge to verify.
- **⚠️ Flags** mark gaps (topic mostly documented outside this repo) and pages that look outdated or conflicting. Each lesson says clearly where the repo stops.

## Your priority topics: where they are

| You asked for | Module(s) |
|---|---|
| Account model | M02 (concepts), M05 (cockpit hands-on) |
| Cloud Foundry | M06 (concepts), M07 (cf CLI, orgs, spaces), M09 (services), M10 (deploy & run) |
| Entitlements | M03 |
| XSUAA / role collections | M04 (basics), M14 (admin side), M15 (developer side: xs-security.json), M19 (IdP trust) |
| Destinations | M17 (⚠️ repo-limited), with App Router routes in M16 |
| MTA deployment | M12 (fundamentals), M13 (blue-green, CI/CD) |
| Business Application Studio | M11 (⚠️ repo-limited) |
| btp / cf CLIs | M08 (btp CLI), M07 (cf CLI) |
| Customer and interview "why / which" questions: BTP vs Azure/GCP, HANA Cloud vs PostgreSQL, CF vs Kyma vs ABAP, data residency, availability, cost, lock-in | A **Customer questions** section in every lesson · first look in M01, M06, M11 · capstone **M18** |

## Learning path

{NL.join(mm)}

## All modules at a glance

| # | Level | Module | Core files | Study time |
|---|---|---|---:|---:|
{NL.join(rows)}
| | | **Total** | **{core_files}** | **~{total_h:g} h** |

**Time per level:** {" · ".join(f"{lvlname[k]} ~{lvl_h[k]:g} h" for k, _, _ in LEVELS)}

**Suggested pace:** at about 1.5 h a day alongside work, Levels 1–3 (the part that matters most for your job, ~{l123:g} h) take about {math.ceil(l123 / 1.5 / 5)} working weeks. The whole syllabus takes about {math.ceil(total_h / 1.5 / 5)} working weeks.

## Levels

{NL.join(f"- **{k} · {n}:** {d}" for k, n, d in LEVELS)}

---

## Module details

"""

gaps = """
## Repo-wide gaps (topics that live in other SAP documentation sets)

These are relevant to your job but are **not substantively covered** in this repo. Lessons will cover only the BTP-side concepts that the repo supports, and will name these as the place to go next. Nothing will be presented as if it came from this repo when it doesn't.

| Topic | Touched in | Lives in (outside this repo) |
|---|---|---|
| CAP (CDS, services, Node.js runtime) | M11 | capire (SAP's CAP documentation) |
| SAP Business Application Studio | M11 | SAP Business Application Studio docs |
| Fiori elements / SAPUI5 / SAP Fiori tools | M11, M16 | SAPUI5 SDK, SAP Fiori tools docs |
| Destination service, Cloud Connector | M17 | SAP BTP Connectivity docs |
| SAP HANA Cloud, PostgreSQL on BTP | M11, M18, M27 | SAP HANA Cloud docs; PostgreSQL, hyperscaler option docs |
| SAP Cloud Identity Services (IAS) | M20 | SAP Cloud Identity Services docs |
| CI/CD service, SAP Cloud Transport Management | M13 | Their own service docs |
| SAP Build Work Zone (launchpad) | M16 | SAP Build Work Zone docs |
| Cloud Logging / application logs | M10, M21 | SAP Cloud Logging docs |
| Competitive positioning (BTP vs AWS/Azure/GCP), HANA Cloud vs PostgreSQL in depth | M18 | SAP Discovery Center, SAP HANA Cloud and PostgreSQL, hyperscaler option docs; general industry knowledge |
"""

open(OUT, 'w', encoding='utf-8').write(hdr + NL.join(body) + gaps)
print("written", OUT, "total_h", total_h, lvl_h, "cov", len(cov), "core", core_files)
