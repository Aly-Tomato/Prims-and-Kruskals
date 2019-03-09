import sys
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

def make_set(x):
    if x not in glb.DSET:
        glb.DSET.union(x)

def find(i):
    if(glb.PARENT[i] == i):
        return i
    return find(glb.PARENT[i])

def kruskals():
    edges = []
    for e in glb.WGRAPH:
        v1,v2 = glb.WGRAPH[e]
        heapq.heappush(edges, (int(e),v1,v2))
    while(edges):
        e,v1,v2 = heapq.heappop(edges)
        glb.PARENT.append(int(e))

def main():
    if len(sys.argv) < 2:
        sys.exit()
    file = sys.argv[1]
    delimiter = ' '
    read_graph(file, delimiter)
    kruskals()
    #print_pretty()