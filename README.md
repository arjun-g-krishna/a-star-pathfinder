# A* path-finding algorithm

A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. A major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches. However, A* is still the best solution in many cases.

## The algorithm

A* is a path-finding algorithm. It is an *informed search algorithm*. Uninformed search algorithms explore the entire search space without any indication of how far away the goal is. On the other hand, informed search algorithms use additional knowledge to increase the efficiency of the search.The goal of the algorithm is to find the shortest path between any two points in a graph

We have an open set, which is represented by a priority queue. The open set keeps track of the nodes that we want to consider next. We assign F,G and H scores to the nodes. These are some functions.

- H(n) gives an estimate of the distance of node 'n' from the end-node. The distance measure used is Manhattan Distance.
- G(n) is the current shortest distance from the start node to the current node 'n'
- F(n) is the sum of H and G functions.
	
	F(n) = G(n) + H(n)

In the beginning, the start node has its F,G and H values as 0. The other nodes have their F,G and H values as ∞ (infinity). Then we look at any edge to get to the next node. We check the length of the current path and compare it to the next node's G score . The G score is updated if the distance is less. The F and H scores are updated accordingly. The last node that we came from is then recorded.

The nodes that are considered are then added to the open set. The open set has its values stored in the format (distance,node). For example (2,C).

We look in the open set and select the node which has the shortest F score. The node is selected and the above steps are repeated for the node.

<img src=demo.gif width=500 height=auto />
