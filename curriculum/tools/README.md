# Curriculum tools

Scripts used to build the doc map statistics and to generate `01-syllabus.md`. You only need these if the syllabus changes (new or re-ordered modules). For studying, ignore this folder.

| File | What it does |
|---|---|
| `modules.py` | **The source of truth for the syllabus**: every module's level, title, objectives, prerequisites, core files, deep-reference branches and flags |
| `resolve.py` | Shared helpers: resolves file IDs to doc paths, walks the TOC, counts words |
| `toc.py` | Rebuilds `toc_nodes.json` from `btp-cloud-platform/docs/index.md` (run after updating the SAP docs) |
| `toc_nodes.json`, `assign.json` | Cached TOC tree and page-to-cluster assignment |
| `stats.py` | Sanity check: reading time per module, duplicate core files, coverage of all pages |
| `uncov.py` | Lists any doc pages not covered by a module |
| `gen_syllabus.py` | Writes `01-syllabus.md` from `modules.py` |
| `gen_progress.py` | Writes a **fresh** `progress.md`. It refuses to overwrite an existing one (your notes!) unless you pass `--force` |

Run them from the `curriculum` folder, for example:

```bash
python tools/stats.py ../btp-cloud-platform/docs
```
```bash
python tools/gen_syllabus.py ../btp-cloud-platform/docs 01-syllabus.md
```

After updating the SAP docs submodule, rebuild the TOC cache first:

```bash
python tools/toc.py ../btp-cloud-platform/docs 1 tools
```
