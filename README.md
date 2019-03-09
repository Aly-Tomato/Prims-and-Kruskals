# Prims-and-Kruskals
Algorithms project exploring MST algorithms

## Usage  
Download with the links above or,  
```
Main Program
$ git clone https://github.com/Aly-Tomato/Prims-and-Kruskals.git  
$ cd Prims-and-Kruskals
$ python3 main.py "{file_name.txt}" 'algo' where p = Prims and k = Kruskals

examples:
$ python3 main.py "city_pairs.txt" p  #executes prims algorithm
$ python3 test.py "executes test suite"
```

Note: Upon submission, Kruskal's algorithm has not yet been fully implemented. Therefore ```python3 main.py "city_pairs.txt" k``` 
will result in errors. Due to interest of time and satisfying responsibilities in other courses I do plan to finish implementing
Kruskal's after the term is over.


## Project Write Up  

### Briefly describe your development process.  
The first step to development this process was to understand the algorithms I were to implement
and make decisions on language and whether or not I would attempt the extra credit.
Ultimately I decided to go with Python in which I go more into my reasoning below.
Once I understood the algorithm I studied the psuedo code example given in class
and created my own pseudo code that represented my chosen language a bit more.


### What sources did you use to help you implement the algorithm?
For Prims, I relied heavily on sources from the text book and in class examples. 
For Python module references I utilized docs.python.org. When I decided to 
give Kruskal's a try I went back to the book but found myself lost. I went online to 
see how others implemented Kruskal's with Python but I did not base my implementation
on examples seen. In fact, some of the examples I didn't utilize the Python set() library
which I planned on doing. So, the work you see done in kruskals.py used docs.python.org
as it's main resource.

### What programming language did you choose and why?
I chose to work with Python because I felt like using a dictionary and tuples were going to simplify the data structures needed
to implement these algorithms. The ease of packing and unpacking tuples were
important in order to maintain organized when dealing with a large data set.
More about data structures below. Mainly, Python is just so much fun!


### What data structures did you use and why? How are you representing your graph?
The overall data structure I am using to represent the weighted graph is a nested dictionary. To represent the minimum spanning tree I used a nested dictionary of tuples. See below:

```
Weighted Graph (input) = {vertex 1: {vertex 2: weight}}

Min Span Tree (output) = {vertex 1: { vertex 2: (weight, cumulative weight)}}
```
Another data structure used in aid of implementation were a visited list ```Vr = []```

### Did you run into any difficulties with the implementation?
I ran into difficulties implementing Kruskals mostly due to poor design from the beginning. Originally I was just planning on implementing Prims so I decided to have a global module that will hold the different data structures instead of creating individual objects for the graphs. This proved difficult as many (if not all) of the algorithms I studied on Kruskal's requires an Object Oriented approach which is not what I've done with Prims. Because of these difficulties I've decided to shift my focus on implementing Kruskal's to developing a good test program. 

### Example outputs from your testing as well as the results from the graph in city-pairs.txt file.
To run the test program execute the following commands:
```
$ cd Prims-and-Kruskals
$ python3 test.py
```
This test program will execute unit tests on the following methods in prims.py ```read_graph(), get_min(), prims()```.
Once executed the test will output if these test PASSED or FAILED including an expected/responded message for errors.
The test suite uses a smaller sample of data in it's weight graph found in _sample_data.txt_.
Below are screenshots of the outputs of the prims algorithm and the test suite on 
the prims implementation.

