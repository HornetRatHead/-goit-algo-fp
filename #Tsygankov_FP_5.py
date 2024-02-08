#Tsygankov_FP_5

import uuid
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root, traversal='DFS'):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    
    if traversal == 'DFS':
        visited = set()
        dfs_color = iter(generate_gradient_rgb((18, 1, 240), (238, 130, 238), 10))  # Створюємо градієнт кольорів для DFS
        dfs_traverse(heap_root, heap, pos, visited, dfs_color)
    elif traversal == 'BFS':
        bfs_color = iter(generate_gradient_rgb((18, 1, 240), (135, 206, 235), 10))  # Створюємо градієнт кольорів для BFS
        bfs_traverse(heap_root, heap, pos, bfs_color)
    
    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_gradient_rgb(start_rgb, end_rgb, n_steps):
    r_step = (end_rgb[0] - start_rgb[0]) / (n_steps - 1)
    g_step = (end_rgb[1] - start_rgb[1]) / (n_steps - 1)
    b_step = (end_rgb[2] - start_rgb[2]) / (n_steps - 1)
    
    for i in range(n_steps):
        r = int(start_rgb[0] + r_step * i)
        g = int(start_rgb[1] + g_step * i)
        b = int(start_rgb[2] + b_step * i)
        yield '#{:02X}{:02X}{:02X}'.format(r, g, b)

def dfs_traverse(node, graph, pos, visited, dfs_color):
    if node is None:
        return
    
    if node.id not in visited:
        visited.add(node.id)
        color = next(dfs_color)
        graph.add_node(node.id, color=color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = pos[node.id][0] - 1
            pos[node.left.id] = (l, pos[node.id][1] - 1)
            dfs_traverse(node.left, graph, pos, visited, dfs_color)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = pos[node.id][0] + 1
            pos[node.right.id] = (r, pos[node.id][1] - 1)
            dfs_traverse(node.right, graph, pos, visited, dfs_color)

def bfs_traverse(node, graph, pos, bfs_color):
    queue = [(node, 0)]
    
    while queue:
        current, level = queue.pop(0)
        color = next(bfs_color)
        graph.add_node(current.id, color=color, label=current.val)
        
        if current.left:
            graph.add_edge(current.id, current.left.id)
            l = pos[current.id][0] - 1
            pos[current.left.id] = (l, pos[current.id][1] - 1)
            queue.append((current.left, level + 1))
        if current.right:
            graph.add_edge(current.id, current.right.id)
            r = pos[current.id][0] + 1
            pos[current.right.id] = (r, pos[current.id][1] - 1)
            queue.append((current.right, level + 1))

# Створення бінарного дерева
root = Node(10)
root.left = Node(8)
root.left.left = Node(6)
root.left.right = Node(7)
root.right = Node(9)
root.right.left = Node(4)
root.right.right = Node(5)

# Візуалізація дерева
draw_heap(root, traversal='DFS')
draw_heap(root, traversal='BFS')


