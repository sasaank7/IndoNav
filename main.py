import tkinter as tk
from tkinter import ttk
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}


def print_graph(nodes):
    for node_name, node in nodes.items():
        print(f"Node: {node_name}")
        print("Neighbors:")
        for neighbor, weight in node.neighbors.items():
            print(f"\t{neighbor}: {weight}")

def add_edge(node1, node2, weight):
    node1.neighbors[node2.name] = weight
    node2.neighbors[node1.name] = weight

def initialize_nodes():
    nodes = {}
    node_names = [
        "node201", "node202", "node251", "node252", "navll", "node203", "node204", "node205", "node206",
        "node248", "node249", "node250", "navlc", "node207", "node208", "node209", "node210", "navlt",
        "node211", "node212", "node213", "node245", "node246", "node247", "naviu", "node214", "node215",
        "node216", "node231", "node232", "node233", "node217", "node218", "navrt", "node219", "node220",
        "node221", "node222", "node223", "node229", "node230", "node224", "node225", "node226", "node227",
        "node228", "navrl", "node241", "node240", "node239", "navcs", "node242", "node243", "node244",
        "navcw", "navill", "node234", "node235", "node236", "node237", "node238", "navcn", "navce", "navilr", "navil"
    ]

    for name in node_names:
        nodes[name] = Node(name)

    return nodes

