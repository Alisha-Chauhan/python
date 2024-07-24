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


## Replace String

The replace() method replaces a string with another string:

## Split String
The split() method returns a list where the text between the specified separator becomes the list items.

The split() method splits the string into substrings if it finds instances of the separator:

# String Concatenation
To concatenate, or combine, two strings you can use the + operator.

# String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

## F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations..

### Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

A placeholder can contain Python code, like math operations: