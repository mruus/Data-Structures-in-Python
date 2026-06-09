# ==========================================================
# LINKED LIST — IMPLEMENTATION
# ==========================================================


class Node:
    """Singly linked list node."""

    def __init__(self, value):
        self.value = value
        self.next = None


# --- CREATING & CONNECTING NODES ---

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)

first_node.next = second_node
second_node.next = third_node
# Result: 10 -> 20 -> 30 -> None


# ==========================================================
# LINKED LIST CLASS
# ==========================================================


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """Print all nodes. O(n)"""
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def insert_at_beginning(self, value):
        """Add node at start. O(1)"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        """Add node at end. O(n)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def search(self, target_value):
        """Return True if value found. O(n)"""
        current_node = self.head
        while current_node:
            if current_node.value == target_value:
                return True
            current_node = current_node.next
        return False

    def delete_first(self):
        """Remove head node. O(1)"""
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        """Remove tail node. O(n)"""
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delete_by_value(self, value_to_delete):
        """Remove first node with given value. O(n)"""
        if self.head is None:
            return
        if self.head.value == value_to_delete:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value_to_delete:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def get_length(self):
        """Return number of nodes. O(n)"""
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def reverse(self):
        """Reverse list in-place. O(n) time, O(1) space."""
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


# ==========================================================
# USAGE EXAMPLE
# ==========================================================

linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.delete_first()
linked_list.delete_last()
linked_list.print_list()
# Output: 10 -> 20 -> 30 -> None
found = linked_list.search(2)
print("Node found => ", found)


# ==========================================================
# DOUBLY LINKED LIST NODE
# ==========================================================


class DoublyNode:
    """Doubly linked list node."""

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
