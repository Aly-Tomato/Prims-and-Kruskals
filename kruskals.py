import heapq
import glb

#note: this algorithm assumes graph has unique weights. No two weights are the same

def read_graph(file, d):
    file_path = open(file)
    for lines in file_path:
        line = [x.strip() for x in lines.split(f'{d}')]
        e1 = line[0]
        e2 = line[1]
        weight = line[2]
        if weight not in glb.WGRAPH.keys():
            glb.WGRAPH[weight] = (e1, e2)
    return glb.WGRAPH

def make_set(v):
     glb.PARENT[v] = v
     glb.RANK[v] = 0

def find(v):
    if(glb.PARENT[v] != v):
        glb.PARENT[v] = find(glb.PARENT[v])
    return glb.PARENT[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if(root1 != root2):
        if(glb.RANK[root1] > glb.RANK[root2]):
            glb.PARENT[root2] = root1
        elif(glb.RANK[root1] < glb.RANK[root2]):
            glb.PARENT[root1] = root2
        else:
            glb.RANK[root2] += 1

def kruskals():
    edges = []
    vertices = set()
    cdist = 0
    for e in glb.WGRAPH:
        v1, v2 = glb.WGRAPH[e]
        heapq.heappush(edges, (int(e),v1,v2))
        vertices.add(v1)
        vertices.add(v2)
    for v in vertices:
        make_set(v)
    while(edges):
        e,v1,v2 = heapq.heappop(edges)
        if(find(v1) != find(v2)):
            union(v1, v2)
            cdist += e
            glb.MST.append((v1, v2, str(e), str(cdist)))
