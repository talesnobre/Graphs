class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for i in range(num_vertices)]
        self.adj_list = [[] for i in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def bfs_path(self, s, t):
        visited = [False] * self.num_vertices
        queue = []
        path = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            path.append(u)

            if u == t:
                return path

            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

        return "Não há caminho entre os vértices"

    def dfs_path(self, s, t):
        visited = [False] * self.num_vertices
        stack = []
        path = []

        stack.append(s)

        while stack:
            u = stack.pop()
            path.append(u)

            if u == t:
                return path

            if not visited[u]:
                visited[u] = True

                for v in reversed(self.adj_list[u]):
                    if not visited[v]:
                        stack.append(v)

        return "Não há caminho entre os vértices"