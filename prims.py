import glb

def read_graph(file, d):
    file_path = open(file)
    for lines in file_path:
        line = [x.strip() for x in lines.split(f'{d}')]
        e1 = line[0]
        e2 = line[1]
        weight = line[2]
        if e1 in glb.WGRAPH.keys():
            glb.WGRAPH[e1][e2] = weight
        else:
            glb.WGRAPH[e1] = {}
            glb.WGRAPH[e1][e2] = weight
    return glb.WGRAPH

#return true if successfully added vertex to visited
#return false if vertex was already visited
def add_visited(Vertex):
    if(Vertex in glb.Vr):
        return False
    else:
        glb.Vr.append(Vertex)
        return True

def get_min():
    minv1 = None
    minv2 = None
    mindist = 0
    for v1 in glb.Vr:
        neighbors = list(glb.WGRAPH.get(v1))
        for v2 in neighbors:
            if v2 in glb.Vr or v1 == v2:
                continue
            if minv1 == None or minv2 == None:
                minv1 = v1
                minv2 = v2
                mindist = glb.WGRAPH[v1][v2]
                continue
            a = int(glb.WGRAPH[v1][v2])
            b = int(glb.WGRAPH[minv1][minv2])
            if a < b:
                minv1 = v1
                minv2 = v2
                mindist = a
    return (minv1,minv2,mindist)

def prims():
    cdist = 0 #cumulative dist
    length = len(list(glb.WGRAPH.keys()))
    v = list(glb.WGRAPH.keys())[0]
    add_visited(v)
    for i in range(0,length-1):
        v, v2, edist = get_min() #v2 min weight
        cdist += int(edist)
        #add v to MST
        glb.MST.append((v,v2,str(edist),str(cdist)))
        add_visited(v2)
    return glb.MST

def print_pretty():
    t1 = "Vertex 1"
    t2 = "Vertex 2"
    tw = "Distance"
    cd = "Cumulative Distance"
    print("******************************************************************************")
    print(t1.ljust(15, ' '), "\t", t2.ljust(15, ' '), "\t", tw.ljust(10, ' '), "\t", cd.ljust(10, ' '))
    print("******************************************************************************")
    for m in glb.MST:
        v1,v2,w, c = m
        print(v1.ljust(15, ' '), "\t", v2.ljust(15, ' '), "\t", w.ljust(10, ' '), "\t", c.ljust(15, ' '))
