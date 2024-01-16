# Day 02

## Plan

- Debugging
- Variables (review)
- Strings
- Data Types
- Input
- Booleans
- Conditionals
- Project 1 Overview

## Debugging

Demonstrate `print(“hello world”)` in interactive mode.

``` python
>>> print(“hello world!”)
hello world
```

- `print(arguments)`  is a function
- We *call* a function and it performs actions
- “Hello world” is a string (data type)
- Let’s break the program. Below are a few examples.

``` python
>>> print("Hello World"
... )
# It is expecting the closing parentheses 

>>> print("Hello World)
# SyntaxError: EOL while scanning string literal
# EOL mean "End of line"
# The Python interpreter was looking for the end of string, the closing "

>>> prin("Hello world")
# NameError: name 'prin' is not defined
# "prin" is not a defined function
# We will learn how to define our own functions in the future
        
>>> print(hello world)
# SyntaxError: invalid syntax

>>> print("Hello World!")
# IndentationError: unexpected indent
# Python use whitespace to determine "blocks" of code
# More on this later
```

- An error in a program is known as a “bug”.
- [The First Computer Bug Ever Found! | Technology Facts - Glitch Facts - YouTube](https://www.youtube.com/watch?v=84VmwdGwYMA)
- The process of fixing fixing bugs is known as **debugging**.
- Read the error messages!

```python
print("Hello World"
# SyntaxError: unexpected EOF while parsing
# EOF means "End of file"
# The Python interpreter was expecting the closing )
```

## variables

A **variable** is a name that refers to an object.

The `=` is the assignment operator.

Notice that variable names can be more than single letters.

```python
# variables.py

# "comments" are preceded by a hash character
# Used to to clarify code and are not interpreted by Python
"# This is not a comment because it's inside quotes." 
# It is a string

msg = "Hello variables"
print(msg)

# variables should be descriptive
message = "My message"
print(message)

# variable referring to numbers
print(7)
my_number = 1
print(my_number)

your_number = 14
our_number = my_number + your_number
print(our_number)

# print function with multiple arguments
first_name = "John"
last_name = "Smith"
print(first_name, last_name)

# variables can be reassigned
first_name = "Sally"
print("first_name has been changed")
print(first_name, last_name)

# print function with sep argument
print("Today's date is")
print(1, 11, 2024, sep='/')
print() # adds an extra line

# f-strings are convenient for string interpolation
print("My first name is ", first_name, ", and my last name is ", last_name)
print(f"My name is {first_name} and my last name is {last_name}")
```

The `print()` function can take more than one argument.  It concatenates the strings. [2. Built-in Functions — Python 3.10 documentation](https://docs.python.org/3.10/library/functions.html#print)

## Exercise: Area of a Circle

Write a program to compute the radius of a circle. There will be three variables `pi`, `radius`, and `area`. Choose an appropriate value for `pi`, a value of your choice for `radius`, and then `area` should be computed appropriately. Print the area.

``` python
pi = 3.14
radius = 10
area = pi * (radius ** 2)
print(area)
```

## Strings

- A **character** is a letter, special character, space, or digit.
- A **string** is a sequence of characters.

``` python
# strings.py

# Strings are surrounded by either double or single quotes
"hello world"
'hello world'

# String operations
mystic_creature = "dragon"
annoying_bug = "fly"

# Adding strings "concatenates" the strings
print(mystic_creature + annoying_bug) # dragonfly

# Multiplying a string repeats the string
print(annoying_bug * 3) # flyflyfly

# Common mistake: Don't use quotes with variables
print("annoying_bug" * 3) #annoying_bugannoying_bugannoying_bug
```

## Data Types

A **value** is a basic object that programs work with. We can use the `type()` function to determine the type of a value.

```python
>>> type(2) 
<class 'int'>

>>> type(42.0) 
<class 'float'>

>>> type('Hello, World!') 
<class 'str'>

>>> # Data Type Conversion ("casting")
>>> price = "1.99"
>>> type(price)
<class 'str'>
>>> real_price = float(price)
>>> type(real_price)
<class 'float'>

>>> float_to_int = int(real_price)
>>> float_to_int
1
```

An appropriate data type can be cast to another data using the following functions:

- `int()`
- `float()`
- `str()`

## input

```python
# input.py

# input() is a function that gets input from the user
# input() takes one argument, a string, which is the prompt
# input() returns a string

name = input("What is your name? ")
print("Hello, " + name + "!")

age = input("How old are you? ")
print(f"You are {age} years old.")

# This will not work
# older_age = age + 1
# print(older_age)

older_age = int(age) + 1
print(f"You will be {older_age} years old next year.")

# You don't need to create a new variable to store the result
older_age = age + 1
print(f"In two years, you will be {older_age}")

# += is the addition assignment operator
older_age += 1 
print(f"In three years, you will be {older_age}")
```

To exit a program waiting for input, press `Ctrl + C` (Windows) or `Cmd + C` (macOS).

### ⚠️ Don't use `input` as a variable

```python
>>> input = input("Enter your name: ")  # input is a function here
Enter your name: Cody
>>> input
'Cody'
>>> input = input("Change your name: ")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    input = input("Change your name: ")
TypeError: 'str' object is not callable
```

## Exercise

Write a program to compute the area of a circle. There will be three variables `pi`, `radius`, and `area`. Choose an appropriate value for `pi``, ask the user for radius, and then area should be computed appropriately. Print the area.

```python
pi = 3.14
radius = int(input("Enter a value for the radius: "))
area = pi * (radius ** 2)
print(area)
```

## Boolean Expressions

A **boolean expression** is an expression that is either `True` or `False`.

The double equal sign `==` is the comparison operator.

```python
>>> 5 == 5
True
>>> 5 == 6
False
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> bool(0)
False
>>> bool(1)
True
>>> bool("hello")
True
>>> bool(None)
False
>>> bool(42)
True
```

## Comparison Operators

```python
>>> x = 5
>>> y = 6
>>> 
>>> # == is the comparison operator
>>> #  = is the assignment operator
>>>
>>> print(x == y)
False
>>> print(x != y)   # not equal
True
>>> print (x > y)
False
>>> print(x < y)
True
>>> print(x <= y)
True
>>> print(x >= y)
False
>>> 
>>> ## String Comparisons
>>> s1 = "abb"
>>> s2 = "abc"
>>> 
>>> print(s1 == s2)
False
>>> print(s1 < s2)
True
>>> print(s2 > s1)
True
>>> # String comparison is done by lexicographic ordering
>>> 
>>> # strings and ints cannot be compared
>>> print("a" > 5)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("a" > 5)
TypeError: '>' not supported between instances of 'str' and 'int'
```

## Logical Operators

```python
>>> not True
False
>>> not False
True
>>> True and True
True
>>> True and False
False
>>> True or True
True
>>> True or False
True
```

Let `a` and `b` be variable names with Boolean values.

| **a** | **b** | **not a** | **a and b** | **a or b** |
| ----- | ----- | ----- | ----- | ----- |
| True  | True  | False | True  | True  |
| True  | False |       | False | True  |
| False | True  | True  | False | True  |
| False | False |       | False | False |

## Control Flow / Branching

```python
# branch.py

x = int(input("Can I have a value for x? "))
# Consider 5, -1, 0

if x > 0:
    print("x is positive")
```

Let's also introduce the `elif` and `else statements`.

```python
# branch.py

x = int(input("Can I have a value for x? "))

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is neither positive nor negative!")
```

## abc.py

```python
# abc.py

print("Can I have an a, b, or c?")
letter = input("> ")

if letter == a or letter == b or letter == c:
    print("Thanks for the letter!")
else:
    print(f"I didn't want a {letter}...")
```

## Exercises

Complete exercises 5 through 9.
