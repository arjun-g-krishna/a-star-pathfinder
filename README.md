# A-star path-finding algorithm

A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. A major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches. However, A* is still the best solution in many cases.

## The algorithm

- A* is a path-finding algorithm. It is an *informed search algorithm.*
- Uninformed search algorithms explore the entire search space without any indication of how far away the goal is.
- On the other hand, informed search algorithms use additional knowledge to increase the efficiency of the search.
- The goal of the algorithm is to find the shortest path between any two points in a graph
- We have an open set, which is represented by a priority queue. The open set keeps track of the nodes that we want to consider next.