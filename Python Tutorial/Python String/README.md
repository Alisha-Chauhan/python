# strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:


## Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:


# Multiline Strings
You can assign a multiline string to a variable by using three quotes:

 Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.


# Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

# String Length
To get the length of a string, use the len() function.

# Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
## Use it in an if statement:

# Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
## Use it in an if statement:


# Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

## Slice From the Start
By leaving out the start index, the range will start at the first character:

## Slice To the End
By leaving out the end index, the range will go to the end:

## Negative Indexing
Use negative indexes to start the slice from the end of the string:

# strings modify 
### Upper Case
The upper() method returns the string in upper case:

### lower case
The lower() method returns the string in lower case:

### Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.