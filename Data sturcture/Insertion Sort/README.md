# Insertion Sort
The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.

The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

## How it works:

Take the first value from the unsorted part of the array.
Move the value into the correct place in the sorted part of the array.
Go through the unsorted part of the array again as many times as there are values.

Continue reading to fully understand the Insertion Sort algorithm and how to implement it yourself.

## Insertion Sort Implementation
To implement the Insertion Sort algorithm in a programming language, we need:

An array with values to sort.
An outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run 
n − 1 times.
An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at 
index i, the sorted part of the array starts at index 0 and ends at index i − 1


## Insertion Sort Improvement
Insertion Sort can be improved a little bit more.

The way the code above first removes a value and then inserts it somewhere else is intuitive. It is how you would do Insertion Sort physically with a hand of cards for example. If low value cards are sorted to the left, you pick up a new unsorted card, and insert it in the correct place between the other already sorted cards.

The problem with this way of programming it is that when removing a value from the array, all elements above must be shifted one index place down:.