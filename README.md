# 🧠 Problem Solving — LeetCode Solutions in Python

A personal collection of **262 LeetCode solutions** written in Python, organized by **data structure / algorithm topic** and **difficulty level**. Each file corresponds to one LeetCode problem, identified by its problem number in the first comment line. Many files contain multiple approaches — the initial personal attempt followed by cleaner, more optimal solutions — with time and space complexity noted inline.

---

## 📋 Table of Contents

- [Repository Overview](#-repository-overview)
- [Structure](#-structure)
- [Problem Count by Category](#-problem-count-by-category)
- [All Problems](#-all-problems)
  - [Arrays & Strings](#-arrays--strings)
  - [Sliding Window & Two Pointers](#-sliding-window--two-pointers)
  - [Hash Tables](#-hash-tables)
  - [Linked Lists](#-linked-lists)
  - [Stacks & Queues](#-stacks--queues)
  - [Trees](#-trees)
  - [Graphs](#-graphs)
  - [Searching (Binary Search)](#-searching-binary-search)
  - [Dynamic Programming](#-dynamic-programming)
  - [Greedy](#-greedy)
  - [Recursive Backtracking](#-recursive-backtracking)
  - [Heaps](#-heaps)
  - [Bit Manipulation](#-bit-manipulation)
- [Code Style & Conventions](#-code-style--conventions)
- [How to Run](#-how-to-run)

---

## 📖 Repository Overview

- **Language:** Python
- **Platform:** LeetCode
- **Total Solutions:** 262 files
- **Topics Covered:** 13 categories
- **Difficulty Levels:** Easy · Medium · Hard
- **Style:** Each file includes the problem number, a primary solution, and often 1–2 alternative approaches with complexity analysis

---

## 📁 Structure

```
Problem Solving/
├── Arrays & Strings/
│   ├── easyLevel/
│   ├── mediumLevel/
│   └── hardLevel/
├── sliding window & two pointers/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Hash Tables/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Linked Lists/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Stacks & Queues/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Trees/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Graghs/               ← (folder named "Graghs" in repo)
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Searching/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── DP/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Greedy/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Recursive Backtracking/
│   ├── easy/
│   ├── meduim/           ← (folder named "meduim" in repo)
│   └── hard/
├── Heaps/
│   ├── easy/
│   ├── medium/
│   └── hard/
└── Bit Manipulation/
    ├── easy/
    ├── medium/
    └── hard/
```

Each `.py` file follows this pattern:

```python
# <LeetCode problem number>
# my solution ->
#   Time : O(...)
#   Space: O(...)

class Solution(object):
    def methodName(self, ...):
        ...

# another solution / a better solution ->
class Solution(object):
    ...
```

---

## 📊 Problem Count by Category

| Category | Easy | Medium | Hard | Total |
|---|---|---|---|---|
| Arrays & Strings | 29 | 25 | 2 | **56** |
| Sliding Window & Two Pointers | 8 | 17 | 3 | **28** |
| Hash Tables | 17 | 10 | 0 | **27** |
| Trees | 14 | 10 | 2 | **26** |
| Dynamic Programming | 5 | 17 | 3 | **25** |
| Linked Lists | 8 | 10 | 1 | **19** |
| Graphs | 3 | 14 | 2 | **19** |
| Searching | 6 | 9 | 0 | **15** |
| Stacks & Queues | 3 | 7 | 2 | **12** |
| Bit Manipulation | 8 | 2 | 0 | **10** |
| Greedy | 4 | 5 | 1 | **10** |
| Heaps | 1 | 4 | 2 | **7** |
| Recursive Backtracking | 0 | 7 | 0 | **7** |
| **Total** | **106** | **137** | **18** | **262** |

---

## 📝 All Problems

### 🔢 Arrays & Strings

**Easy (29)**

| Problem | LeetCode # |
|---|---|
| 1299 (Replace Elements with Greatest Element on Right) | 1299 |
| 1450 (Number of Students Doing Homework at a Given Time) | 1450 |
| 1984 (Minimum Difference Between Highest and Lowest of K Scores) | 1984 |
| Array Partition | 561 |
| Backspace String Compare | 844 |
| Best Time to Buy and Sell Stock | 121 |
| Construct the Rectangle | 492 |
| Find Closest Number to Zero | 2239 |
| Find Numbers Disappeared in Array | 448 |
| Find Pivot Index | 724 |
| Find the Index of the First Occurrence | 28 |
| Is Subsequence | 392 |
| Longest Common Prefix | 14 |
| Max Score After Splitting a String | 1422 |
| Merge Sorted Array | 88 |
| Merge Strings Alternately | 1768 |
| Missing Number | 268 |
| Move Zeroes | 283 |
| Number of Lines to Write String | 806 |
| Plus One | 66 |
| Range Sum Query | 303 |
| Reformat Date | 1507 |
| Remove Duplicates from Sorted Array | 26 |
| Remove Element | 27 |
| Reverse String II | 541 |
| Roman to Integer | 13 |
| Squares of a Sorted Array | 977 |
| Summary Ranges | 228 |
| Unique Email Addresses | 929 |

**Medium (25)**

| Problem | LeetCode # |
|---|---|
| Best Time to Buy and Sell Stock II | 122 |
| Find the Duplicate Number | 287 |
| H-Index | 274 |
| Insert Delete GetRandom O(1) | 380 |
| Insert Interval | 57 |
| Max Distance to Closest Person | 849 |
| Maximum Length of Pair Chain | 646 |
| Maximum Product Subarray | 152 |
| Maximum Subarray (Kadane's) | 53 |
| Merge Intervals | 56 |
| Minimum Number of Arrows to Burst Balloons | 452 |
| Non-Overlapping Intervals | 435 |
| Product of Array Except Self | 238 |
| Remove Duplicates from Sorted Array II | 80 |
| Reverse Integer | 7 |
| Reverse Words in a String | 151 |
| Rotate Array | 189 |
| Rotate Image | 48 |
| Set Matrix Zeroes | 73 |
| Sort Colors | 75 |
| Spiral Matrix | 54 |
| String Compression | 443 |
| Sum of Even Numbers After Queries | 985 |
| The Kth Factor of n | 1492 |
| Zigzag Conversion | 6 |

**Hard (2)**

| Problem | LeetCode # |
|---|---|
| First Missing Positive | 41 |
| Text Justification | 68 |

---

### 🪟 Sliding Window & Two Pointers

**Easy (8)**

| Problem | LeetCode # |
|---|---|
| 2379 (Maximum Total Importance of Roads) | 2379 |
| Assign Cookies | 455 |
| Maximum Average Subarray I | 643 |
| Remove Duplicates from Sorted Array | 26 |
| Remove Elements | 27 |
| Reverse String | 344 |
| Sort Array By Parity | 905 |
| Squares of Sorted Arrays | 977 |

**Medium (17)**

| Problem | LeetCode # |
|---|---|
| 3Sum | 15 |
| 3Sum Closest | 16 |
| 4Sum | 18 |
| Container With Most Water | 11 |
| Longest Repeating Character Replacement | 424 |
| Longest Substring Without Repeating Characters | 3 |
| Longest Subarray of 1's After Deleting One Element | 1493 |
| Max Consecutive Ones III | 1004 |
| Max Number of K-Sum Pairs | 1679 |
| Maximum Number of Vowels in a Substring | 1456 |
| Maximum Points You Can Obtain from Cards | 1423 |
| Maximum Sum Circular Subarray | 918 |
| Minimum Operations to Reduce X to Zero | 1658 |
| Minimum Size Subarray Sum | 209 |
| Permutation in String | 567 |
| Two Sum II | 167 |
| Valid Palindrome | 125 |

**Hard (3)**

| Problem | LeetCode # |
|---|---|
| Minimum Window Substring | 76 |
| Substring with Concatenation of All Words | 30 |
| Trapping Rain Water | 42 |

---

### 🗂️ Hash Tables

**Easy (17)**

| Problem | LeetCode # |
|---|---|
| 1160 (Find Words That Can Be Formed by Characters) | 1160 |
| Contains Duplicate | 217 |
| Contains Duplicate II | 219 |
| Distribute Candies | 575 |
| Find Common Characters | 1002 |
| Happy Number | 202 |
| Isomorphic Strings | 205 |
| Jewels and Stones | 771 |
| Majority Element | 169 |
| Maximum Number of Balloons | 1189 |
| Number of Good Pairs | 1512 |
| Relative Sort Array | 1122 |
| Robot Return to Origin | 657 |
| Two Sum | 1 |
| Unique Number of Occurrences | 1207 |
| Valid Anagram | 242 |
| Word Pattern | 290 |

**Medium (10)**

| Problem | LeetCode # |
|---|---|
| Contiguous Array | 525 |
| Custom Sort String | 791 |
| Equal Row and Column Pairs | 2352 |
| Group Anagrams | 49 |
| Integer to Roman | 12 |
| Longest Consecutive Sequence | 128 |
| Optimal Partition of a String | 2405 |
| Ransom Note | 383 |
| Subarray Sum Equals K | 560 |
| Valid Sudoku | 36 |

---

### 🔗 Linked Lists

**Easy (8)**

| Problem | LeetCode # |
|---|---|
| 1290 (Convert Binary Number in a Linked List to Integer) | 1290 |
| Intersection of Two Linked Lists | 160 |
| Linked List Cycle | 141 |
| Merge Two Sorted Lists | 21 |
| Middle of the Linked List | 876 |
| Remove Duplicates from Sorted List | 83 |
| Remove Linked List Elements | 203 |
| Reverse Linked List | 206 |

**Medium (10)**

| Problem | LeetCode # |
|---|---|
| Add Two Numbers | 2 |
| Copy List with Random Pointer | 138 |
| Delete the Middle Node of a Linked List | 2095 |
| Insert Greatest Common Divisors in Linked List | 2807 |
| Maximum Twin Sum of a Linked List | 2130 |
| Remove Nth Node From End of List | 19 |
| Reorder List | 143 |
| Reverse Linked List II | 92 |
| Rotate List | 61 |
| Swap Nodes in Pairs | 24 |

**Hard (1)**

| Problem | LeetCode # |
|---|---|
| Reverse Nodes in K-Group | 25 |

---

### 📚 Stacks & Queues

**Easy (3)**

| Problem | LeetCode # |
|---|---|
| Baseball Game | 682 |
| Next Greater Element I | 496 |
| Valid Parentheses | 20 |

**Medium (7)**

| Problem | LeetCode # |
|---|---|
| Basic Calculator II | 227 |
| Daily Temperatures | 739 |
| Evaluate Reverse Polish Notation | 150 |
| Longest Substring Without Repeating Characters | 3 |
| Min Stack | 155 |
| Monotonic Array | 896 |
| Next Greater Element II | 503 |
| Simplify Path | 71 |

**Hard (2)**

| Problem | LeetCode # |
|---|---|
| Basic Calculator | 224 |
| Largest Rectangle in Histogram | 84 |

---

### 🌳 Trees

**Easy (14)**

| Problem | LeetCode # |
|---|---|
| Balanced Binary Tree | 110 |
| Binary Tree Paths | 257 |
| Count Complete Tree Nodes | 222 |
| Diameter of Binary Tree | 543 |
| Invert Binary Tree | 226 |
| Kth Smallest Element in a BST | 230 |
| Leaf-Similar Trees | 872 |
| LCA of a Binary Search Tree | 235 |
| Maximum Depth of Binary Tree | 104 |
| Minimum Absolute Difference in BST | 530 |
| Minimum Depth of Binary Tree | 111 |
| Path Sum | 112 |
| Same Tree | 100 |
| Search in a Binary Search Tree | 700 |
| Symmetric Tree | 101 |

**Medium (10)**

| Problem | LeetCode # |
|---|---|
| Add and Search Word (Trie) | 211 |
| Binary Tree Level Order Traversal | 102 |
| Binary Tree Right Side View | 199 |
| Construct Binary Tree from Preorder and Inorder | 105 |
| Count Good Nodes in Binary Tree | 1448 |
| Implement Trie (Prefix Tree) | 208 |
| Maximum Binary Tree | 654 |
| Subtree of Another Tree | 572 |
| Validate Binary Search Tree | 98 |

**Hard (2)**

| Problem | LeetCode # |
|---|---|
| Binary Tree Maximum Path Sum | 124 |
| Serialize and Deserialize Binary Tree | 297 |

---

### 🗺️ Graphs

**Easy (3)**

| Problem | LeetCode # |
|---|---|
| Find if Path Exists in a Graph | 1971 |
| Find the Town Judge | 997 |
| Island Perimeter | 463 |

**Medium (14)**

| Problem | LeetCode # |
|---|---|
| Clone Graph | 133 |
| Course Schedule | 207 |
| Course Schedule II | 210 |
| Game of Life | 289 |
| Keys and Rooms | 841 |
| Max Area of Island | 695 |
| Min Cost to Connect All Points | 1584 |
| Nearest Exit from Entrance in Maze | 1926 |
| Network Delay Time | 743 |
| Number of Islands | 200 |
| Pacific Atlantic Water Flow | 417 |
| Rotten Oranges | 994 |
| Shortest Bridge | 934 |
| Word Search | 79 |

**Hard (2)**

| Problem | LeetCode # |
|---|---|
| Find Edges in Shortest Paths | 3123 |
| Longest Increasing Path in a Matrix | 329 |

---

### 🔍 Searching (Binary Search)

**Easy (6)**

| Problem | LeetCode # |
|---|---|
| Binary Search | 704 |
| First Bad Version | 278 |
| Guess Number Higher or Lower | 374 |
| Perfect Squares | 279 |
| Search Insert Position | 35 |
| Sqrt(x) | 69 |

**Medium (9)**

| Problem | LeetCode # |
|---|---|
| Find Minimum in Rotated Sorted Array | 153 |
| Find Peak Element | 162 |
| Find the Smallest Divisor Given a Threshold | 1283 |
| Find First and Last Position of Element | 34 |
| Koko Eating Bananas | 875 |
| Search a 2D Matrix | 74 |
| Search a 2D Matrix II | 240 |
| Search in Rotated Sorted Array | 33 |
| Successful Pairs of Spells and Potions | 2300 |

---

### 💡 Dynamic Programming

**Easy (5)**

| Problem | LeetCode # |
|---|---|
| Climbing Stairs | 70 |
| Min Cost Climbing Stairs | 746 |
| N-th Tribonacci Number | 1137 |
| Pascal's Triangle | 118 |
| Valid Palindrome II | 680 |

**Medium (17)**

| Problem | LeetCode # |
|---|---|
| Coin Change | 322 |
| Decode Ways | 91 |
| House Robber | 198 |
| House Robber II | 213 |
| Jump Game | 55 |
| Longest Common Subsequence | 1143 |
| Longest Increasing Subsequence | 300 |
| Longest Palindromic Substring | 5 |
| Maximum Subarray | 53 |
| Minimum Falling Path Sum | 931 |
| Minimum Path Sum | 64 |
| Palindromic Substrings | 647 |
| Triangle | 120 |
| Unique Paths | 62 |
| Unique Paths II | 63 |
| Valid Parenthesis String | 678 |
| Word Break | 139 |

**Hard (3)**

| Problem | LeetCode # |
|---|---|
| Regular Expression Matching | 10 |
| Wildcard Matching | 44 |
| Word Search II | 212 |

---

### 💰 Greedy

**Easy (4)**

| Problem | LeetCode # |
|---|---|
| Can Place Flowers | 605 |
| Lemonade Change | 860 |
| Maximum Nesting Depth of Parentheses | 1614 |
| Maximum Odd Binary Number | 2946 |

**Medium (5)**

| Problem | LeetCode # |
|---|---|
| Gas Station | 134 |
| Jump Game | 55 |
| Jump Game II | 45 |
| Rabbits in Forest | 781 |
| Valid Parenthesis String | 678 |

**Hard (1)**

| Problem | LeetCode # |
|---|---|
| Candy | 135 |

---

### 🔁 Recursive Backtracking

**Medium (7)**

| Problem | LeetCode # |
|---|---|
| Combination Sum | 39 |
| Combinations | 77 |
| Generate Parentheses | 22 |
| Letter Combinations of a Phone Number | 17 |
| Permutations | 46 |
| Subsets | 78 |
| Sum of All Subset XOR Totals | 1863 |

---

### 🏔️ Heaps

**Easy (1)**

| Problem | LeetCode # |
|---|---|
| Last Stone Weight | 1046 |
| Second Largest Digit in a String | 1796 |

**Medium (4)**

| Problem | LeetCode # |
|---|---|
| Find K Pairs with Smallest Sums | 373 |
| K Closest Points to Origin | 973 |
| Kth Largest Element in an Array | 215 |
| Top K Frequent Elements | 347 |

**Hard (2)**

| Problem | LeetCode # |
|---|---|
| Find Median from Data Stream | 295 |
| Merge K Sorted Lists | 23 |

---

### ⚙️ Bit Manipulation

**Easy (8)**

| Problem | LeetCode # |
|---|---|
| Add Binary | 67 |
| Base 7 | 504 |
| Counting Bits | 338 |
| Hamming Distance | 461 |
| Number of 1 Bits | 191 |
| Power of Two | 231 |
| Reverse Bits | 190 |
| Single Number | 136 |

**Medium (2)**

| Problem | LeetCode # |
|---|---|
| Factorial Trailing Zeroes | 172 |
| Single Number II | 137 |

---

## 🖋️ Code Style & Conventions

Every solution file follows a consistent format:

**Problem number in first comment line:**
```python
# 70
```

**Author's initial attempt labeled clearly:**
```python
# my solution ->
#   Time : O(n)
#   Space: O(1)
```

**Alternative approaches when available:**
```python
# another solution ->
# a better solution ->
# a wide better solution ->
# AI solution ->         ← marks solutions studied/referenced externally
# I solved it later after explanation ->   ← honest notes on difficulty
```

**All solutions use `class Solution(object):`** following LeetCode's Python 2-style class convention.

**Complexity annotations** appear either as comments at the top of the solution or at the bottom, e.g.:
```python
# Time: O(n * m)
# Space: O(n * m)
```

Multiple approaches in the same file demonstrate progression — from the first working solution to the most efficient one, making it easy to understand the thought process behind each optimization.

---

## ▶️ How to Run

Each file is standalone and can be run directly with Python:

```bash
python "Arrays & Strings/easyLevel/Two Sum.py"
```

Or open in VS Code and run with the Python extension. No external dependencies are required — all solutions use only Python's standard library (`collections`, `heapq`, `math`, etc.).

To run a specific solution, instantiate the `Solution` class and call the method:

```python
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

---

## 📈 Progress Summary

| Difficulty | Count | Percentage |
|---|---|---|
| Easy | 106 | 40% |
| Medium | 137 | 52% |
| Hard | 18 | 7% |
| **Total** | **262** | **100%** |

Topics with the most depth: **Arrays & Strings** (56), **Sliding Window & Two Pointers** (28), **Hash Tables** (27), **Trees** (26), **Dynamic Programming** (25).

---

*Solutions written in Python · LeetCode Problem Solving Collection*
