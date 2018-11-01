import random
import copy


class Graph(object):
    class Edge(object):
        def __init__(self, source, destination, weight):
            """
            DO NOT EDIT!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: Vertex where this edge ends
            :param weight: Value associated with this edge
            """
            self.source = source
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

    class Path(object):
        def __init__(self, vertices=list(), weight=0):
            """
            DO NOT EDIT!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            :param weight: Total weight of the path
            """
            self.vertices = vertices
            self.weight = weight

        def __eq__(self, other):
            return self.vertices == other.vertices and self.weight == other.weight

        def __repr__(self):
            return f"Weight:{self.weight} Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a vertex id to the path
            :param vertex: id of a vertex
            :return: None
            """
            self.vertices.append(vertex)

        def add_weight(self, weight):
            """
            Add weight to the path
            :param weight: weight
            :return: None
            """
            self.weight += weight

        def remove_vertex(self):
            """
            Remove the most recently added vertex from the path
            :return: None
            """
            if not self.is_empty():
                self.vertices.pop()

        def is_empty(self):
            """
            Check if the path object is empty
            :return: True if empty, False otherwise
            """
            return len(self.vertices) == 0

    class Vertex(object):
        def __init__(self, number):
            """
            Class representing a vertex in the graph
            :param number: Unique id of this vertex
            """
            self.edges = []
            self.id = number
            self.visited = False

        def __repr__(self):
            return f"Vertex: {self.id}"

        __str__ = __repr__

        def add_edge(self, destination, weight):
            pass

        def degree(self):
            pass

        def get_edge(self, destination):
            pass

        def get_edges(self):
            pass

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: List of edges
        """
        random.seed(10)
        edges = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    edges.append([i, j, random.randint(-10, 50)])
        return edges

    def __init__(self, size=0, connectedness=0):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        """
        assert connectedness <= 1
        self.adj_map = {}
        self.size = size
        self.connectedness = connectedness
        self.construct_graph()

    def construct_graph(self):
        pass

    def vertex_count(self):
        pass

    def vertices(self):
        pass

    def insert_edge(self, source, destination, weight):
        pass

    def find_valid_paths(self, source, destination, limit):
        pass

    def find_shortest_path(self, source, destination, limit):
        pass

    def find_longest_path(self, source, destination, limit):
        pass

    def find_most_vertices_path(self, source, destination, limit):
        pass


    def find_least_vertices_path(self, source, destination, limit):
        pass