def add_edges(nodes):
    # Adding edges with weights
    edges = [
        ("node201", "node202", 100), ("node201", "node252", 100), ("node201", "node251", 100), ("node201", "navll", 200),
        ("node202", "node252", 200), ("node202", "node251", 100), ("node202", "navll", 100),
        ("node251", "node252", 100), ("node251", "navll", 100),
        ("node252", "navll", 200),
        ("navll", "navlc", 600), ("navll", "navcw", 800),
        ("node203", "navll", 100), ("node203", "node204", 200),
        ("node204", "node205", 100), ("node204", "node250", 100), ("node204", "node249", 200), ("node204", "node206", 200), ("node204", "node248", 300), ("node204", "navll", 200), ("node204", "navlc", 400),
        ("node205", "node250", 100), ("node205", "node249", 200), ("node205", "node206", 100), ("node205", "node248", 200), ("node205", "navll", 300), ("node205", "navlc", 300),
        ("node206", "node250", 300), ("node206", "node249", 100), ("node206", "node248", 100), ("node206", "navll", 400), ("node206", "navlc", 200),
        ("node248", "node250", 200), ("node248", "node249", 100), ("node248", "node206", 100), ("node248", "node204", 300), ("node248", "navll", 400), ("node248", "navlc", 100),
        ("node249", "node250", 100), ("node249", "node206", 100), ("node249", "node204", 200), ("node249", "node205", 100), ("node249", "navll", 300), ("node249", "navlc", 200),
        ("node250", "node206", 200), ("node250", "node204", 100), ("node250", "node205", 200), ("node250", "navll", 200), ("node250", "navlc", 300),
        ("navlc", "navlt", 600),
        ("node207", "navlc", 100), ("node207", "node208", 100), ("node207", "node209", 200), ("node207", "navlt", 300),
        ("node208", "node209", 100), ("node208", "navlt", 200),
        ("node209", "navlt", 100),
        ("navlt", "naviu", 1100),
        ("node211", "node212", 200), ("node211", "node213", 400), ("node211", "node247", 100), ("node211", "node246", 200), ("node211", "node245", 500), ("node211", "naviu", 600),
        ("node212", "node213", 200), ("node212", "node247", 200), ("node212", "node246", 100), ("node212", "node245", 300), ("node212", "naviu", 400),
        ("node213", "node247", 400), ("node213", "node246", 200), ("node213", "node245", 100), ("node213", "naviu", 200),
        ("node245", "node247", 400), ("node245", "node246", 200), ("node245", "node211", 400), ("node245", "naviu", 200),
        ("node246", "node247", 200), ("node246", "node211", 400), ("node246", "node245", 200), ("node246", "naviu", 400),
        ("node247", "node211", 100), ("node247", "node245", 400), ("node247", "naviu", 600),
        ("naviu", "navlt", 1100), ("naviu", "navrt", 1100), ("naviu", "navil", 600),
        ("node214", "node215", 200), ("node214", "node216", 400), ("node214", "node231", 400), ("node214", "node232", 200), ("node214", "node233", 100), ("node214", "navrt", 500),
        ("node215", "node216", 200), ("node215", "node231", 200), ("node215", "node232", 100), ("node215", "node233", 200), ("node215", "navrt", 300),
        ("node216", "node231", 100), ("node216", "node232", 200), ("node216", "node233", 400), ("node216", "navrt", 100),
        ("node231", "node232", 200), ("node231", "node233", 400), ("node231", "navrt", 100),
        ("node232", "node233", 200), ("node232", "navrt", 300),
        ("node233", "navrt", 500),
        ("node217", "navrt", 100),
        ("node218", "navrt", 100),
        ("navrt", "navrl", 1200),
        ("node219", "node220", 100), ("node219", "node221", 400), ("node219", "node222", 600), ("node219", "node223", 800), ("node219", "node229", 800), ("node219", "node230", 400), ("node219", "navrl", 900),
        ("node220", "node221", 300), ("node220", "node222", 500), ("node220", "node223", 700), ("node220", "node229", 700), ("node220", "node230", 300), ("node220", "navrl", 900),
        ("node221", "node222", 200), ("node221", "node223", 400), ("node221", "node229", 400), ("node221", "node230", 100), ("node221", "navrl", 500),
        ("node222", "node223", 200), ("node222", "node229", 200), ("node222", "node230", 200), ("node222", "navrl", 300),
        ("node223", "node229", 100), ("node223", "node230", 400), ("node223", "navrl", 100),
        ("node229", "node230", 400), ("node229", "navrl", 100),
        ("node230", "navrl", 500),
        ("node224", "navrl", 100),
        ("node225", "node226", 200), ("node225", "node227", 200), ("node225", "node228", 100), ("node225", "navrl", 200),
        ("node226", "node227", 100), ("node226", "node228", 200), ("node226", "navrl", 400),
        ("node227", "node228", 200), ("node227", "navrl", 400),
        ("node228", "navrl", 200),
        ("navrl", "navce", 800),
        ("node241", "node240", 400), ("node241", "node239", 800), ("node241", "navcw", 200), ("node241", "navcs", 400),
        ("node240", "node239", 400), ("node240", "navcs", 100),
        ("node239", "navcs", 400),
        ("navcs", "navcw", 500),
        ("node242", "node243", 300), ("node242", "node244", 600), ("node242", "navcw", 100), ("node242", "navcn", 500), ("node242", "navill", 600),
        ("node243", "node244", 300), ("node243", "navcw", 400), ("node243", "navill", 300),
        ("node244", "navcw", 600), ("node244", "navill", 100),
        ("navcw", "navill", 600),
        ("node234", "node235", 100),
        ("node235", "node236", 200), ("node235", "node237", 400), ("node235", "node238", 600), ("node235", "navilr", 200), ("node235", "navce", 600),
        ("node236", "node237", 200), ("node236", "node238", 400), ("node236", "navilr", 400), ("node236", "navce", 500),
        ("node237", "node238", 200), ("node237", "navilr", 600), ("node237", "navce", 300), ("node237", "navcn", 500),
        ("node238", "navilr", 800), ("node238", "navce", 100), ("node238", "navcn", 500),
        ("navcn", "navcw", 500), ("navcn", "navce", 500),
        ("navce", "navilr", 600),
        ("navilr", "navil", 300),
        ("navil", "navill", 300), ("navil", "naviu", 600)
    ]

    for edge in edges:
        node1_name, node2_name, weight = edge
        add_edge(nodes[node1_name], nodes[node2_name], weight)

    return nodes

