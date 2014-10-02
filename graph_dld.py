#!/usr/bin/env python
# encoding: utf-8

### Structure
## Create a graph object based on a dictionary
# graph = {node: [edge_list]}
# edge = [tailnode, weight=1]
# def make_graph()
# def addNode()
# def connectNodes()
# def changeWeight()
# def weights_decay()
# def indicate_hill_node()
# def indicate_cake_node()

import math

math.asinh(


class Node(object):

    def __init__(self, name):
        self.name = name


class graph(object):
    """Generic graph class, implemented with a dictionary."""

    def __init__(self, d={"hill": None}):
        """@TODO: to be defined

        :d: @TODO

        """
        #TODO (--) check correctness of input graph
        self.d = d

    def add_node(self, graph, node=None, edge_list=None):
        if node:
            graph[node] = edge_list
            return True
        node = len(graph)
        graph[node] = edge_list
        return True

    def connect_nodes(self):
        pass


    def change_weight(self):
        pass


    def weights_decay(self):
        pass


    def indicate_hill_node(self):
        pass


    def indicate_cake_node(self):
        pass
