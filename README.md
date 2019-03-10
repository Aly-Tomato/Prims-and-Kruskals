# Prims-and-Kruskals
Algorithms project exploring MST algorithms.

## Usage  
Download with the links above or,  
```
Main Program
$ git clone https://github.com/Aly-Tomato/Prims-and-Kruskals.git  
$ cd Prims-and-Kruskals
$ python3 main.py "{file_name.txt}" {algo} where p = Prims and k = Kruskals

examples:
$ python3 main.py "city_pairs.txt" p  #executes prims algorithm
$ python3 main.py "city_pairs.txt" k  #executes kruskals algorithm
$ python3 test.py p "executes test suite on prims"
$ python3 test.py k "executes test suite on kruskals"
```

## Project Write Up  

### Briefly describe your development process.  
The first step to development this process was to understand the algorithms I were to implement
and make decisions on language and whether or not I would attempt the extra credit.
Ultimately I decided to go with Python in which I go more into my reasoning below.
Once I understood the algorithm I studied the psuedo code example given in class
and created my own pseudo code that represented my chosen language a bit more. I
feel like I did a decent amount of prep work before implementing Prims that I found that 
when it came to implementing Prims, it was simple and took a lot less time than I had
allocated to the homework. Because of this I decided to give Kruskals a try and
in the later paragraphs I'll go into detail about how implementing Kruskals was
a more difficult task for me compared to Prims.


### What sources did you use to help you implement the algorithm?
For Prims, I relied heavily on sources from the text book and in class examples. 
For Python module references I utilized docs.python.org. When I decided to 
give Kruskal's a try I went back to the book but found myself lost. I went online to 
see how others implemented Kruskal's with Python but I did not base my implementation
on examples seen. In fact, some of the examples I saw online didn't utilize the Python set() library
which I planned on doing. So, the work you see done in kruskals.py used docs.python.org
as it's main resource as well as in class notes.

### What programming language did you choose and why?
I chose to work with Python because I felt like using a dictionary and tuples were going to simplify the data structures needed
to implement these algorithms. The ease of packing and unpacking tuples were
important in order to maintain organized when dealing with a large data set. I'm happy
that I decided to use tuples because the two algorithms pack the values in different
orders. This is simply done by just ordering them to satisfy the different algorithms.
Had it have been linked nodes or a list perhaps, re-ording the data
would have been a much more serious ordeal.   
For example, Prims key/value pair looked like this:  
```(vertex 1, vertex 2, weight, cumulative weight)```  
In contrast to Kruskals which looked like this:  
```(weight, vertex 1, vertex 2, cumulative weight)```  
More about data structures below. Ultimately my main motivation in chosing
Python is simple - Python is just so much fun!


### What data structures did you use and why? How are you representing your graph?
The overall data structure I am using to represent the weighted graph is a nested dictionary. 
To represent the minimum spanning tree I used a nested dictionary of tuples. In Prims
I represented the visited vertices in a list and in Kruskals I represented parent nodes
and ranks in a dictionary. I explain these choices in later paragraphs. 
See below:

```
Weighted Graph (input) = {vertex 1: {vertex 2: weight}}
Min Span Tree (output) = {vertex 1: { vertex 2: (weight, cumulative weight)}}

# Prims
Visited Vertices = []

# Kruskals
Parent = {vertex 1: vertex 2, vertex 3: vertex 4}
Vertices = set(vertex 1, vertex 2, ... , vertex n)
Edges = set(weight, vertex 1, vertex 2)
```

### Did you run into any difficulties with the implementation?
I ran into difficulties implementing Kruskals mostly due to poor design 
choices from the beginning. Originally I was intending on only implementing 
Prims algorithm so I decided to have a global module that would hold the different 
data structures instead of thinking of the graph as an object itself. 
This proved difficult as many of the algorithms I studied on Kruskal's 
required an Object Oriented approach which is not what I started with Prims. 
To be honest, I'm rather embarassed that I didn't take an object oriented approach
with Prims and if given the opportunity to do it again I would. Because of my last
minute decision to attempt a Kruskal implementation I missed out on utilizing
polymorphism in designing the test suite and related methods such as reading in the graph
printing the graph and etc. 
So how did I work around this in Kruskals? I relied on my global module to help 
organize the two separate algorithms. Instead of each vertice having parent nodes and a rank
I created PARENT and RANK dictionaries in my glb "global" module where each vertice
mapped to a specific point in the aforementioned dictionaries.

### Example outputs from your testing as well as the results from the graph in city-pairs.txt file.
To run the test suite execute the following commands seen in section **_Usage_**
This test program will execute unit tests on the following methods in prims.py ```read_graph(), get_min(), prims()```.
Once executed the test will output if these test PASSED or FAILED including an expected/responded message for errors.
The test suite uses a smaller sample of data in it's weight graph found in _sample_data.txt_.
Below are screenshots of the outputs of the prims algorithm and the test suite on 
the Prims implementation.

