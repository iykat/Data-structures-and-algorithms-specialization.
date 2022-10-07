WHITE, GREEN, RED = 0, 1, 2

def acyclic(adj):
    number_of_nodes = len(adj)
    colors = [WHITE for _ in range(number_of_nodes)]
    
    def dfs(node):
        colors[node] = GREEN
        neighbours = adj[node]
        
        for neighbour in neighbours:
            neighbours_color = colors[neighbour]
            if neighbours_color == GREEN:
                return 1
            if neighbours_color == RED:
                continue 
            contains_cycle = dfs(node)
            if contains_cycle:
                return 1
        colors[node] = RED 
        return 0 
    
    for node in range(number_of_nodes):
        if colors[node] != WHITE:
            continue 
        
        contains_cycle = dfs(node)
        if contains_cycle:
            return 1
    return 0 
        