#!/usr/bin/python3

import random
from pprint import pprint


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.goal_node = False
        make_set(self)

    def __repr__(self):
        return ('<Node name: {}, neighbors: {}, goal: {}'.format(
            self.name, len(self.neighbors), self.goal_node))

    def add_neighbor(self, neighbor):
        if type(neighbor) is not Node:
            return False
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)
        return union(self, neighbor)

    def set_goal_node(self, value):
        if type(value) is not bool:
            return False
        self.goal_node = value


def make_set(node):
    node.parent = node


def find(node):
    if node.parent == node:
        return node
    return find(node.parent)


def union(x_node, y_node):
    x_node_root = find(x_node)
    y_node_root = find(y_node)
    if x_node_root == y_node_root:
        return False
    x_node_root.parent = y_node_root
    return True


def gen_nodes(node_count):
    nodes = [Node(x) for x in range(0, node_count)]
    components = len(nodes)

    while components > 1:
        x_node = nodes[random.randint(0, len(nodes)-1)]
        y_node = nodes[random.randint(0, len(nodes)-1)]
        if x_node is y_node or x_node.name in y_node.neighbors:
            continue
        if find(x_node) is find(y_node):
            if random.randint(0, 10) > 11:
                continue
        if x_node.add_neighbor(y_node):
            components -= 1

    random.choice(nodes).set_goal_node(True)

    pprint(nodes)
    return nodes
