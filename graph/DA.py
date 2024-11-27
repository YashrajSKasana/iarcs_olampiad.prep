import heapq

def dijkstra(graph, N, start, end):
    pq = []
    distances = ["@"] * N
    distances[start] = 0  
    heapq.heappush(pq, (0, start))  

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if distances[current_node] != "@" and current_distance > distances[current_node]:
            continue

        for neighbor in range(N):
            if neighbor == current_node:
                continue
            
            weight = abs(current_node - neighbor) * max(graph[current_node], graph[neighbor])
            new_distance = current_distance + weight

            if distances[neighbor] == "@" or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances[end] if distances[end] != "@" else None

num_tasks = int(input())
def run_prob():
    for _ in range(num_tasks):
        N, A, B = map(int, input().split())
        A -= 1  
        B -= 1  
        graph = list(map(int, input().split()))
        result = dijkstra(graph, N, A, B)
        print(result)

