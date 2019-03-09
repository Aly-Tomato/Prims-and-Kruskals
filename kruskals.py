import sys
import heapq

def read_graph(file, d):
    file_path = open(file)
    for lines in file_path:
        line = [x.strip() for x in lines.split(f'{d}')]
        e1 = line[0]
        e2 = line[1]
        weight = line[2]
        if weight in wgraph.keys():
            wgraph[weight][e1] = e2
        else:
            wgraph[weight] = {}
            wgraph[weight][e1] = e2
    return wgraph

def kruskals(wgraph):
    edges = []
    for e in wgraph:
        heapq.heappush(edges, e)
    print(edges)



def main():
    if len(sys.argv) < 2:
        sys.exit()
    file = sys.argv[1]
    delimiter = ' '
    read_graph(file, delimiter)
    kruskals()
    #print_pretty()