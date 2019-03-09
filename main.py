import sys
import kruskals
import prims

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
        prims.prims()
        prims.print_pretty()
    elif(algo == 'k'):
        #kruskals
        kruskals.read_graph(file, delimiter)
        kruskals.kruskals()
    else:
        usage()

if __name__ == "__main__":
    main()



