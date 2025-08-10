from collections import defaultdict

def count_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)
            components += 1
    return components

def min_edges(n, edge_list):
    components = count_components(n, edge_list)
    return components-1

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_tree.txt"
    solution_path = "../solution-outputs/rosalind_tree.txt"
    file = open(file_path, "r").readlines()
    n = int(file[0])
    print(n)
    edges = []
    for line in file[1:]:
        line = line.strip()
        vals = line.split(' ')
        edges.append((int(vals[0]), int(vals[1])))
    print(edges)
    print(min_edges(n, edges))