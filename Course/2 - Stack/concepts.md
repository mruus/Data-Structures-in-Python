# STACK — CONCEPT EXPLANATIONS

---

## WHAT IS A STACK?

A Stack is a linear data structure that follows the **LIFO** principle:

**L**ast **I**n, **F**irst **O**ut.

Think of a stack of plates:

```
  ┌───┐
  │ 3 │  ← top (last plate added)
  ├───┤
  │ 2 │
  ├───┤
  │ 1 │  ← bottom (first plate added)
  └───┘
```

- You can only add/remove from the **top**.
- The last plate you put on is the first one you take off.

---

## REAL-WORLD ANALOGIES

| Analogy | Push | Pop | Peek |
|---|---|---|---|
| Stack of plates | Place a plate on top | Remove the top plate | Look at top plate |
| Browser history | Visit new page | Go back | Current page |
| Undo (Ctrl+Z) | Record action | Undo last action | — |
| Function calls | Call a function | Return from function | — |

---

## CORE OPERATIONS

| Operation | Description | Example |
|---|---|---|
| `push(value)` | Add to top | `push(5)` → `[5]` |
| `pop()` | Remove & return top | `pop()` → `5` |
| `peek()` | Return top without removing | `peek()` → `5` |
| `is_empty()` | Check if stack is empty | `is_empty()` → `True`/`False` |
| `size()` | Return number of items | `size()` → `3` |

---

## VISUAL EXAMPLE

Start with an empty stack:

```
[]
```

Push `10`:

```
[10]
 ↑
top
```

Push `20`:

```
[10, 20]
      ↑
     top
```

Push `30`:

```
[10, 20, 30]
          ↑
         top
```

Pop:

```
Returns: 30
Stack: [10, 20]
```

Pop:

```
Returns: 20
Stack: [10]
```

Pop:

```
Returns: 10
Stack: []
```

---

## STACK vs LINKED LIST

| | Stack | Linked List |
|---|---|---|
| Access | Only top | Any node (via traversal) |
| Insert | Only top (push) | Beginning, end, middle |
| Remove | Only top (pop) | Any node |
| Principle | LIFO | — |
| Use case | Undo, backtracking | Dynamic storage |

---

## IMPLEMENTATION APPROACHES

### Using a Python List

```python
stack = []
stack.append(10)   # push
stack.pop()        # pop (returns 10)
```

Built-in. Simple. But good for learning the concept.

### Using a Linked List

Push = insert at head. Pop = delete head.

Both are O(1).

### Using a Fixed Array

Pre-allocate memory. Track a `top` index.

---

## BIG O — ALL OPERATIONS ARE O(1)

| Operation | Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| is_empty | O(1) |
| Size | O(1) |

Stacks are efficient because you only ever touch the top.

---

## COMMON USE CASES

1. **Undo / Redo** — every action is pushed; undo pops.
2. **Browser back button** — pages visited are pushed; back pops.
3. **Expression evaluation** — `(3 + 5) * 2` uses stacks for operators.
4. **Balanced parentheses** — `{[()]}` — push opening brackets, pop when closing matches.
5. **Function call stack** — when `a()` calls `b()` calls `c()`, each call is pushed on the stack.
6. **DFS (Depth First Search)** — uses a stack (explicitly or via recursion).
7. **Reversing** — push all items, then pop all → reversed order.

---

## KEY RULE

> You can only interact with the **top**.
> No peeking at the middle.
> No removing from the bottom.
