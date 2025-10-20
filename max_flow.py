from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        """Додає ребро з пропускною здатністю"""
        self.graph[u][v] = capacity
        # Зворотне ребро з нульовою пропускною здатністю
        if v not in self.graph or u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        """Пошук у ширину для знаходження шляху з вільною пропускною здатністю"""
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def edmonds_karp(self, source, sink):
        """Основний алгоритм обчислення максимального потоку"""
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            # Знаходимо мінімальну пропускну здатність уздовж шляху
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Оновлюємо залишкові пропускні здатності
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


def build_logistics_network():
    """Створює граф логістичної мережі"""
    g = Graph()

    terminals = ["T1", "T2"]
    storages = ["S1", "S2", "S3", "S4"]
    shops = [f"M{i}" for i in range(1, 15)]

    edges = [
        ("T1", "S1", 25), ("T1", "S2", 20), ("T1", "S3", 15),
        ("T2", "S3", 15), ("T2", "S4", 30), ("T2", "S2", 10),
        ("S1", "M1", 15), ("S1", "M2", 10), ("S1", "M3", 20),
        ("S2", "M4", 15), ("S2", "M5", 10), ("S2", "M6", 25),
        ("S3", "M7", 20), ("S3", "M8", 15), ("S3", "M9", 10),
        ("S4", "M10", 20), ("S4", "M11", 10), ("S4", "M12", 15),
        ("S4", "M13", 5), ("S4", "M14", 10)
    ]

    for u, v, c in edges:
        g.add_edge(u, v, c)

    # Додаємо суперджерело і супервитік
    g.add_edge("Source", "T1", 100)
    g.add_edge("Source", "T2", 100)
    for m in shops:
        g.add_edge(m, "Sink", 100)

    return g


if __name__ == "__main__":
    g = build_logistics_network()
    max_flow = g.edmonds_karp("Source", "Sink")
    print(f"🔹 Максимальний потік у мережі: {max_flow}")
