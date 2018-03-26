# Connected-Component

Identifying the connected components in an unweighted network.

Input: from the command line the name of the edge list file of an undirected graph.

For example:

python Connected-Component.py MyGraph.txt

As usual, the vertices in the edge list file are labeled with values between 0 and|V|-1.

Output: to the standard output the list of all connected components, where each
list is a line consisting of all vertex indices of the component. In addition, all
vertices in each component are sorted by their indices; so are all components by
their first vertices. 

For example:

Component: 1 7 8 12 25

Component: 2 3 5 16 19 26

Component: 4 6 10 14 20

...
