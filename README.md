# Prims-and-Kruskals
Algorithms project exploring MST algorithms

## Usage  
```
Main Program
$ git clone https://github.com/Aly-Tomato/Prims-and-Kruskals.git  
$ cd Prims-and-Kruskals
$ python3 main.py

To run test program
$python3 test.py
```
Or, download with the links above.  

## Project Write Up  

### Briefly describe your development process.  
The first step to development this process was to understand the algorithms I were to implement. 


### What sources did you use to help you implement the algorithm?
I relied heavily on sources from the book and in class examples.

### What programming language did you choose and why?
I chose to work with Python again because I felt like using a dictionary and tuples were going to simplify the data structures needed
to implement these algorithms.


### What data structures did you use and why? How are you representing your graph?
The overall data structure I am using to represent the weighted graph is a nested dictionary. To represent the minimum spanning tree I used a nested dictionary of tuples. See below:

```
Weighted Graph (input) = {vertex 1: {vertex 2: weight}}

Min Span Tree (output) = {vertex 1: { vertex 2: (weight, cumulative weight)}}
```
Another data structure used in aid of implementation were a visited list ```Vr = []```

### Did you run into any difficulties with the implementation?
I ran into difficulties implementing Kruskals mostly due to poor design from the beginning. Originally I was just planning on implementing Prims so I decided to have a global module that will hold the different data structures instead of creating individual objects for the graphs. This proved difficult as many (if not all) of the algorithms I studied on Kruskal's requires an Object Oriented approach which is not what I've done with Prims. 

### Example outputs from your testing as well as the results from the graph in city-pairs.txt file.
To run the test program execute the following commands:
```
$ cd Prims-and-Kruskals
$ python3 test.py
```
This test program will execute unit tests on the following methods in prims.py ```read_graph(), get_min(), prims()```.
Once executed the test will output if these test PASSED of FAILED including an expected/responded message for errors.
