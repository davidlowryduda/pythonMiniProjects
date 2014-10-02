"""
Better idea. Lay a weight 1 trail to the cake, and a weight 3 trail back.
"""
import random


class Vertex:
    def __init__(self, key):
        self.name = key
        self.connections = {}

    def add_neighbor(self, nbr, weight=1):
        self.connections[nbr] = weight

    def __str__(self):
        return str(self.name) + ' connectedTo: ' + str([x.name for x in self.connections])

    def get_connections(self):
        return self.connections.keys()

    def get_name(self):
        return self.name

    def get_weight(self, nbr):
        return self.connections[nbr]


class Graph(object):
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertex_list

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if from_vertex not in self.vertex_list:
            nv1 = self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_list:
            nv2 = self.add_vertex(to_vertex)
        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], weight)

    def add_edge_both(self, from_vertex, to_vertex, weight=1):
        self.add_edge(from_vertex, to_vertex, weight)
        self.add_edge(to_vertex, from_vertex, weight)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())


class Ant(object):
    visit_weight = 1
    decay_rate = 0.9

    def __init__(self, graph):
        self.visited_list = []
        self.graph = graph
        self.done = False

    def designate_start(self, vertex):
        self.start = vertex
        self.location = self.start
        self.visited_list.append(vertex)

    def designate_goal(self, vertex):
        self.goal = vertex

    def move(self):
        starting_location = self.location
        connections = []
        total_weight = 0
        for neighbor in starting_location.get_connections():
            # Don't go to last node
            if neighbor != self.visited_list[-1]:
                weight = starting_location.get_weight(neighbor)
                total_weight = total_weight + weight
                connections.append([neighbor, weight])

        cutoff = random.random()*total_weight
        found = False
        while not found:
            place = connections.pop()
            cutoff = cutoff - place[1]
            if cutoff < 0:
                found = True
                break
            if len(connections) == 0:
                print "ERROR in while loop"
        destination = place[0]
        self.location = destination

        # Deposit pheremone trail
        starting_location.add_neighbor(destination, starting_location.get_weight(destination) +
                                       self.visit_weight)
        destination.add_neighbor(starting_location, destination.get_weight(starting_location) +
                                 self.visit_weight)
        #starting_location[destination] = starting_location[destination] + self.visit_weight
        #destination[starting_location] = destination[starting_location] + self.visit_weight

        self.edge_decay()

        if self.location == self.goal:
            self.done = True
            print "You made it!"

    def edge_decay(self):
        #TODO decay
        """
        for node in graph:
            for neighbor in node.neighbors:
                node[neighbor] = node[neighbor]*decay_rate
        """
        pass


g = Graph()
for i in range(6):
    g.add_vertex(i)
g.vertex_list
g.add_edge_both(0,1,5)
g.add_edge_both(0,5,2)

for v in g:
    for w in v.get_connections():
        print v.get_name(), w.get_name()

Ant1 = Ant(g)
Ant1.designate_start(g.vertex_list[0])
Ant1.designate_goal(g.vertex_list[1])
Ant1.move()
print Ant1.location
