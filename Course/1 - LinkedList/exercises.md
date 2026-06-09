# Linked List Practice Exercises

## Important

Do **not** search for solutions.

Do **not** ask AI to write the code.

Use only your current `LinkedList` implementation as reference.

Before writing any code:

1. Draw the linked list on paper.
2. Identify where you start (**Head**).
3. Identify how you move (**current_node.next**).
4. Identify when you stop.
5. Then write the code.

### What I Expect From You

I expect mistakes.

I expect some methods to fail the first time.

I expect you to spend time debugging.

That is how data structures are learned.

Do not focus on speed.

Focus on understanding what node you are standing on at every step.

---

# Exercise 1 — Count Even Numbers

Create a method:

`count_even_numbers()`

Example:

```text
10 -> 21 -> 30 -> 45 -> 50 -> None
```

Expected Result:

```text
3
```

Questions:

- How do I visit every node?
- How do I know if a number is even?
- Where should I store the count?

Goal:

Count how many nodes contain an even number.

---

# Exercise 2 — Find the Largest Value

Create a method:

`find_max()`

Example:

```text
10 -> 90 -> 5 -> 40 -> None
```

Expected Result:

```text
90
```

Questions:

- What should happen if the list is empty?
- What value should I start with?
- When should I replace the current maximum?

Goal:

Return the largest value in the linked list.

---

# Exercise 3 — Find the Smallest Value

Create a method:

`find_min()`

Example:

```text
10 -> 90 -> 5 -> 40 -> None
```

Expected Result:

```text
5
```

Questions:

- How is this similar to `find_max()`?
- What changes?

Goal:

Return the smallest value in the linked list.

---

# Exercise 4 — Sum All Values

Create a method:

`sum_values()`

Example:

```text
10 -> 20 -> 30 -> None
```

Expected Result:

```text
60
```

Questions:

- Where should the running total be stored?
- What should the initial value be?

Goal:

Return the total sum of all node values.

---

# Exercise 5 — Count Nodes

Create a method:

`count_nodes()`

Example:

```text
10 -> 20 -> 30 -> None
```

Expected Result:

```text
3
```

Questions:

- How do I know how many nodes I visited?

Goal:

Return the total number of nodes.

---

# Exercise 6 — Get First Value

Create a method:

`get_first()`

Example:

```text
10 -> 20 -> 30 -> None
```

Expected Result:

```text
10
```

Questions:

- Which node already points to the first value?

Goal:

Return the first node's value.

---

# Exercise 7 — Get Last Value

Create a method:

`get_last()`

Example:

```text
10 -> 20 -> 30 -> None
```

Expected Result:

```text
30
```

Questions:

- How do I know I reached the last node?
- What does the last node point to?

Goal:

Return the last node's value.

---

# Exercise 8 — Check If List Is Empty

Create a method:

`is_empty()`

Example:

```text
Head
 ↓
None
```

Expected Result:

```text
True
```

Questions:

- What tells us that a linked list is empty?

Goal:

Return `True` or `False`.

---

# Exercise 9 — Count Occurrences

Create a method:

`count_occurrences(value)`

Example:

```text
10 -> 20 -> 10 -> 30 -> 10 -> None
```

Input:

```text
10
```

Expected Result:

```text
3
```

Questions:

- How do I compare values?
- How do I keep track of matches?

Goal:

Return how many times the value appears.

---

# Exercise 10 — Insert After Value

Create a method:

`insert_after(target_value, new_value)`

Before:

```text
10 -> 20 -> 30 -> None
```

Call:

```text
insert_after(20, 25)
```

After:

```text
10 -> 20 -> 25 -> 30 -> None
```

Questions:

- Which node should receive the new node?
- What happens to the old connection?
- In what order should pointers be updated?

Goal:

Insert the new value after the target value.

---

# Final Challenge

After finishing all exercises, answer these questions without looking at code:

1. What is a node?
2. What is a pointer?
3. What is Head?
4. Why do we use `current_node`?
5. How do we move through a linked list?
6. How do we know we reached the end?
7. Why can't we jump directly to the last node?

If you can answer those questions confidently, you understand the basics of Linked Lists.

---

# When Finished

Send me:

- Your code
- Your outputs
- Which exercise was hardest
- Where your thinking got stuck

Then we will review it together.