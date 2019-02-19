# Author: HennRock05
# Assignment 4
# References: https://www.redblobgames.com/pathfinding/a-star/implementation.html#cpp-astar
#             https://forum.unity.com/threads/astar-path-finding-sample-150-lines-of-code.106892/


import collections
import heapq

# Container for the nodes
# Holds the current node, heuristics value, and list of adjacent nodes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.h = heuristics[data]
        self.child_nodes = graph.edges[data]

# Heap queue to store the adjacent nodes and sort them from least to greatest
# Returns the cheapest node
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# Container for graph edges
# Includes method to calculate the cost
class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    # Return the edge
    def neighbors(self, id):
        return self.edges[id]
    
    # Calculate the cost
    def get_cost(self, current, next_node):
        try:
            cost = costs[current + next_node] + heuristics[next_node]
        except:
            cost = costs[next_node + current] + heuristics[next_node]
        
        return cost

# Setting values for directed graph
graph = SimpleGraph()
graph.edges = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': ['H'],
    'H': ['G'],
    'D': ['F'],
    'F': ['H'],
    'G': ['E'],
    'C': ['L'],
    'L': ['I', 'J'],
    'I': ['J', 'K'],
    'J': ['I', 'K'],
    'K': ['E']
}

# Hold heuristic data - distance between the node and the goal
heuristics = {
    'S': 10,
    'A': 9,
    'B': 7,
    'C': 8,
    'D': 8,
    'E': 0,
    'F': 6,
    'G': 3,
    'H': 6,
    'I': 4,
    'J': 4,
    'K': 3,
    'L': 6
}

# Holds weights for each edge or arc
costs = {
    'AD': 4,
    'AS': 7,
    'AB': 3,
    'BH': 1,
    'CL': 2,
    'DF': 5,
    'FH': 3,
    'GE': 2,
    'HG': 2,
    'IK': 4,
    'JK': 4,
    'KE': 5,
    'IJ': 4,
    'LJ': 4,
    'LI': 4,
    'SB': 2,
    'SC': 3
}

# A* function that takes the graph, start node, and end node
# Searches for the cheapest path considering g and h
def astar_search(graph, start, goal):
    # List to append nodes for the cheapest path
    path_list = list()
    # Instantiate the priority queue
    queue = PriorityQueue()
    
    # As long as there is a start value - execute.
    # After ever move, the new node becomes the start value
    while start:
        
        # Append the start value (new node) to the list
        path_list.append(start)
        
        # If the start value (new node) is the goal, we're done
        if start == goal:
            return path_list
        
        # Create a current node object from the start value (new node)
        current_node = Node(start)
        
        # For every adjacent node listed in current node's child_node list
        for child in current_node.child_nodes:
            # Calculate the cost f() = g() + h()
            child_cost = graph.get_cost(current_node.data, child)
            # Put the node, cost in the priority queue
            # Priority queue places the cheapest one at the front of the queue
            queue.put(child, child_cost)
        
        # Cheapest node becomes the next start node
        start = queue.get()

def main():
    cheapest_path = astar_search(graph, 'S', 'E')
    print("AStar's results: ", cheapest_path)

if __name__ == "__main__":
    main()
