import sys
import kruskals
import prims

def usage():
    print("USAGE: main.py [\"file.txt\"] [\'algo\'] where p = prims , k = kruskals")
    sys.exit()

def main():
    file = sys.argv[1]
    delimiter = ' '

    if len(sys.argv) < 2:
        usage()
    if(sys.argv[2] == "p"):
        #prims
        prims.read_graph(file, delimiter)
        prims.prims()
        prims.print_pretty()
    elif(sys.argv[2] == "k"):
        #kruskals
        kruskals.read_graph(file, delimiter)
        kruskals.kruskals()
    else:
        usage()

if __name__ == "__main__":
    main()



