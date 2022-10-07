#Uses python3
import sys


# solution 1

def acyclic(adj):
    number_of_nodes = len(adj)
    visited = [False for _ in range(number_of_nodes)]
    currently_in_stack = [False for _ in range(number_of_nodes)]
    
    for node in range(number_of_nodes):
        if visited[node]: 
            continue
        
        contains_cycle = is_node_in_cycle(adj, node, visited, currently_in_stack)
        if contains_cycle:
            return 1
    return 0

def is_node_in_cycle(adj, node, visited, currently_in_stack):
    visited[node] = True 
    currently_in_stack[node] = True 
    
    neighbours = adj[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            contains_cycle = is_node_in_cycle(adj, neighbour, visited, currently_in_stack)
            if contains_cycle:
                return 1
        elif currently_in_stack[neighbour]:
            return 1
    
    currently_in_stack[node] = False 
    return 0


# solution 2

WHITE, GREEN, RED = 0, 1, 2

def acyclic(adj):
    number_of_nodes = len(adj)
    colors = [WHITE for _ in range(number_of_nodes)]
    
    for node in range(number_of_nodes):
        if colors[node] != WHITE:
            continue
        
        contains_cycle = traverse_and_color_nodes(adj, node, colors)
        if contains_cycle:
            return 1 
    return 0

def traverse_and_color_nodes(adj, node, colors):
    colors[node] = GREEN 
    neighbours = adj[node]
    
    for neighbour in neighbours:
        neighbour_color = colors[neighbour]
        
        if neighbour_color == GREEN:
            return 1
        if neighbour_color == RED:
            continue 
        
        contains_cycle = traverse_and_color_nodes(adj, neighbour, colors)
        if contains_cycle:
            return 1
    colors[node] = RED 
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
