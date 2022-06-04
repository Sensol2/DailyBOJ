import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, item):
        self.item = item
        self.left_node = None
        self.right_node = None

    def AddChildNode(self, new_node):

        if self.item > new_node.item and not self.left_node:
            self.left_node = new_node
            # print("Added ", new_node.item, "in parent", node.item)
            return
        elif self.item < new_node.item and not self.right_node:
            self.right_node = new_node
            # print("Added ", new_node.item, "in parent", node.item)
            return
        else:
            if self.left_node and self.item > new_node.item:
                self.left_node.AddChildNode(new_node)
            if self.right_node:
                self.right_node.AddChildNode(new_node)

    def PrintbyPostfix(self):

        if self.left_node:
            self.left_node.PrintbyPostfix()
        if self.right_node:
            self.right_node.PrintbyPostfix()
        print(self.item)


root = int(input())
node = Node(root)

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    node.AddChildNode(Node(int(line)))

node.PrintbyPostfix()