if __name__ == "__main__":
    nodes = initialize_nodes()
    nodes_with_edges = add_edges(nodes)
    '''for node_name, node in nodes_with_edges.items():
        print(f"Initialized node: {node_name}, Neighbors: {node.neighbors}")'''
    #print_graph(nodes)

    class_room = [
        "node201", "node250", "node249", "node208", "node209", "node210", "node211", "node213", "node215",
        "node216", "node233", "node217", "node218", "node230", "node228", "node227"
    ]
    lab = [
        "node252", "node251", "node202", "node203", "node205", "node206", "node247", "node245", "node246",
        "node212", "node231", "node232", "node219", "node221", "node222", "node223", "node225", "node226",
        "node242", "node243"
    ]
    tutorial = ["node248", "node207", "node220", "node224"]
    staff_room = ["node214", "node240", "node229"]
    staff = ["node204"]
    CSD_HOD = ["node239"]
    CSE_HOD = ["node241"]
    HOD = ["node238"]
    pg_classes = ["node236", "node237"]
    girls_waiting_room = ["node235"]
    ladies_washroom = ["node234"]
    mens_washroom = ["node244"]

    # Create a graph
    G = nx.Graph()

    # Add nodes and edges to the graph
    for node, neighbors in nodes.items():
        G.add_node(node)
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)


    def a_star(graph, start, goal):
        """
        A* algorithm to find the shortest path between start and goal nodes in a graph.
        """

        # Heuristic function (straight line distance between two nodes)
        def heuristic(n1, n2):
            return abs(ord(n1[4]) - ord(n2[4])) + abs(int(n1[5:]) - int(n2[5:]))

        # Priority queue for open nodes
        open_nodes = [(0 + heuristic(start, goal), start)]
        # Set of visited nodes
        visited = set()
        # Parent nodes to reconstruct the path
        parents = {}

        while open_nodes:
            # Pop the node with the smallest f value
            current_f, current_node = min(open_nodes)
            open_nodes.remove((current_f, current_node))

            # Check if goal reached
            if current_node == goal:
                path = [current_node]
                while current_node != start:
                    current_node = parents[current_node]
                    path.append(current_node)
                path.reverse()
                return path

            # Mark current node as visited
            visited.add(current_node)

            # Explore neighbors
            for neighbor in graph.neighbors(current_node):
                # Skip visited nodes
                if neighbor in visited:
                    continue

                # Calculate tentative g value
                tentative_g = graph[current_node][neighbor]["weight"]

                # Add neighbor to open nodes if not already in the queue
                if neighbor not in (node for _, node in open_nodes):
                    open_nodes.append((tentative_g + heuristic(neighbor, goal), neighbor))
                    parents[neighbor] = current_node
                elif tentative_g < graph[parents[neighbor]][neighbor]["weight"]:
                    parents[neighbor] = current_node


    # GUI setup
    def on_select():
        """
        Event handler for clicking the button.
        """
        start = start_var.get()
        end = end_var.get()

        # Find the shortest path using A* algorithm
        shortest_path = a_star(G, start, end)

        # Display the shortest path
        print("Shortest Path:", shortest_path)


    root = tk.Tk()
    root.title("Indoor Navigation")

    # Add widgets
    start_label = ttk.Label(root, text="Select Start Node:")
    start_label.grid(row=0, column=0)
    start_var = tk.StringVar()
    start_dropdown = ttk.Combobox(root, textvariable=start_var, values=list(G.nodes()))
    start_dropdown.grid(row=0, column=1)

    end_label = ttk.Label(root, text="Select End Node:")
    end_label.grid(row=1, column=0)
    end_var = tk.StringVar()
    end_dropdown = ttk.Combobox(root, textvariable=end_var, values=list(G.nodes()))
    end_dropdown.grid(row=1, column=1)

    find_button = ttk.Button(root, text="Find Shortest Path", command=on_select)
    find_button.grid(row=2, columnspan=2)

    root.mainloop()