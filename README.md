# SAP BTP Study

A structured self-study course on **SAP Business Technology Platform**, built from SAP's official BTP documentation, with a small local website to study it in.

- **28 modules** across 5 levels: Foundation → Core: Cloud Foundry → Developer (CAP / Fiori) → Advanced / Admin → Optional / Reference
- Each lesson has: plain-language summary, core concepts with analogies, Mermaid diagrams, Windows hands-on, gotchas, interview Q&A, **customer questions** (delivery and presentation style), a quiz, and links to the exact SAP source pages
- A **local study site** with a progress tracker, which also renders the original SAP docs

> Status: lessons are being written one at a time. See `curriculum/progress.md` or the site's sidebar for what's available.

---

## Set up on a new laptop

**You need:** Git, Python 3.8 or newer, and a modern browser. Nothing else: no `pip install`, no Node.js.

**1. Clone, including the SAP docs (submodule):**

```bash
git clone --recurse-submodules https://github.com/SubodhDataNub/sap-btp-study.git
```

> **Windows tip:** clone into a short folder such as `C:\study\` (anything up to about 100 characters). Some SAP doc paths are long, and Windows' 260-character path limit can otherwise hide a few images.

If you already cloned without `--recurse-submodules`, fetch the docs with:

```bash
git submodule update --init
```

**2. Start the study site:**

- **Windows:** double-click `curriculum\Start BTP Study Site.cmd`, or run:
  ```powershell
  python curriculum\site\serve.py
  ```
- **macOS / Linux:**
  ```bash
  sh curriculum/start-site.sh
  ```

Your browser opens at **http://127.0.0.1:8765** (or **http://localhost:8765**). Keep the terminal window open while you study, and press `Ctrl+C` to stop. If the port is busy, add `--port 8800`.

> "This site can't be reached" means the server isn't running. Start it again.

---

## Keeping two laptops in sync

Your progress (`curriculum/progress.md`) and new lessons travel through GitHub:

**Before you study:**

```bash
git pull
```

**After you study** (saves your module statuses and notes):

```bash
git add curriculum/progress.md
```
```bash
git commit -m "Update study progress"
```
```bash
git push
```

⚠️ **This repository is public.** Anything you write in `progress.md` notes becomes public when you push. Keep notes about your employer, customers or projects out of it.

---

## What's in here

| Path | What it is |
|---|---|
| `curriculum/01-syllabus.md` | The full syllabus: levels, modules, objectives, study times, exact source files |
| `curriculum/00-doc-map.md` | Map of all 2,065 SAP doc pages grouped into topic clusters, plus flagged gaps and outdated pages |
| `curriculum/modules/` | The lessons (`NN-module-name.md`) |
| `curriculum/progress.md` | Your checklist and notes |
| `curriculum/site/` | The local study site (`serve.py` + static files, Python standard library only) |
| `curriculum/tools/` | Scripts that generate the syllabus. Only needed if the syllabus changes |
| `btp-cloud-platform/` | **Git submodule:** SAP's official BTP documentation ([SAP-docs/btp-cloud-platform](https://github.com/SAP-docs/btp-cloud-platform)), pinned to the version the curriculum was built from |

The site serves files only on your own machine (`127.0.0.1` / `::1`). It is read-only except for updating module statuses in `progress.md`.

---

## Sources, licences and disclaimer

- **SAP BTP documentation:** © SAP SE, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Included as a git submodule, not copied or modified.
- **Lessons and curriculum:** personal study notes written from those docs. They are **not** official SAP documentation. Claims marked 📄 come from the SAP docs; claims marked 🌐 are general knowledge to verify.
- **Bundled libraries** (in `curriculum/site/vendor/`): [marked](https://github.com/markedjs/marked) 12.0.2 and [mermaid](https://github.com/mermaid-js/mermaid) 10.9.1, both MIT-licensed. Their licence files are included.
