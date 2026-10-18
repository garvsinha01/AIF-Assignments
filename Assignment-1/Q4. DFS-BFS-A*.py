from collections import deque
import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

weighted_graph = {
    'A': [('B', 1), ('C', 3)],   
    'B': [('D', 3), ('E', 1)],   
    'C': [('F', 5)],             
    'D': [],                     
    'E': [('F', 1)],              
    'F': []                     
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}


def dfs(graph, start):
    visited = set()

    def visit(vertex):
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in graph[vertex]:
                visit(neighbor)

    visit(start)

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def a_star(graph, heuristic, start, goal):

    open_list = [(heuristic[start], start)]
    visited = set()

    while open_list:

        cost, current = heapq.heappop(open_list)

        if current == goal:
            print(current, end=" ")
            return

        if current not in visited:
            visited.add(current)
            print(current, end=" ")

            for neighbor, distance in graph[current]:

                if neighbor not in visited:
                    f_cost = cost + distance + heuristic[neighbor]
                    heapq.heappush(open_list, (f_cost, neighbor))


print("DFS Traversal:")
dfs(graph, 'A')

print("\n\nBFS Traversal:")
bfs(graph, 'A')

print("\n\nA* Search:")
a_star(weighted_graph, heuristic, 'A', 'F')

print()
