# Fibonacci Numbers
The Fibonacci numbers are very useful for introducing algorithms, so before we continue, here is a short introduction to Fibonacci numbers.

The Fibonacci numbers are named after a 13th century Italian mathematician known as Fibonacci.

The two first Fibonacci numbers are 0 and 1, and the next Fibonacci number is always the sum of the two previous numbers, so we get 0, 1, 1, 2, 3, 5, 8, 13, 21, ...


# How it works:

Start with the two first Fibonacci numbers 0 and 1.
Add the two previous numbers together to create a new Fibonacci number.
Update the value of the two previous numbers.
Do point a and b above 18 times.



# To show the difference between loops and recursion, we will implement solutions to find Fibonacci numbers in three different ways:

An implementation of the Fibonacci algorithm above using a for loop.
An implementation of the Fibonacci algorithm above using recursion.
Finding the nth Fibonacci number using recursion.

# 1. Implementation Using a For Loop

"""It can be a good idea to list what the code must contain or do before programming it:

Two variables to hold the previous two Fibonacci numbers
A for loop that runs 18 times
Create new Fibonacci numbers by adding the two previous ones
Print the new Fibonacci number
Update the variables that hold the previous two fibonacci numbers"""


# 2. Implementation Using Recursion

""" Recursion is when a function calls itself. 
To implement fibonacci algorithm we needs most of the same things as in the code example above, but we need to 
replace the for loop with recursion. To replace the for loop with recursion, we need encapsulate much of the code
 in function, and we need the function call itself to create a new fibonacci number as long as the produced number of fibonacci number
 or equal to 19."""

# 3. Finding The nth Fibonacci Number Using Recursion

"""To find the nth Fibonacci number we can write code based on the mathematic formula for Fibonacci number 
n: F(n) = F(n−1) + F(n−2)
This just means that for example the 10th Fibonacci number is the sum of the 9th and 8th Fibonacci numbers."""

 When using this concept with recursion, we can let the function call itself as long as n is less than, or equal to, 1. If 
 n ≤ 1
 it means that the code execution has reached one of the first two Fibonacci numbers 1 or 0.
