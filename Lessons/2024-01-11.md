# Day 01

## Outline

- Set Up the Learning Environment
- Syllabus
- Computing
- Python Basics
  - Operators
  - Variables

## Set Up the Learning Environment

- Sign up for GitHub
- Explain GitHub
- Visit [www.github.com/codespaces](www.github.com/codespaces)
- Set up blank codespace
- Create a lesson folder
- Create an exercise folder
- Change folder settings (optional)
- Create hello.py
- Install Python extension
- Adjust font size


## What is a "computer"?

- The machine in front of you is a *modern* computer.
- A computer is one who computes.
- You are a computer!
- By today’s standards, you are a slow computer with bad memory… but necessary to design and implement modern computers.
- We need tools to aid in our computation as we move into the future

## What does a computer do?

- Performs calculations
- Remembers calculations
- What a human tells it to do

> “What I mean is that if you really want to understand something, the best way is to try and explain it to someone else. That forces you to sort it out in your own mind... And that’s really the essence of programming. By the time you’ve sorted out a complicated idea into little steps that even a stupid machine can deal with, you’ve certainly learned something about it yourself.”
> ― Douglas Adams, Dirk Gently's Holistic Detective Agency

## Terminology

**Computation** is any type of calculation that includes both arithmetical and non-arithmetical steps and which follows a well-defined model (e.g. an **algorithm**).

A **program** is a sequence of instructions that specify how to perform a computation.

## REPL

A **Read-Eval-Print Loop (REPL)**, also known as an interactive shell, is a simple, interactive computer programming environment that takes single user inputs (READ) (i.e. single expressions), EVALUATES them, and returns (PRINTS) the result to the user; a program written in a REPL environment is executed piecewise.

## Arithmetic Operators

[Official Python Docs: 3.10 Using Python as a Calculator](https://docs.python.org/3.10/tutorial/introduction.html#using-python-as-a-calculator)

Arithmetic operators follow the standard order of operation.

- `()` : parentheses
- `**` : exponentiation
- `+` : addition
- `-` : subtraction
- `*` : multiplication
- `/` : division
- `//` : floor division (quotient)
- `%` : modulus (remainder)

## calculator (interactive)

``` python
>>> 3 + 3
6
>>> (3 + 6) ** 2
81
>>> 5 / 2
2.5
>>> 100 / 50 - 1
1.0
>>> 7 // 3
2
>>> 7 % 3
1
>>> quit() # quits the interactive terminal
```

## Types

We can use the `type` function to determine the data type of its input.

```python
>>> type(3)
<class 'int'>
>>> type(3.0)
<class 'float'>
>>> type(8 / 3)
<class 'float'>
>>> type(8 // 3)
<class 'int'>
>>> type("hello")
<class 'str'>
```

## Comments

We can write **comments** in our programs. Our programs will eventually get to be very, very long. Commenting is a way for you to leave "notes" for yourself or other programmers so that you (and/or others) understand what your thinking process was when you originally wrote your program.

Python supports comments via the `#` symbol. You can use the `#` symbol to tell Python to essentially ignore anything else on that line which comes after the symbol. Here are some examples:

``` python
print('Hello, world!')  # this will print the string Hello World!

# the following line will print the string My Name
print('My Name')
```

## Exercise 1: Python as a Calculator

Write a mathematical expression in a `print` function that satisfies the comments.

```python
# Example
# How many seconds are there in 2 minutes, 42 seconds?
print(2 * 60 + 42) # this will print 162

# Exercise 1
# How many seconds are there in 2 hours, 42 minutes, 42 seconds?
print(2 * 60 * 60 + 42 * 60 + 32) 

# Exercise 2
# Write an expression that simplifies to 42.0 and 
# uses the exponentiation, addition, subtraction, 
# multiplication, and division operators.
print(((((100 / 10) - 10) + 42) ** 0) * 42 )     
```

A small program is sometimes referred to as a *script*.

## variables.py

A **variable** is a name that refers to an object.

The `=` is the assignment operator.

Notice that variable names can be more than single letters.

```python
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
```

The `print()` function can take more than one argument.  It concatenates the strings. [2. Built-in Functions — Python 3.10 documentation](https://docs.python.org/3.10/library/functions.html#print)

## Rules for variables

No spaces. Use underscore in place of a space

- ❌ `my var` is not valid
- ✅ `my_var` is valid

The first character of a variable name must be a letter or the underscore character.

- ❌`4var` is invalid
- ✅ `_message` is valid

No characters are allowed in a variable name besides alphanumeric (alphabet or numeric) characters and the underscore ("_") character (no special characters like &, !, +, $, etc.)

- ❌`you&i` is invalid
- ✅ `you_and_i` is valid

Python is case sensitive, so two variables with the same name but different case are two different variables.

- `name`, `NAME`, and `Name` are all different variables

❌ You *cannot* use any of Python's built in "reserved words” or **keywords**.

``` python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

⚠️ Do **not** create a variable named `print` because that would conflict with the pre-defined `print` function, and overwrite the default functionality of `print`.

```python
>>> print("hello")
hello
>>> print = 42
>>> print("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```
## Exercises

Complete [exercises](../../exercises.md) 1 though 4.
