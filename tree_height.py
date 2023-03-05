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

def read_input_from_keyboard():
    n = int(input())
    parents = list(map(int, input().split()))
    return n, parents

def read_input_from_file(file_name):
    try:
        with open(os.path.join("input_files", file_name), "r") as f:
            input_data = f.read().strip()
            n, parents = input_data.split("\n")
            n = int(n)
            parents = list(map(int, parents.split()))
            return n, parents
    except FileNotFoundError:
        print("File not found!")
        return None, None
    except ValueError:
        print("Invalid input file format!")
        return None, None

def perform_task(input_data):
    n, parents = input_data
    return compute_height(parents)

def main():
    choice = input("Enter 'F' to read input from file or 'I' to enter input from keyboard: ")
    if choice.upper() == 'F':
        while True:
            file_name = input("Enter the file name to read input from (file name should not contain 'a'): ")
            if 'a' in file_name:
                print("Invalid file name! File name should not contain 'a'.")
            else:
                break
        input_data = read_input_from_file(file_name)
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
