# Day 03

## Plan

- Booleans
- Conditionals

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
