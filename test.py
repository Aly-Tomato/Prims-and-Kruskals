import prims
import kruskals
import glb
import sys

def test_read (file, delimiter, algo):
    if(algo == 'k'):
        glb.WGRAPH = kruskals.read_graph(file, delimiter)
    if(algo == 'p'):
        glb.WGRAPH = prims.read_graph(file, delimiter)
    exKeys = 3
    keys = glb.WGRAPH.keys()
    respKeys = len(keys)
    #check total keys
    if(respKeys != exKeys):
        print("ERROR:\t read_graph() returned wrong amount of keys")
        print(f"Expected:  {exKeys}")
        print(f"Responded: {respKeys}")
        return False
    #check neighbors do not include key value
    for k in keys:
        if k in glb.WGRAPH[k]:
            print("ERROR:\t Key neighbors have same values as Key")
            print(f"Expected:  Key = {k}, graph[Key] != Key")
            print(f"Responded: {glb.WGRAPH[k]}")
            return False
    return True

def test_getmin():
    glb.Vr = ['a']
    expected = ('a','b','1')
    responded = prims.get_min()
    if expected == responded:
        return True
    else:
        print("ERROR:\t get_min returns wrong min edge")
        print(f"Expected:  {expected}")
        print(f"Responded: {responded}")
        return False

def test_prims():
    glb.Vr.clear()
    responded = prims.prims()
    expected = [('a', 'b', '1', '1'), ('a', 'c', '2', '3')]
    if(expected == responded):
        return True
    else:
        print("ERROR:\t prims.prims returned unexpected MST")
        print(f"Expected:  {expected}")
        print(f"Responded: {responded}")

def usage():
    print("USAGE: test.py [algo] where p = prims , k = kruskals")
    print("$ test.py k")
    sys.exit()

def main():
   file = "sample_data.txt"
   delimiter = ' '
   if(len(sys.argv) < 2):
       usage()
   algo = sys.argv[1]

   if(algo == 'p'):
       print("....TESTING PRIMS....")
       if test_read(file,delimiter,algo):
           print("prims.read_graph() : PASS")
       else:
           print("prims.read_graph() : FAIL")

       if test_getmin():
           print("prims.get_min() : PASS")
       else:
           print("prims.get_min() : FAIL")

       if test_prims():
           print("prims.prims() : PASS")
       else:
           print("prims.prims() : FAIL")
   if(algo == 'k'):
       print("....TESTING KRUSKALS....")
       if test_read(file,delimiter,algo):
           print("prims.read_graph() : PASS")
       else:
           print("prims.read_graph() : FAIL")
   else:
       usage()

if __name__ == "__main__":
    main()