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
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute tree height
    height = compute_height(parents)

    # Print output
    print(height)


if __name__ == '__main__':
    main()



def main():
    choice = input("Enter 'F' to read input from file or 'I' to enter input from keyboard: ")
    if choice.upper() == 'F':
        file_name = input("Enter the file name to read input from (file name should not contain 'a'): ")
        if 'a' in file_name:
            print("Invalid file name! File name should not contain 'a'.")
            return
        try:
            with open('input_files/' + file_name, 'r') as f:
                input_data = f.read().strip()
        except FileNotFoundError:
            print("File not found!")
            return
    elif choice.upper() == 'I':
        input_data = read_input_from_keyboard()
    else:
        print("Invalid choice!")
        return

    # call the function to perform the task
    result = perform_task(input_data)

    # print the result
    print(result)


if __name__ == '__main__':
    main()

