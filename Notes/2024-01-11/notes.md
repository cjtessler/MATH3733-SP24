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

## Review Syllabus

- It is fine to use ChatGPT or other generative AI tools on the programming exercises. In fact, I encourage you to use it to evaluate your solution and generate similar exercises.

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

## Guessing Game

``` text
I am thinking of a number! Try to guess it.
> 10
Too low! Guess again.
> 100
Too high! Guess again.
> -100
Too low! Guess again
> 95
That's it! Would you like to play again? (yes/no)
```

Main Ideas

- *variables* to store numbers
- Control flow
  - *conditionals* or *branching* to test guess
  - repetition (*looping*)
- input/output
- Data Types
  - numbers (*int*s, *float*s, etc)
  - words (*strings*)
- *functions* encapsulate repeated behavior
- `random` module

We will eventually build this, take care of errors, and improve game play.

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
print()

# Exercise 2
# Write an expression that simplifies to 42.0 and 
# uses the exponentiation, addition, subtraction, 
# multiplication, and division operators.
print()     
```

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

>>>   print("Hello World!")
# IndentationError: unexpected indent
# Python use whitespace to determine "blocks" of code
# More on this later
```

- An error in a program is known as a “bug”.
- [The First Computer Bug Ever Found! | Technology Facts - Glitch Facts - YouTube](https://www.youtube.com/watch?v=84VmwdGwYMA)
- The process of fixing fixing bugs is known as **debugging**.
- Read the error messages!

## hello_variables.py

A small program is sometimes referred to as a *script*.

```python
print("Hello World"
# SyntaxError: unexpected EOF while parsing
# EOF means "End of file"
# The Python interpreter was expecting the closing )
```

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
first_name = "Cody"
last_name = "Tessler"
print(first_name, last_name)

# variables can be reassigned
first_name = "Hayley"
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

⚠️ Do **not** create a variable named `print` because that would conflict with the pre-defined `print` function. More on **namespace** later.

## Exercise 2: Area of a Circle

Write a program to compute the radius of a circle. There will be three variables `pi`, `radius`, and `area`. Choose an appropriate value for `pi`, a value of your choice for `radius`, and then `area` should be computed appropriately. Print the area.

``` python
pi = 3.14
radius = 10
area = pi * (radius ** 2)
print(area)
```

## Exercises

**Exercise 1: More on `print()`**

Run the following commands and observe the output.

``` python
print('Single Quotes')
```

``` python
print("Double Quotes")
```

``` python
print('''Triples Quotes are extra
    helpful because they allow a string
    to span multiple lines. Don't forget
    to try this with 'single quotes' and
    "double" quotes.''')
```

``` python
print("Why can't I use single quotes here?")
# Be sure to answer the question as well
```

Now write a program that generates the following output:

``` text
Hello, I'm happy you decided to run this "Python" program!
```

**Exercise 2: Primes** An integer $p$ is prime if $1$ and $p$ are its only divisors. Show that $149$ is a prime number. Use the fact that $p$ is prime if $p$ `%` $n \neq 0$ for all $n \leq \sqrt{p}$.

**Exercise 3: Fermat's Theorem on the sum of two squares** Fermat's Two Squares Theorem states every prime number $p$ of the form $4k+1$ can be expressed as the some of two squares. For example $5 = 2^2 + 1^1$.

Show that $149$ is of the form $4k+1$ and find numbers $a$ and $b$ such that $a^2 + b^2 = 149$.

**Exercise 4: Reading on variables** Read the article [https://realpython.com/python-variables/](https://realpython.com/python-variables/) and answer the following questions.

- How do you assign multiple variables on the same line to the same value?
- What is met by the statement, "A Python variable is a symbolic name that is a reference or pointer to an object."?
- Is `n_a_m_E` a valid variable name?
- What is the difference between Camel, Pascal, and Snake case?

**Exercise 5: Area and Perimeter of a square** Write a program to compute the area and perimeter of a rectangle and print the values. Use appropriately named variables.
