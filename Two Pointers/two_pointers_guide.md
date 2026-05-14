# Two Pointers — Complete Guide

## What is it?

Two pointers is a technique where you use two index variables to traverse a data structure, eliminating the need for nested loops. It reduces time complexity from O(n²) to O(n) in many problems.

> The key insight: instead of checking every possible pair with a nested loop, use the structure of the data (usually sorted order) to move pointers intelligently.

---

## The Three Variants

"Two pointers" is an umbrella term for three distinct patterns. Knowing which one to use is the whole skill.

### Variant 1 — Left / Right (Converging)

Start at opposite ends, move toward each other until they meet.

```
[1,  3,  5,  7,  9]
 L               R     → compare, then move L right or R left
```

### Variant 2 — Slow / Fast (Same Direction)

Both start from the beginning, one moves faster. Used for cycles, middle finding, kth from end.
See the dedicated slow/fast pointer guide for full coverage.

```
[1, 2, 3, 4, 5]
 S  F             → slow moves 1 step, fast moves 2 steps
```

### Variant 3 — Sliding Window (Expanding / Shrinking)

Both move forward; together they define a window. Expand right, shrink left when a condition breaks.

```
[a, b, c, d, e]
    L     R       → window = [b, c, d]
```

---

## When TO Use

### 1. Two Sum on a Sorted Array (Left/Right)

If the sum is too small, move the left pointer right. If too big, move the right pointer left. Guaranteed O(n).

- Key requirement: array must be sorted first
- If unsorted: sort it first (O(n log n)) or use a HashMap instead
- Leetcode: 167 (Two Sum II)

### 2. Container with Most Water (Left/Right)

Start at both ends. Always move the pointer at the shorter height inward — a taller wall can only help, never hurt.

- Classic greedy + two pointers combo
- Leetcode: 11

### 3. Palindrome Check on a String or Array (Left/Right)

Left starts at index 0, right at the last index. Compare and converge.

- O(n) with O(1) space — no need to reverse the string
- Works for both strings and arrays
- Leetcode: 125, 680

### 4. Three Sum / Four Sum (Left/Right Nested)

Fix one element with an outer loop. Run left/right two pointers on the rest for each fixed element.

- Reduces O(n³) brute force to O(n²)
- Sort the array first
- Watch for the "skip duplicates" step to avoid repeating triplets/quadruplets
- Leetcode: 15 (3Sum), 18 (4Sum)

### 5. Longest/Shortest Subarray or Substring (Sliding Window)

Expand right pointer to grow the window. When a constraint breaks, shrink from the left until it's satisfied again.

- Often paired with a HashMap or Set to track window contents
- Common problems:
  - Longest substring without repeating characters (Leetcode 3)
  - Minimum window substring (Leetcode 76)
  - Max consecutive ones with at most k flips (Leetcode 1004)
  - Longest subarray with sum ≤ k

### 6. Remove Duplicates / In-place Operations (Slow/Fast on Array)

One pointer tracks the position to write to, another scans ahead. Modifies the array in-place with O(1) space.

- Leetcode: 26 (Remove Duplicates from Sorted Array), 27 (Remove Element)

---

## When NOT to Use


| Situation                           | Use This Instead                                      |
| ----------------------------------- | ----------------------------------------------------- |
| Unsorted array for two-sum          | HashMap — O(n) without sorting                        |
| Linked list (left/right variant)    | Slow/fast pointers — no random access                 |
| Need every valid pair, not just one | Nested loop — two pointers only finds one efficiently |
| 2D matrix traversal                 | BFS / DFS / binary search per row                     |
| Existence check (does X exist?)     | HashSet — O(1) lookup, simpler                        |
| Non-contiguous subsets              | Dynamic programming or backtracking                   |


---

## Common Mistakes

**Mistake 1 — Using left/right on an unsorted array**
Left/right only works because sorted order guarantees that moving a pointer changes the sum in a predictable direction. On an unsorted array, moving left doesn't mean the sum increases — the logic breaks completely.

**Mistake 2 — Confusing the three variants**
All three are called "two pointers" but solve different problems:

- Converging (left/right) = pair/target problems on sorted data
- Same direction (slow/fast) = cycle, middle, distance on chains
- Sliding window = subarray/substring length or sum problems

**Mistake 3 — Forgetting to skip duplicates in 3Sum/4Sum**
After finding a valid triplet, you must advance both pointers and skip any repeated values, or you'll return duplicate triplets.

**Mistake 4 — Off-by-one on window shrinking**
In sliding window, shrink with `while` not `if` — a single shrink step may not be enough to restore the constraint.

---

## Quick Variant Picker


| Problem shape                                    | Variant                         |
| ------------------------------------------------ | ------------------------------- |
| Sorted array + find pair/triplet with target sum | Left/right converging           |
| Palindrome on string or array                    | Left/right converging           |
| Linked list + cycle / middle / kth from end      | Slow/fast                       |
| Longest or shortest subarray/substring           | Sliding window                  |
| In-place array modification                      | Slow/fast on array              |
| Three sum / four sum                             | Left/right nested inside a loop |


---

## Complexity


| Variant                | Time                | Space                                     |
| ---------------------- | ------------------- | ----------------------------------------- |
| Left/Right (two sum)   | O(n) after sorting  | O(1)                                      |
| Left/Right (three sum) | O(n²) after sorting | O(1)                                      |
| Sliding Window         | O(n)                | O(1) to O(k) depending on window tracking |
| Slow/Fast              | O(n)                | O(1)                                      |


Compared to brute force:

- Two sum brute force: O(n²) → Two pointers: O(n)
- Three sum brute force: O(n³) → Two pointers: O(n²)

---

## LeetCode Problems to Practice


| Problem                                   | Number | Variant                |
| ----------------------------------------- | ------ | ---------------------- |
| Two Sum II (sorted)                       | 167    | Left/right             |
| Container with Most Water                 | 11     | Left/right             |
| Valid Palindrome                          | 125    | Left/right             |
| 3Sum                                      | 15     | Left/right nested      |
| 4Sum                                      | 18     | Left/right nested      |
| Remove Duplicates from Sorted Array       | 26     | Slow/fast on array     |
| Remove Element                            | 27     | Slow/fast on array     |
| Longest Substring Without Repeating Chars | 3      | Sliding window         |
| Minimum Window Substring                  | 76     | Sliding window         |
| Max Consecutive Ones III                  | 1004   | Sliding window         |
| Trapping Rain Water                       | 42     | Left/right             |
| Sort Colors (Dutch Flag)                  | 75     | Three pointers variant |


---

## Relationship to Slow & Fast Pointers

Slow/fast is a sub-pattern of two pointers. The key differences:


|                   | Left/Right                   | Slow/Fast                      |
| ----------------- | ---------------------------- | ------------------------------ |
| Starting position | Opposite ends                | Same start                     |
| Direction         | Converging                   | Same direction                 |
| Speed             | Same speed                   | Different speeds               |
| Best for          | Sorted arrays, pair problems | Linked lists, cycle detection  |
| Data structure    | Arrays, strings              | Linked lists, arrays as chains |


