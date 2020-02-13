from Tree.node import Node


class Tree:
    def __init__(self):
        self.root = None

    def add_root(self, object):
        root = Node(object)
        self.root = root
        return root

    def add_right(self, father, object):
        child = Node(object)
        father.right = child
        child.father = father
        return child

    def add_left(self, father, object):
        child = Node(object)
        father.left = child
        child.father = father
        return child