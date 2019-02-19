import collections
import heapq

class Node:
    def __init__(self, data=None):
        self.data = data
        self.h = heuristics[data]


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]
    
    def get_cost(self, current, next_node):
        try:
            cost = costs[current+next_node] + heuristics[next_node]
        except:
            cost = costs[next_node+current] + heuristics[next_node]
        
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

def astar_search(graph, start, goal):
    current = start
    adj_list = list()
    path_list = list()
    
    while current:
        if current == goal:
            print("Done: Reached the goal")
            return current
        
        print("--------------------Debug - while current------------------")
        print("Current: ", current)

        for next_node in graph.neighbors(current):
            new_cost = graph.get_cost(current, next_node)
            print("Next: ", next_node)
            
            adj_list.append((next_node,new_cost))
            print("adj_list: ", adj_list)
            
            adj_list.sort(key = lambda x:x[1])
            print("Sorted adj_list: ", adj_list)
        

        path_list.append(adj_list[0][0])
        print("Path list: ", path_list)
        
        current = next_node
    

print(astar_search(graph, 'S', 'E'))