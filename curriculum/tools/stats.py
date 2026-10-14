import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from resolve import *
seen={}; cov=set(); tot_w=0
for m in M:
    core=[res(t) for t in m['core']]
    w=sum(words(f) for f in core); tot_w+=w
    for f in core:
        if f in seen: print(f"  DUP core {f} in M{seen[f]:02} and M{m['n']:02}")
        seen[f]=m['n']
    cov|=set(core)
    for rid,_ in m.get('ref',[]): cov|=({res(rid.rstrip('!'))} if rid.endswith('!') else subtree(res(rid)))
    big=[(words(f),f.split('/')[-1][:50]) for f in core if words(f)>4000]
    print(f"M{m['n']:02} {m['lvl']} core={len(core):2} words={w:6} read~{w/150/60:4.1f}h hands={m['hands']} {big if big else ''}")
print("total core words",tot_w, "core files",len(seen), "coverage incl ref",len(cov),"/",len(files))
