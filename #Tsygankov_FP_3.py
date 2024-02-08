#Tsygankov_FP_3

import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Ініціалізуємо словник для зберігання найкоротших відстаней до кожної вершини
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0  # Відстань від початкової вершини до неї самої дорівнює 0
    # Ініціалізуємо бінарну купу для використання як пріоритетна черга
    pq = [(0, start)]  # (відстань, вершина)
    
    while pq:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_node = heapq.heappop(pq)
        
        # Якщо поточна відстань до цієї вершини більша, ніж відстань, яку ми вже обчислили, ігноруємо цю вершину
        if current_distance > distances[current_node]:
            continue
        
        # Оновлюємо відстані до всіх сусідніх вершин поточної вершини
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            # Якщо нова відстань коротша, ніж поточна, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Створення зваженого графа
G = nx.Graph()
G.add_weighted_edges_from([('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5), ('B', 'D', 10), ('C', 'D', 3)])

# Виклик алгоритму Дейкстри
start_node = 'A'
shortest_distances = dijkstra(G, start_node)

# Вивід результатів
print("Найкоротші відстані від вершини", start_node)
for node, distance in shortest_distances.items():
    print(f"Від {start_node} до {node}: {distance}")

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=20, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}, font_color='red')
plt.title("Зважений граф")
plt.show()