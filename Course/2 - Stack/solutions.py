# ==========================================================
# STACK — SOLUTIONS
# ==========================================================

class Stack:
    """LIFO data structure."""

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ==========================================================
# EXERCISE 1 — REVERSE A STRING
# ==========================================================

def reverse_string(text):
    """Push every char, then pop every char. O(n)"""
    stack = Stack()
    for char in text:
        stack.push(char)

    reversed_chars = []
    while not stack.is_empty():
        reversed_chars.append(stack.pop())

    return "".join(reversed_chars)


print("1 - Reverse a String")
print(reverse_string("mansuur abdullahi abdirahman"))  # olleh
print()


# ==========================================================
# EXERCISE 2 — BALANCED PARENTHESES
# ==========================================================

def is_balanced(expression):
    """Return True if all brackets match. O(n)"""
    stack = Stack()
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


print("2 - Balanced Parentheses")
print(is_balanced("({[]})"))  # True
print(is_balanced("({[})"))   # False
print(is_balanced("()"))      # True
print(is_balanced("("))       # False
print(is_balanced(")"))       # False
print()


# ==========================================================
# EXERCISE 4 — MIN STACK
# ==========================================================

class MinStack:
    """Stack that returns the minimum value in O(1)."""

    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, value):
        self.stack.push(value)
        if self.min_stack.is_empty() or value <= self.min_stack.peek():
            self.min_stack.push(value)

    def pop(self):
        if self.stack.is_empty():
            return None
        value = self.stack.pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value

    def peek(self):
        return self.stack.peek()

    def get_min(self):
        return self.min_stack.peek()

    def is_empty(self):
        return self.stack.is_empty()


print("4 - Min Stack")
ms = MinStack()
ms.push(5)
print("min:", ms.get_min())  # 5
ms.push(3)
print("min:", ms.get_min())  # 3
ms.push(7)
print("min:", ms.get_min())  # 3
ms.pop()
print("min:", ms.get_min())  # 3
ms.pop()
print("min:", ms.get_min())  # 5
print()


# ==========================================================
# EXERCISE 5 — EVALUATE POSTFIX EXPRESSION
# ==========================================================

def evaluate_postfix(expression):
    """Evaluate a postfix expression. O(n)"""
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()  # second operand
            a = stack.pop()  # first operand
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a / b)
        else:
            stack.push(int(token))

    return stack.pop()


print("5 - Evaluate Postfix Expression")
print(evaluate_postfix("3 4 +"))               # 7
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))   # 14
print()


# ==========================================================
# EXERCISE 6 — STACK USING ARRAY (FIXED SIZE)
# ==========================================================

class ArrayStack:
    """Fixed-size stack using a pre-allocated array."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            raise OverflowError("Stack is full")
        self.top += 1
        self.items[self.top] = value

    def pop(self):
        if self.is_empty():
            return None
        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1


print("6 - Array Stack")
arr_stack = ArrayStack(3)
arr_stack.push(10)
arr_stack.push(20)
arr_stack.push(30)
print(arr_stack.pop())  # 30
print(arr_stack.pop())  # 20
print(arr_stack.pop())  # 10
print()


# ==========================================================
# EXERCISE 7 — REVERSE A STACK (RECURSION)
# ==========================================================

def reverse_stack(stack):
    """Reverse a stack in-place using recursion. No extra data structure."""
    if stack.is_empty():
        return

    top = stack.pop()
    reverse_stack(stack)
    _insert_at_bottom(stack, top)


def _insert_at_bottom(stack, value):
    """Helper: insert a value at the bottom of the stack."""
    if stack.is_empty():
        stack.push(value)
        return

    top = stack.pop()
    _insert_at_bottom(stack, value)
    stack.push(top)


print("7 - Reverse a Stack")
rev_stack = Stack()
rev_stack.push(10)
rev_stack.push(20)
rev_stack.push(30)
print("Before:", end=" ")
temp = []
while not rev_stack.is_empty():
    temp.append(rev_stack.pop())
print(temp)  # [30, 20, 10] — was built from top to bottom

# Rebuild and reverse
for val in [10, 20, 30]:
    rev_stack.push(val)
reverse_stack(rev_stack)
print("After:", end=" ")
temp = []
while not rev_stack.is_empty():
    temp.append(rev_stack.pop())
print(temp)  # [10, 20, 30] — reversed
print()


# ==========================================================
# FINAL CHALLENGE ANSWERS
# ==========================================================

print("Final Challenge Answers")
print("1. LIFO = Last In, First Out — the last item pushed is the first item popped.")
print("2. Every operation is O(1) because you only touch the top — no traversal needed.")
print("3. Top in a Python list-based stack: the last element (self.items[-1]).")
print("4. Top in a linked list-based stack: the head node (self.top).")
print("5. You can't access the middle because the stack intentionally hides everything below the top.")
print("6. Real-world uses: (a) undo/redo, (b) browser back button, (c) function call stack.")
