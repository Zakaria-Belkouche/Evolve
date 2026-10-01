# Algorithmic Thinking

## Contents
---
- [Roadmap](#roadmap)
	- [Phase 1: Core patterns](#phase-1-core-patterns)
	- [Phase 2: Data structures and traversal](#phase-2-data-structures-and-traversal)
	- [Phase 3: Advanced problem solving](#phase-3-advanced-problem-solving)
	- [Phase 4: Later topics](#phase-4-later-topics)
- [Learning Loop](#learning-loop)
---
- [Phase 1:](#phase-1)
    - [Arrays and Strings](#arrays-and-strings)

## Roadmap

### Phase 1: Core patterns

Build comfort with these before moving on:

1. **Arrays and strings:** indexing, iteration, state, prefix/suffix ideas, edge cases.
2. **Hash maps and sets:** fast lookup, frequency counts, stored indexes, duplicate detection.
3. **Two pointers:** left/right and slow/fast pointers; especially useful with sorted arrays.
4. **Sliding window:** fixed and dynamic windows for substring and subarray problems.
5. **Sorting:** understand Bubble, Selection and Insertion Sort; then focus on Merge Sort and Quick Sort.
6. **Binary search:** classic search, boundary search and sorted-array problems.

### Phase 2: Data structures and traversal

1. **Stacks and queues:** LIFO/FIFO, parentheses; monotonic stacks later.
2. **Linked lists:** nodes, traversal, reversal, cycle detection.
3. **Recursion:** base and recursive cases, call stack.
4. **Trees:** binary trees, BSTs, preorder/inorder/postorder traversals.
5. **DFS and BFS:** recursion or stack for DFS, queue for BFS; tree and grid traversal.

### Phase 3: Advanced problem solving

1. **Graphs:** adjacency lists, visited sets, connected components, cycle detection.
2. **Backtracking:** subsets, permutations, combinations, decision trees.
3. **Dynamic programming:** start with Climbing Stairs and House Robber; then Coin Change, Unique Paths, Longest Common Subsequence and Edit Distance.
4. **Heaps / priority queues:** top K, kth largest, repeated minimum/maximum extraction.

### Phase 4: Later topics

No need to focus on these yet:

- Greedy algorithms; topological sort; Union-Find; Dijkstra.
- Minimum spanning trees (Prim and Kruskal); tries; bit manipulation; advanced DP.
- Specialised structures: Segment Trees and Fenwick Trees.

## Learning Loop

For each pattern:

1. Learn the idea and when it is useful.
2. Study one simple example.
3. Solve 2–3 Easy problems, then one Medium problem.
4. Explain the solution in your own words.
5. Revisit it a few days later, then aim for 3–5 problems per pattern and review again after a week without notes.

Avoid random problem grinding. Learn the **pattern**, not a memorised solution. For example, two pointers are useful when moving one pointer can safely eliminate part of the candidate space; the goal is to recognise when that reasoning applies to a new problem.

## Reflection After Each Problem

- What pattern did I use, and why did it work?
- What are the time and space complexities?
- What clue in the problem could point me toward this approach?

---

# Phase 1:

## Arrays and Strings

Arrays (often Python lists) and strings are ordered sequences. Their elements can be accessed by index.

- Loop through values to inspect or compare them.
- Track simple information as you go, such as a count or maximum.
- Watch index boundaries; valid indexes go from `0` to `len(sequence) - 1`.
- A single pass through `n` elements is usually `O(n)`.

```python
nums = [5, 8, 12, 3]

for index in range(len(nums)):
	print(index, nums[index])
```

### LeetCode Problems

- [x] **[Running Sum of 1d Array](LeetCode-Solutions/running-sum.py)** — *Easy*
        - AI assistance: None; completed in 5 minutes.
        - Runtime: _Not recorded_
        - Memory: _Not recorded_
        - Notes: _Add notes here_
- [x] **[Richest Customer Wealth](LeetCode-Solutions/richest-customer.py)** — *Easy*
        - AI assistance: None; completed in 3 minutes.
        - Runtime: _Not recorded_
        - Memory: _Not recorded_
        - Notes: _Add notes here_
- [x] **[Merge Strings Alternately](LeetCode-Solutions/merge-strings-alternately.py)** — *Easy*
        - AI assistance: None; completed in 25 minutes.
        - Runtime: Beats 5.7% of submissions.
        - Memory: Beats 58.33% of submissions.
        - Notes: strings are immutable in Python so concatenation creates a new string each time. Using a list to collect characters and joining at the end is more efficient then generating a new string each time.
- [x] **[Find Pivot Index](LeetCode-Solutions/find-pivot-index.py)** — *Easy*
        - AI assistance: None; completed in 15 minutes.
        - Runtime: Beats 7.87% of submissions.
        - Memory: Beats 48.43% of submissions.
        - Notes: when doing sum(nums[0:i]) and sum(nums[i+1:]), the slicing creates new lists each time. So the initial for loop is O(n). Both sum's combine to also mean I'm iterating over the entire list again for each index. So n * n = O(n^2). Can optimise.
- [x] **[Summary Ranges](LeetCode-Solutions/summary-ranges.py)** — *Easy*
        - AI assistance: None
        - Runtime: Beats 100% of submissions.
        - Memory: Beats 65.4% of submissions.
        - Notes: Actually very proud of myself. My first solution was correct and beat 100% of runtime submissions, however the memory usage was terrible comparatively. I managed to then optimise the memory usage to beat the majority of submissions. Great.
- [x] **[Longest Common Prefix](LeetCode-Solutions/longest-common-prefix.py)** — *Easy*
        - AI assistance: No Ai assistance; completed in ~ 35 minutes.
        - Runtime: Beats 100% of submissions.
        - Memory: Beats 33% of submissions.
        - Notes: Quite happy with this although memory usage could be better.
- [ ] **[Best Time to Buy and Sell Stock](LeetCode-Solutions/best-time-to-buy-and-sell-stock.py)** — *Easy*
        - AI assistance: _Not recorded_
        - Runtime: _Not recorded_
        - Memory: _Not recorded_
        - Notes: Finding more difficult.
- [x] **[Valid Palindrome](LeetCode-Solutions/valid-palindrome.py)** — *Easy*
        - AI assistance: None. Completed in about 5 minutes... 
        - Runtime: Beats 36.3% of submissions.
        - Memory: Beats 5.8% of submissions.
        - Notes: Considering the time it took me to complete this problem... Very happy.
- [ ] **[Plus One](LeetCode-Solutions/plus-one.py)** — *Easy*
        - AI assistance: _Not recorded_
        - Runtime: _Not recorded_
        - Memory: _Not recorded_
        - Notes: _Add notes here_
- [ ] **[Rotate Array](LeetCode-Solutions/rotate-array.py)** — *Medium*
        - AI assistance: _Not recorded_
        - Runtime: _Not recorded_
        - Memory: _Not recorded_
        - Notes: _Add notes here_
- [ ] **[Product of Array Except Self](LeetCode-Solutions/product-of-array-except-self.py)** — *Medium*
        - AI assistance: _Not recorded_
        - Runtime: _Not recorded_
        - Memory: _Not recorded_
        - Notes: _Add notes here_

