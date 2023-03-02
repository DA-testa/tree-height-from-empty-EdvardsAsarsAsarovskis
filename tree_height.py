import sys
import threading

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
    stack = [root]
    while stack:
        level_size = len(stack)
        while level_size:
            node = stack.pop(0)
            level_size -= 1
            for child in node.children:
                stack.append(child)
        height += 1

    return height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(parents))

if __name__ == '__main__':
    main()
