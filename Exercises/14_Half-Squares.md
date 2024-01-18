# Half-Squares

## Dummy variable `_`

Consider the following loop, which was typed in a REPL environment:

```python
>>> for i in range(3):
...     print("hello")
...
hello
hello
hello
```

Notice that `i` was never used, and the string `hello` was printed three times. Since the variable is not necessary, we can use the dummy variable `_`:

```python
>>> for _ in range(3):
...     print("hello")
...
hello
hello
hello
```

The advantage to this is that it keeps the "namespace" from being cluttered. For example, in a large problem, if `i` is used before the `for` loop to store an important value, the usage of `i` again in the `for` loop will overwrite the original value.

## Algebraic Expression in `range`

Notice that the input to the range function may contain an algebraic expression.

```python
>>> x = 2
>>> for _ in range(x+1):
...     print("hello")
...
hello
hello
hello
```

## Instructions

Ask the use for input `n`. 
Write a program that uses only two output statements, `print("#", end="")` and `print()` to produce pattern of hash symbols shaped like half of a perfect `n x n` square (or a right triangle):

## Test 1 (`n=5`)

```text
#####
####
###
##
#
```

## Test 2 (`n=10`)

```text
##########
#########
########
#######
######
#####
####
###
##
#
```

## Test 3 (`n=1`)

```text
#
```

