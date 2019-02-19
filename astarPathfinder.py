import collections
import heapq

class Node:
    def __init__(self, data = None):
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
    
    def cost(self,current, next):
        


# Setting values for directed graph
graph = SimpleGraph()
graph.edges = {
    'S':['A','B','C'],
    'A':['B','D'],
    'B':['H'],
    'H':['G'],
    'D':['F'],
    'F':['H'],
    'G':['E'],
    'C':['L'],
    'L':['I','J'],
    'I':['J','K'],
    'J':['I','K'],
    'K':['E']
}

heuristics = {
    'S':10,
    'A':9,
    'B':7,
    'C':8,
    'D':8,
    'E':0,
    'F':6,
    'G':3,
    'H':6,
    'I':4,
    'J':4,
    'K':3,
    'L':6
}

costs = {
    'AD':4,
    'AS':7,
    'AB':3,
    'BH':1,
    'CL':2,
    'DF':5,
    'FH':3,
    'GE':2,
    'HG':2,
    'IK':4,
    'JK':4,
    'KE':5,
    'IJ':4,
    'LJ':4,
    'LI':4,
    'SB':2,
    'SC':3
}

def astar_search(graph, start, goal):
    # Create the priority queue
    frontier = PriorityQueue()
    # Add start to the priority queue
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        # node holds the first item off the queue
        node = frontier.get()
        
        if node == goal:
            break
        
        current = Node(node)
        
        for item in graph.neighbors(current.data):
            next = Node(item)
            new_cost = cost_so_far[current.data] + graph.cost(current.data, next.data)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                #### stopped here
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                
    return came_from, cost_so_far

print(astar_search(graph, 'S', 'E'))