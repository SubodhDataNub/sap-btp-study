import json, os, re, sys
SP=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,SP)
from modules import M, LEVELS
DOCS=sys.argv[1]
nodes=json.load(open(os.path.join(SP,'toc_nodes.json')))
files=sorted({n[2] for n in nodes})
title={}
for d,t,f in nodes: title.setdefault(f,t.replace(chr(92),''))
def res(tok):
    c=[f for f in files if f.split('/')[-1].endswith('-'+tok+'.md')] if re.fullmatch(r'[0-9a-f]{7}',tok) else [f for f in files if f.split('/')[-1].startswith(tok)]
    if len(c)!=1: raise SystemExit(f"bad id {tok}: {c}")
    return c[0]
def subtree(f):
    for i,(d,t,ff) in enumerate(nodes):
        if ff==f:
            s={ff}; j=i+1
            while j<len(nodes) and nodes[j][0]>d: s.add(nodes[j][2]); j+=1
            return s
_wc={}
def words(f):
    if f not in _wc:
        txt=open(os.path.join(DOCS,f),encoding='utf-8').read()
        txt=re.sub(r'<[^>]+>',' ',txt); txt=re.sub(r'\]\([^)]*\)',']',txt)
        _wc[f]=len(re.findall(r'[A-Za-z0-9_]+',txt))
    return _wc[f]
