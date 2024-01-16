# Debugging

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




```python
print("Hello World"
# SyntaxError: unexpected EOF while parsing
# EOF means "End of file"
# The Python interpreter was expecting the closing )
```


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


