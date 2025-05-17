import os
import sys
from linked_list.Node import Node

# Get the absolute path of the current file (main.py)
current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(current_file_path)

# Add the root directory to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import your modules


class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, key, product):
        new_node = Node(key, product)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        if not self.head:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current and current.key != key:
            previous = current
            current = current.next

        if current:
            previous.next = current.next

        return None

    def find(self, key):
        if not self.head:
            return None

        current = self.head
        while current:
            if current.key == key:
                return current.product
            current = current.next

        return None

    def entries(self):
        current = self.head

        while current:
            yield (current.key, current.product)
            current = current.next
