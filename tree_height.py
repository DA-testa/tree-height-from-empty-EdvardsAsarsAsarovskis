import sys
import threading
import os.path

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

def compute_height(parents):
    # Create a list of nodes for each index
    nodes = [Node(i) for i in range(len(parents))]

    # Link each node to its parent
    for child_index in range(len(parents)):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = nodes[child_index]
        else:
            parent_node = nodes[parent_index]
            parent_node.children.append(nodes[child_index])

    # Compute height using a depth-first search
    height = 0
    stack = [(root, 1)]
    while stack:
        node, level = stack.pop()
        if not node.children:
            height = max(height, level)
        for child in node.children:
            stack.append((child, level+1))

    return height


def main():
    choice = input()
    tree = list(map(int, input().split()))
    height = compute_height(tree)
    if choice == "I":
        print(height)
    else:
        print(height)

if __name__ == "__main__":
    main()


