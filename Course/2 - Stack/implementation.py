# ==========================================================
# STACK — IMPLEMENTATION (using Python list)
# ==========================================================


class Stack:
    """LIFO data structure."""

    def __init__(self):
        self.items = []

    def push(self, value):
        """Add item to top. O(1)"""
        self.items.append(value)

    def pop(self):
        """Remove and return top item. O(1)"""
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """Return top item without removing. O(1)"""
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """Return True if stack is empty. O(1)"""
        return len(self.items) == 0

    def size(self):
        """Return number of items. O(1)"""
        return len(self.items)


# ==========================================================
# STACK — IMPLEMENTATION (using Linked List)
# ==========================================================


class Node:
    """Singly linked list node."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    """LIFO data structure built on linked list."""

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        """Add item to top. O(1)"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return top item. O(1)"""
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def peek(self):
        """Return top item without removing. O(1)"""
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        """Return True if stack is empty. O(1)"""
        return self.top is None

    def size(self):
        """Return number of items. O(1)"""
        return self._size


# ==========================================================
# USAGE EXAMPLE
# ==========================================================

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # 30
print(stack.peek())  # 20
print(stack.size())  # 2
