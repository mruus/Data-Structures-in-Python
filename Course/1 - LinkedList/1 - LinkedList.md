# LINKED LIST — CONCEPT EXPLANATIONS

---

## WHAT IS A LINKED LIST?

A Linked List is a data structure used to store data.

Unlike a Python list:

```python
numbers = [10, 20, 30]
```

where elements are stored **next to each other in memory**,

a Linked List stores data in **separate nodes**.

Each node knows:
1. Its own value
2. Where the next node is located

```
Head
  ↓
10 -> 20 -> 30 -> None
```

**None** means: "There are no more nodes after this one."

**Head:** Points to the first node.

**Tail:** The last node in the list.

```
Head
  ↓
10 -> 20 -> 30 -> None
             ↑
            Tail
```

---

## WHAT IS A NODE?

A node is the building block of a linked list.

Each node contains:
1. `value` — the actual data
2. `next` — pointer to the next node

```
+----------------+
| value = 10     |
| next  = -----> |
+----------------+
```

The `next` pointer stores the **address/reference** of the next node.

---

## SINGLY vs DOUBLY LINKED LIST

### Singly Linked List
```
10 -> 20 -> 30 -> None
```
Each node has **one pointer** (`next`). You can only move forward.

### Doubly Linked List
```
None <- 10 <-> 20 <-> 30 -> None
```
Each node has **two pointers** (`previous` and `next`).

**Advantages:**
- Can move forward
- Can move backward
- More flexible than singly linked list

**Disadvantage:**
- Uses more memory (extra pointer per node)

---

## BIG O NOTATION

**O** means "Order Of Growth" — it describes how an algorithm grows as the amount of data increases.

| Notation | Name | Meaning |
|---|---|---|
| O(1) | Constant Time | Always one operation. Speed stays the same regardless of data size. |
| O(n) | Linear Time | Must visit every node. Time grows proportionally with data. |
| O(n²) | Quadratic Time | For every node, loop through every node again. |

### O(1) — Constant Time
Example: **Insert at beginning.**

Doesn't matter if the list has 10 nodes or 1,000,000 nodes — speed remains nearly the same.

### O(n) — Linear Time
Example: **Search.**

- 10 nodes → may check 10 nodes
- 1000 nodes → may check 1000 nodes

### O(n²) — Quadratic Time
Not common for basic linked list operations.

100 nodes → 100 × 100 = 10,000 operations.

---

## COMPLETE COMPLEXITY TABLE

| Operation | Complexity |
|---|---|
| Insert at beginning | O(1) |
| Insert at end | O(n) |
| Search | O(n) |
| Delete first | O(1) |
| Delete last | O(n) |
| Delete by value | O(n) |
| Traverse | O(n) |
| Find length | O(n) |
| Reverse | O(n) |
| Access by index | O(n) |
