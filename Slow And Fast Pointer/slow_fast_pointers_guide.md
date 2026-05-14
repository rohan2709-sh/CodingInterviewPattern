# Slow & Fast Pointers — Complete Guide

## What is it?

Two pointers moving through a structure at different speeds — one slow (moves 1 step), one fast (moves 2 steps). Their relative positions reveal structure that a single pointer can't see.

```
slow: 1 step at a time → node.next
fast: 2 steps at a time → node.next.next
```

---

## The Real Rule (not just "use on linked lists")

> Use slow & fast pointers when the problem involves **following a chain of connections** and you suspect a **cycle, midpoint, or distance** is involved.

The data structure matters less than the problem shape. It works on linked lists naturally, and on arrays when values act as the next index (like a virtual linked list).

---

## When TO Use

### 1. Cycle Detection in a Linked List
If fast and slow ever point to the same node, a cycle exists. If fast reaches null, no cycle. This is Floyd's Algorithm.

Also works for:
- Finding the start of the cycle
- Finding the length of the cycle

### 2. Find the Middle of a Linked List
When fast reaches the end, slow is exactly at the middle. No need to count the length first.

Also good for:
- Splitting a list in half for merge sort

### 3. Check if a Linked List is a Palindrome
- Step 1: use slow/fast to find the middle
- Step 2: reverse the second half
- Step 3: compare both halves

Note: this modifies the list. If that's not allowed, use a stack instead.

### 4. Find the Kth Node from the End
Move fast pointer K steps ahead first. Then move both at the same speed. When fast hits null, slow is at the Kth node from the end.

Used in: Remove Nth node from end of list (Leetcode 19)

### 5. Find a Duplicate in an Array (No Extra Space)
When array values act as "next pointers" (values in range 1..n in an n+1 array), the duplicate creates a cycle. Floyd's algorithm finds it in O(n) time, O(1) space.

Classic problem: Leetcode 287 — Find the Duplicate Number.

Key constraint: array values must be usable as indices.

---

## When NOT to Use

| Situation | Use This Instead |
|---|---|
| Array/string with random access (arr[i]) | Simple loop or index math |
| Sorted array — find pair that sums to target | Left/right two pointers |
| Subarray or substring problems | Sliding window |
| Doubly linked list or tree traversal | BFS / DFS / parent pointers |
| Space is not a constraint | HashSet (simpler and more readable) |

---

## Common Misconception

Slow/fast pointers are often confused with two other "two pointer" patterns:

**Left/Right Two Pointers** — both start at opposite ends and move toward each other. Used for sorted arrays (two-sum, three-sum, container with most water). Completely different problem shape.

**Sliding Window** — two pointers both move forward but define a window boundary. Used for subarrays, substrings. Not the same as slow/fast.

All three are called "two pointers" but solve different problems. The key differentiator for slow/fast is the **speed difference** and the **chain-following** nature of the traversal.

---

## Quick Decision Checklist

- [ ] Am I traversing a singly linked list, or an array where values act as indices?
- [ ] Does the problem involve a cycle, a midpoint, or a distance from the end?
- [ ] Do I need O(1) space?

If all three are yes → slow & fast pointers are the right tool.

---

## Complexity

| | Time | Space |
|---|---|---|
| Slow & Fast Pointer | O(n) | O(1) |
| HashSet cycle check | O(n) | O(n) |

The slow/fast pattern is valuable precisely because it gives you O(n) time with O(1) space — no extra memory needed.

---

## LeetCode Problems to Practice

| Problem | Number | What it tests |
|---|---|---|
| Linked List Cycle | 141 | Basic cycle detection |
| Linked List Cycle II | 142 | Find cycle start |
| Middle of the Linked List | 876 | Find middle |
| Palindrome Linked List | 234 | Middle + reverse + compare |
| Remove Nth Node from End | 19 | Kth from end |
| Find the Duplicate Number | 287 | Array as linked list + cycle |
| Happy Number | 202 | Cycle detection on numbers |
