#Uses python3

import sys

def number_of_components(adj):
    result = 0
    number_of_nodes = len(adj)
    visited = [False] * number_of_nodes
    for node in range(len(adj)):
        if not visited[node]:
            explore(adj, node, visited)
            result += 1
    return result

def explore(adj, node, visited):
    visited[node] = True 
    for neighbour in adj[node]:
        if not visited[neighbour]:
            explore(adj, neighbour, visited)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
