graph = [
    {8,5,2},
    {5,2,0},
    {1,7,6,5},
    {0,1},
    {3},
    {0,4},
    {3,8,2},
    {2,5,4},
    {5,4}
]
graph2 = [
    {8, 5},     
    {2, 0},     
    {7, 6},     
    {1},        
    {3},        
    {4},        
    {2},        
    {4},        
    {5}         
]
graph3 = [
    {1, 2},    
    {0, 3, 2}, 
    {0, 1},    
    {1}        
]


def BFS(graph, root):
    visited = [-1] * len(graph) 
    visited[root] = "@"
    que = [root]
    while que:
        vertex = que.pop(0)
        for edg in graph[vertex]:
            if visited[edg] == -1:
                visited[edg] = vertex
                que.append(edg)
    return visited

def DFS(graph, root, __visited=[], __parent="@"):
    if not __visited:
        __visited = [-1] * len(graph)
    if __visited[root] != -1:
        return
    __visited[root] = __parent
    for vertex in graph[root]:
            DFS(graph, vertex, __visited, root)
    return __visited
dfs = lambda node: DFS(graph,node)
bfs = lambda node: BFS(graph,node)
# for i in range(len(graph3)):
    # print(f"{i}: {dfs(i)}")

# for i in range(len(graph3)):
    # print(f"{i}: {bfs(i)}")
node = 3
x = bfs(2)
while node != "@":
    print(node)
    node = x[node]
    print(node)

