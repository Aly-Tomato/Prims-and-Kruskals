import sys
import kruskals
import prims
import glb

def usage():
    print("USAGE: main.py [\"file.txt\"] [algo] where p = prims , k = kruskals")
    sys.exit()

def main():
    if len(sys.argv) < 3:
        usage()
    file = sys.argv[1]
    delimiter = ' '
    algo = sys.argv[2]
    if(algo == 'p'):
        #prims
        prims.read_graph(file, delimiter)
        graph,tdist = prims.prims()
        glb.print_pretty()
        print(f"Total Distance : {tdist}")
    elif(algo == 'k'):
        #kruskals
        kruskals.read_graph(file, delimiter)
        graph,tdist = kruskals.kruskals()
        glb.print_pretty()
        print(f"Total Distance : {tdist}")
    else:
        usage()

if __name__ == "__main__":
    main()



