**Problem 1 - Two Sum**

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

----------------------------------------------------------------------------------------------------------------

**Problem 14 - Longest Common Prefix**

Write a function to find the longest common prefix string amongst an array of strings.

----------------------------------------------------------------------------------------------------------------

**Problem 17 - Letter Combinations of a Phone Number**

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![alt tag](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

Input: Digit string "23"

Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

----------------------------------------------------------------------------------------------------------------

**Problem 94 - Binary Tree Inorder Traversal**

Given a binary tree, return the inorder traversal of its nodes' values.

For example:

Given binary tree [1,null,2,3],

	   1

	    \

	     2

	    /

	   3

return [1,3,2].

----------------------------------------------------------------------------------------------------------------

**Problme 98 - Validate Binary Search Tree**

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.

The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.

Example 1:

	    2

	   / \

	  1   3

Binary tree [2,1,3], return true.

Example 2:

	    1

	   / \

	  2   3

Binary tree [1,2,3], return false.

----------------------------------------------------------------------------------------------------------------

**Problem 140 - Word Break II**

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

----------------------------------------------------------------------------------------------------------------

**Problem 145 - Binary Tree Postorder Traversal**

Given a binary tree, return the postorder traversal of its nodes' values.

For example:

Given binary tree {1,#,2,3},

	   1

	    \

	     2

	    /

	   3


return [3,2,1].

----------------------------------------------------------------------------------------------------------------

**Problem 155 - Min Stack**

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.

pop() -- Removes the element on top of the stack.

top() -- Get the top element.

getMin() -- Retrieve the minimum element in the stack.

----------------------------------------------------------------------------------------------------------------

**Problem 190 - Reverse Bits**

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

----------------------------------------------------------------------------------------------------------------

**Problem 191 - Number of 1 Bits**

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

----------------------------------------------------------------------------------------------------------------

**Problem 222 - Count Complete Tree Nodes**

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

----------------------------------------------------------------------------------------------------------------

**Problem 230 - Kth Smallest Element in a BST**

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

----------------------------------------------------------------------------------------------------------------

**Problem 239 - Sliding Window Maximum**

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,

Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

	Window Position                          Max

	[1  3  -1] -3  5  3  6  7           	  3

	1 [3  -1  -3] 5  3  6  7           	      3

	1  3 [-1  -3  5] 3  6  7           	      5

	1  3  -1 [-3  5  3] 6  7           	      5

	1  3  -1  -3 [5  3  6] 7           	      6

	1  3  -1  -3  5 [3  6  7]          	      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

----------------------------------------------------------------------------------------------------------------

**Problem 279 - Perfect Squares**

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

----------------------------------------------------------------------------------------------------------------

**Problem 338 - Counting Bits**

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].