# Name: JChang
# Assignment 3
# dfsPathfinder.py
# Reference: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/


# homework graph
graph = {'A': set(['B']),
         'B': set(['A', 'C', 'D']),
         'C': set(['B', 'D']),
         'D': set(['B', 'C', 'E', 'F']),
         'E': set(['F', 'D']),
         'F': set(['G']),
         'G': set(['F'])
         }

# No value for EF - so set EF to 0
costs = {
    'AB': 4,
    'BC': 2,
    'BD': 9,
    'CD': 3,
    'DE': 10,
    'EF': 3,
    'DF': 2,
    'FG': 2
}

# Get list of paths
# DFS is implemented using a stack
def dfs_pathfinder(graph, start, goal):
    # Initialize the stack with the start node
    stack = [(start, [start])]
    # As long as there are items in the stack, keeping checking
    while stack:
        (node, path) = stack.pop()
        for next in (graph[node] - set(path)):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                

# Get the cost of each path and return the total cost of the path.
def get_cost(path):
    index = 0
    cost = 0
    total_cost = 0
    arclist = []
    
    # create list of arcs to get cost
    while index < (len(path) - 1):
        arc = str(path[index] + path[index + 1])
        total_cost += costs[arc]
        index += 1
    
    return total_cost


# Get all paths
path_list = list(dfs_pathfinder(graph, 'A', 'G'))
# Sort the paths from shortest to longest
path_list.sort(reverse=True)
# Prettify output
print("=== DFS Pathfinder ===")
print("The shortest path is: ")
short_path = ''.join(path_list[0])

print(short_path)

# Dictionary to hold path:costs
dict = {}

# map the paths to the costs
for path in path_list:
    # Concatenate the path list into a string for the key
    key = key = ''.join(path)
    # Calculate the value
    value = get_cost(path)
    dict[key] = value

# Print the cheapest path according to cost
print("The cheapest path is: ")
print(min(dict, key=dict.get))
