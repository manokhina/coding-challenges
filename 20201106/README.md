# Problem description

Write a method that receives one integer at a time.  Keep track of these numbers, use the last K entries and perform the following operations:
- Discard the top 20% and bottom 20% of K received integers, in an ordered fashion.
- Return the average of the remaining digits

Input: [10, 20, 30, 40, 1, 5, 3, 75, 99, 33, 66], 
k = 5

k digits = 10, 20, 30, 40, 1

Remove item 1 and 5 (20% of K): 10, 20, 30

Output: 12
