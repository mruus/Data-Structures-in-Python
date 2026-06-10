# Stack Practice Exercises

## Important

Do **not** search for solutions.

Do **not** ask AI to write the code.

Use only your `Stack` implementation as reference.

Before writing any code:

1. Draw the stack on paper.
2. Trace push/pop operations step by step.
3. Identify where the **top** is at every step.
4. Then write the code.

---

# Exercise 1 — Reverse a String

Write a function:

```python
def reverse_string(text):
```

Example:

```text
Input:  "hello"
Output: "olleh"
```

Hint: Push every character. Then pop every character.

Questions:

- What order do characters come out?
- Why does this work?

---

# Exercise 2 — Balanced Parentheses

Write a function:

```python
def is_balanced(expression):
```

Example:

```text
Input:  "({[]})"
Output: True

Input:  "({[})"
Output: False
```

Rules:

- Push opening brackets: `(`, `{`, `[`
- When you see a closing bracket, pop and check if it matches
- If stack is empty at the end → balanced

Questions:

- What happens if you see a closing bracket but the stack is empty?
- What happens if the stack still has items after the loop?

---

# Exercise 3 — Stack Using Two Queues

Skip this for now. Come back after learning Queues.

---

# Exercise 4 — Min Stack

Extend your `Stack` class to support `get_min()` in O(1) time.

```python
class MinStack:
    def push(self, value):   ...
    def pop(self):           ...
    def get_min(self):       ...   # return smallest value
```

Example:

```text
push(5)   → min = 5
push(3)   → min = 3
push(7)   → min = 3
pop()     → min = 3
pop()     → min = 5
```

Hint: Maintain a second stack that tracks the minimums.

Questions:

- When you push a value smaller than the current min, what do you record?
- When you pop a value equal to the current min, what do you do?

---

# Exercise 5 — Evaluate Postfix Expression

Postfix (Reverse Polish Notation):

```text
3 4 +      → 7
5 1 2 + 4 * + 3 - → 14
```

Write:

```python
def evaluate_postfix(expression):
```

Rules:

- If number → push
- If operator → pop two values, compute, push result

Questions:

- Which operand is popped first? (Order matters for `-` and `/`)
- What should the stack contain at the end?

---

# Exercise 6 — Stack Using Array (Fixed Size)

Implement a stack with a fixed-size array:

```python
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1
```

Questions:

- What happens if you push when the stack is full?
- What does `top = -1` mean?

---

# Exercise 7 — Reverse a Stack

Given a stack, reverse it **without using another data structure** (except recursion).

```python
def reverse_stack(stack):
```

Hint: Recursion implicitly uses the call stack.

Questions:

- How does recursion help here?
- What is the base case?

---

# Final Challenge

After finishing, answer these:

1. What does LIFO mean?
2. Why is every stack operation O(1)?
3. Where is the "top" in a Python list-based stack?
4. Where is the "top" in a linked list-based stack?
5. Why can't you access the middle of a stack?
6. Name 3 real-world uses of a stack.
