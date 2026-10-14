import sys,os,json; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from resolve import *
a=json.load(open(os.path.join(SP,'assign.json')))
cov=set()
for m in M:
    cov|={res(t) for t in m['core']}
    for rid,_ in m.get('ref',[]): cov|=({res(rid.rstrip('!'))} if rid.endswith('!') else subtree(res(rid)))
un=sorted(set(files)-cov)
from collections import Counter
print(Counter(a[f] for f in un))
for f in un: print(a[f][:3], f.split('/')[-1][:75], '|', title[f][:60])
