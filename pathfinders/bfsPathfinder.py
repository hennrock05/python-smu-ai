# Name: JChang
# Assignment 3
# bfsPathfinder.py
# Reference: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# Homework graph
graph = {'A': set(['B']),
         'B': set(['A', 'C', 'D']),
         'C': set(['B', 'D']),
         'D': set(['B', 'C', 'E', 'F']),
         'E': set(['F', 'D']),
         'F': set(['G']),
         'G': set(['F'])
         }

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


# Returns all possible paths between 2 nodes.
# Sorts the list from shortest to longest
# BFS is implemented using a queue
def bfs_pathfinder(graph, start, goal):
    # Add first node to the queue
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next in (graph[node] - set(path)):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Calculate the cost for each path
def get_cost(path):
    index = 0
    cost = 0
    total_cost = 0
    arclist = []
    
    # create list of arcs to map to costs
    # calculate total cost
    while index < (len(path) - 1):
        arc = str(path[index] + path[index + 1])
        total_cost += costs[arc]
        index += 1
    
    return total_cost


# Get all paths
path_list = list(bfs_pathfinder(graph, 'A', 'G'))
# Sort the paths from shortest to longest
path_list.sort(reverse=True)
# Prettify output
print("=== BFS Pathfinder ===")
print("The shortest path is: ")
short_path = ''.join(path_list[0])

print(short_path)

# Dictionary to map paths to costs
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
