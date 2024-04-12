import heapq

def dijkstra(graph, source, destination):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    visited = set()
    queue = [(0, source)]

    while queue:
        distance, current_node = heapq.heappop(queue)

        if current_node == destination:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))

    if distances[destination] == float('inf'):
        return float('inf'), []

    # Reconstruct the shortest path
    shortest_path = []
    current_node = destination
    while current_node != source:
        shortest_path.append(current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                current_node = neighbor
                break
    shortest_path.append(source)
    shortest_path.reverse()

    return distances[destination], shortest_path


def print_graph(graph):
    for node, connections in graph.items():
        print(f"Node {node}:")
        for neighbor, distance in node, connections.items():
            print(f"    -> {neighbor} (Distance: {distance})")

edges_dict = {'node201': {'node202': 100, 'node252': 100, 'node251': 100, 'navll': 200}, 'node202': {'node201': 100, 'node252': 200, 'node251': 100, 'navll': 100}, 'node252': {'node201': 100, 'node202': 200, 'node251': 100, 'navll': 200}, 'node251': {'node201': 100, 'node202': 100, 'node252': 100, 'navll': 100}, 'navll': {'node201': 200, 'node202': 100, 'node251': 100, 'node252': 200, 'navlc': 600, 'navcw': 800, 'node203': 100, 'node204': 200, 'node205': 300, 'node206': 400, 'node248': 400, 'node249': 300, 'node250': 200}, 'navlc': {'navll': 600, 'node204': 400, 'node205': 300, 'node206': 200, 'node248': 100, 'node249': 200, 'node250': 300, 'navlt': 600, 'node207': 100}, 'navcw': {'navll': 800, 'node241': 200, 'navcs': 500, 'node242': 100, 'node243': 400, 'node244': 600, 'navill': 600, 'navcn': 500}, 'node203': {'navll': 100, 'node204': 200}, 'node204': {'node203': 200, 'node205': 100, 'node250': 100, 'node249': 200, 'node206': 200, 'node248': 300, 'navll': 200, 'navlc': 400}, 'node205': {'node204': 100, 'node250': 200, 'node249': 100, 'node206': 100, 'node248': 200, 'navll': 300, 'navlc': 300}, 'node250': {'node204': 100, 'node205': 200, 'node206': 200, 'node248': 200, 'node249': 100, 'navll': 200, 'navlc': 300}, 'node249': {'node204': 200, 'node205': 100, 'node206': 100, 'node248': 100, 'node250': 100, 'navll': 300, 'navlc': 200}, 'node206': {'node204': 200, 'node205': 100, 'node250': 200, 'node249': 100, 'node248': 100, 'navll': 400, 'navlc': 200}, 'node248': {'node204': 300, 'node205': 200, 'node206': 100, 'node250': 200, 'node249': 100, 'navll': 400, 'navlc': 100}, 'navlt': {'navlc': 600, 'node207': 300, 'node208': 200, 'node209': 100, 'naviu': 1100}, 'node207': {'navlc': 100, 'node208': 100, 'node209': 200, 'navlt': 300}, 'node208': {'node207': 100, 'node209': 100, 'navlt': 200}, 'node209': {'node207': 200, 'node208': 100, 'navlt': 100}, 'naviu': {'navlt': 1100, 'node211': 600, 'node212': 400, 'node213': 200, 'node245': 200, 'node246': 400, 'node247': 600, 'navrt': 1100, 'navil': 600}, 'node211': {'node212': 200, 'node213': 400, 'node247': 100, 'node246': 400, 'node245': 400, 'naviu': 600}, 'node212': {'node211': 200, 'node213': 200, 'node247': 200, 'node246': 100, 'node245': 300, 'naviu': 400}, 'node213': {'node211': 400, 'node212': 200, 'node247': 400, 'node246': 200, 'node245': 100, 'naviu': 200}, 'node247': {'node211': 100, 'node212': 200, 'node213': 400, 'node245': 400, 'node246': 200, 'naviu': 600}, 'node246': {'node211': 400, 'node212': 100, 'node213': 200, 'node245': 200, 'node247': 200, 'naviu': 400}, 'node245': {'node211': 400, 'node212': 300, 'node213': 100, 'node247': 400, 'node246': 200, 'naviu': 200}, 'navrt': {'naviu': 1100, 'node214': 500, 'node215': 300, 'node216': 100, 'node231': 100, 'node232': 300, 'node233': 500, 'node217': 100, 'node218': 100, 'navrl': 1200}, 'navil': {'naviu': 600, 'navilr': 300, 'navill': 300}, 'node214': {'node215': 200, 'node216': 400, 'node231': 400, 'node232': 200, 'node233': 100, 'navrt': 500}, 'node215': {'node214': 200, 'node216': 200, 'node231': 200, 'node232': 100, 'node233': 200, 'navrt': 300}, 'node216': {'node214': 400, 'node215': 200, 'node231': 100, 'node232': 200, 'node233': 400, 'navrt': 100}, 'node231': {'node214': 400, 'node215': 200, 'node216': 100, 'node232': 200, 'node233': 400, 'navrt': 100}, 'node232': {'node214': 200, 'node215': 100, 'node216': 200, 'node231': 200, 'node233': 200, 'navrt': 300}, 'node233': {'node214': 100, 'node215': 200, 'node216': 400, 'node231': 400, 'node232': 200, 'navrt': 500}, 'node217': {'navrt': 100}, 'node218': {'navrt': 100}, 'navrl': {'navrt': 1200, 'node219': 900, 'node220': 900, 'node221': 500, 'node222': 300, 'node223': 100, 'node229': 100, 'node230': 500, 'node224': 100, 'node225': 200, 'node226': 400, 'node227': 400, 'node228': 200, 'navce': 800}, 'node219': {'node220': 100, 'node221': 400, 'node222': 600, 'node223': 800, 'node229': 800, 'node230': 400, 'navrl': 900}, 'node220': {'node219': 100, 'node221': 300, 'node222': 500, 'node223': 700, 'node229': 700, 'node230': 300, 'navrl': 900}, 'node221': {'node219': 400, 'node220': 300, 'node222': 200, 'node223': 400, 'node229': 400, 'node230': 100, 'navrl': 500}, 'node222': {'node219': 600, 'node220': 500, 'node221': 200, 'node223': 200, 'node229': 200, 'node230': 200, 'navrl': 300}, 'node223': {'node219': 800, 'node220': 700, 'node221': 400, 'node222': 200, 'node229': 100, 'node230': 400, 'navrl': 100}, 'node229': {'node219': 800, 'node220': 700, 'node221': 400, 'node222': 200, 'node223': 100, 'node230': 400, 'navrl': 100}, 'node230': {'node219': 400, 'node220': 300, 'node221': 100, 'node222': 200, 'node223': 400, 'node229': 400, 'navrl': 500}, 'node224': {'navrl': 100}, 'node225': {'node226': 200, 'node227': 200, 'node228': 100, 'navrl': 200}, 'node226': {'node225': 200, 'node227': 100, 'node228': 200, 'navrl': 400}, 'node227': {'node225': 200, 'node226': 100, 'node228': 200, 'navrl': 400}, 'node228': {'node225': 100, 'node226': 200, 'node227': 200, 'navrl': 200}, 'navce': {'navrl': 800, 'node235': 600, 'node236': 500, 'node237': 300, 'node238': 100, 'navcn': 500, 'navilr': 600}, 'node241': {'node240': 400, 'node239': 800, 'navcw': 200, 'navcs': 400}, 'node240': {'node241': 400, 'node239': 400, 'navcs': 100}, 'node239': {'node241': 800, 'node240': 400, 'navcs': 400}, 'navcs': {'node241': 400, 'node240': 100, 'node239': 400, 'navcw': 500}, 'node242': {'node243': 300, 'node244': 600, 'navcw': 100, 'navcn': 500, 'navill': 600}, 'node243': {'node242': 300, 'node244': 300, 'navcw': 400, 'navill': 300}, 'node244': {'node242': 600, 'node243': 300, 'navcw': 600, 'navill': 100}, 'navcn': {'node242': 500, 'node237': 500, 'node238': 500, 'navcw': 500, 'navce': 500}, 'navill': {'node242': 600, 'node243': 300, 'node244': 100, 'navcw': 600, 'navil': 300}, 'node234': {'node235': 100}, 'node235': {'node234': 100, 'node236': 200, 'node237': 400, 'node238': 600, 'navilr': 200, 'navce': 600}, 'node236': {'node235': 200, 'node237': 200, 'node238': 400, 'navilr': 400, 'navce': 500}, 'node237': {'node235': 400, 'node236': 200, 'node238': 200, 'navilr': 600, 'navce': 300, 'navcn': 500}, 'node238': {'node235': 600, 'node236': 400, 'node237': 200, 'navilr': 800, 'navce': 100, 'navcn': 500}, 'navilr': {'node235': 200, 'node236': 400, 'node237': 600, 'node238': 800, 'navce': 600, 'navil': 300}}

'''source_node = input("Enter source node: ")
destination_node = input("Enter destination node: ")
shortest_distance, shortest_path = dijkstra(edges_dict, source_node, destination_node)
print(f"Shortest distance from {source_node} to {destination_node}: {shortest_distance}")
print(f"Shortest path: {' -> '.join(shortest_path)}")'''

#print_graph(edges_dict)


'''import tkinter as tk
from tkinter import messagebox


def on_submit():
    source_node = source_entry.get()
    destination_node = destination_entry.get()
    shortest_distance, shortest_path = dijkstra(edges_dict, source_node, destination_node)

    if shortest_distance == float('inf'):
        messagebox.showinfo("Error", f"No path exists from {source_node} to {destination_node}.")
        return

    shortest_distance_label.config(text=f"Shortest distance: {shortest_distance}")
    shortest_path_label.config(text=f"Shortest path: {' -> '.join(shortest_path)}")

    # Highlight the shortest path nodes in red color
    for node in shortest_path:
        node_labels[node].config(bg='red')


# Create the Tkinter window
window = tk.Tk()
window.title("Shortest Path Finder")

# Create labels and entry fields for source and destination nodes
source_label = tk.Label(window, text="Source Node:")
source_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
source_entry = tk.Entry(window)
source_entry.grid(row=0, column=1, padx=10, pady=5)

destination_label = tk.Label(window, text="Destination Node:")
destination_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
destination_entry = tk.Entry(window)
destination_entry.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(window, text="Find Shortest Path", command=on_submit)
submit_button.grid(row=2, columnspan=2, padx=10, pady=10)

shortest_distance_label = tk.Label(window, text="")
shortest_distance_label.grid(row=3, columnspan=2, padx=10, pady=5)

shortest_path_label = tk.Label(window, text="")
shortest_path_label.grid(row=4, columnspan=2, padx=10, pady=5)

# Create labels for all nodes
node_labels = {}
for node in edges_dict:
    node_labels[node] = tk.Label(window, text=node, bg="lightgrey", padx=10, pady=5, relief="solid")
    node_labels[node].grid(row=5 + list(edges_dict.keys()).index(node), column=0, padx=10, pady=2, sticky="w")

window.mainloop()'''

import heapq
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

'''
def dijkstra(graph, source, destination):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    visited = set()
    queue = [(0, source)]

    while queue:
        distance, current_node = heapq.heappop(queue)

        if current_node == destination:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))

    if distances[destination] == float('inf'):
        return float('inf'), []

    # Reconstruct the shortest path
    shortest_path = []
    current_node = destination
    while current_node != source:
        shortest_path.append(current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                current_node = neighbor
                break
    shortest_path.append(source)
    shortest_path.reverse()

    return distances[destination], shortest_path'''


def plot_graph(graph):
    fig = Figure(figsize=(8, 6))
    plot = fig.add_subplot(111)

    for node, connections in graph.items():
        for neighbor, distance in connections.items():
            plot.plot([node, neighbor], [0, distance], marker='o')

    return fig


def highlight_shortest_path(graph, shortest_path):
    fig = plot_graph(graph)
    plot = fig.get_axes()[0]

    for i in range(len(shortest_path) - 1):
        node1 = shortest_path[i]
        node2 = shortest_path[i + 1]
        plot.plot([node1, node2], [0, graph[node1][node2]], color='red', marker='o')

    return fig


def show_result():
    source_node = source_entry.get()
    destination_node = destination_entry.get()

    shortest_distance, shortest_path = dijkstra(edges_dict, source_node, destination_node)
    shortest_distance_label.config(text=f"Shortest distance: {shortest_distance}")

    shortest_path_figure = highlight_shortest_path(edges_dict, shortest_path)
    canvas = FigureCanvasTkAgg(shortest_path_figure, master=root)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=3, columnspan=2)


root = tk.Tk()
root.title("Shortest Path Visualization")

source_label = tk.Label(root, text="Source Node:")
source_label.grid(row=0, column=0)
source_entry = tk.Entry(root)
source_entry.grid(row=0, column=1)

destination_label = tk.Label(root, text="Destination Node:")
destination_label.grid(row=1, column=0)
destination_entry = tk.Entry(root)
destination_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=show_result)
calculate_button.grid(row=2, columnspan=2)

shortest_distance_label = tk.Label(root, text="")
shortest_distance_label.grid(row=4, columnspan=2)

root.mainloop()
