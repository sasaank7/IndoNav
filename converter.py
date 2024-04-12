import tkinter as tk
import heapq


class DijkstraGraphTraversal:
    def __init__(self, master):
        self.master = master
        self.master.title("Dijkstra's Graph Traversal")
        self.master.geometry("800x600")

        self.canvas = tk.Canvas(master, bg="white", width=800, height=500)
        self.canvas.pack()

        self.start_node = None
        self.end_node = None
        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

        self.shortest_distance = {}
        self.visited = set()
        self.path = []

        self.draw_graph()

        self.start_node_label = tk.Label(master, text="Start Node:")
        self.start_node_label.place(x=20, y=520)
        self.start_node_entry = tk.Entry(master)
        self.start_node_entry.place(x=100, y=520)

        self.end_node_label = tk.Label(master, text="End Node:")
        self.end_node_label.place(x=250, y=520)
        self.end_node_entry = tk.Entry(master)
        self.end_node_entry.place(x=320, y=520)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse_graph)
        self.traverse_button.place(x=480, y=515)

    def draw_graph(self):
        node_positions = {
            'A': (100, 100),
            'B': (200, 100),
            'C': (200, 300),
            'D': (100, 300)
        }

        for node, connections in self.graph.items():
            x, y = node_positions[node]
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue", tags=f"node_{node}")
            self.canvas.create_text(x, y - 20, text=node, tags=f"label_{node}")

            for neighbor, weight in connections.items():
                if (neighbor, node) not in self.visited:
                    self.canvas.create_line(x, y, x, y + 20, arrow=tk.LAST, fill="black")
                    self.canvas.create_text((x + x) / 2, (y + y + 20) / 2, text=str(weight))
                    self.visited.add((node, neighbor))

    def dijkstra(self, source):
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        queue = [(0, source)]

        while queue:
            distance, current_node = heapq.heappop(queue)

            if current_node not in self.visited:
                self.visited.add(current_node)

                for neighbor, weight in self.graph[current_node].items():
                    if neighbor not in self.visited:
                        new_distance = distance + weight
                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
                            heapq.heappush(queue, (new_distance, neighbor))

        return distances

    def traverse_graph(self):
        start_node = self.start_node_entry.get().upper()
        end_node = self.end_node_entry.get().upper()

        if start_node not in self.graph or end_node not in self.graph:
            tk.messagebox.showerror("Error", "Invalid Node")
            return

        self.shortest_distance = self.dijkstra(start_node)
        self.path = [end_node]

        current_node = end_node
        while current_node != start_node:
            min_distance = float('inf')
            next_node = None
            for neighbor, weight in self.graph[current_node].items():
                if self.shortest_distance[neighbor] + weight == self.shortest_distance[current_node]:
                    if weight < min_distance:
                        min_distance = weight
                        next_node = neighbor
            self.path.append(next_node)
            current_node = next_node

        self.path.reverse()
        self.highlight_path()

    def highlight_path(self):
        shortest_path = self.path

        # Loop through each node in the shortest path
        for i in range(len(shortest_path) - 1):
            current_node = shortest_path[i]
            next_node = shortest_path[i + 1]

            # Get the coordinates of the current and next node
            x1, y1 = self.canvas.coords(f"node_{current_node}")[0], self.canvas.coords(f"node_{current_node}")[1]
            x2, y2 = self.canvas.coords(f"node_{next_node}")[0], self.canvas.coords(f"node_{next_node}")[1]

            # Highlight the edge between the current and next node
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="highlighted_path")


def main():
    root = tk.Tk()
    app = DijkstraGraphTraversal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
