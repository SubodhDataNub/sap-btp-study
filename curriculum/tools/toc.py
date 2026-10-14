import re, sys, json, os
docs = sys.argv[1]; maxdepth = int(sys.argv[2])
lines = open(os.path.join(docs,'index.md'),encoding='utf-8').read().splitlines()
pat = re.compile(r'^( *)-\s+\[(.*?)\]\((.*?)\)')
nodes=[]
for l in lines:
    m=pat.match(l)
    if not m: continue
    d=len(m.group(1))//4; f=m.group(3).split('#')[0]
    nodes.append((d,m.group(2),f))
# subtree distinct files
out=[]
for i,(d,t,f) in enumerate(nodes):
    files={f}
    j=i+1
    while j<len(nodes) and nodes[j][0]>d:
        files.add(nodes[j][2]); j+=1
    if d<=maxdepth:
        out.append(f"{'  '*d}{t} [{len(files)}] ({f})")
print("\n".join(out))
allf={n[2] for n in nodes}
ondisk=set()
for r,_,fs in os.walk(docs):
    for x in fs:
        if x.endswith('.md'): ondisk.add(os.path.relpath(os.path.join(r,x),docs).replace(os.sep,'/'))
print("\nTOC distinct files:",len(allf)," on disk:",len(ondisk)," not in TOC:",len(ondisk-allf)," TOC missing on disk:",len(allf-ondisk))
json.dump(nodes,open(os.path.join(sys.argv[3],'toc_nodes.json'),'w'))
print(sorted(ondisk-allf)[:40])
