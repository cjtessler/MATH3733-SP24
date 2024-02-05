# Day 7: Recursion

## Recursion

The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34,...

How can a program compute this sequence?

`fib(1) == 1` and `fib(2) == 1` are the base cases, and the next numbers are the sum of the previous two.

Recursion is the process of repeating items in a self-similar way.

![https://res.cloudinary.com/practicaldev/image/fetch/s--KA7Ky3uR--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/226xc0p9pgtgadnin92j.jpeg](https://res.cloudinary.com/practicaldev/image/fetch/s--KA7Ky3uR--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/226xc0p9pgtgadnin92j.jpeg)

## What is recursion?

Algorithmically, we design solutions to problem by **divide-and-conquer**. That is, reduce a problem to simpler versions of the same problem.

Semantically, we write a function that calls itself.

- We want to avoid infinite recursion
  - We must have one or more base cases that are easy to solve.
  - We must solve the same problem on some other input with the goal of simplifying the larger problem input.


## Iterative Algorithms

Looping constructs such as `while` and `for` loops lead to iterative algorithms.

Capture computation is a set of **state variables** can update on each iteration of the loop.

## Multiplication - Iterative

`a` is added to itself `b` times: `a*b = a + a + a + ... + a + a`

``` python
def iterative_multiply(a, b):
    result = 0          # state variable
    while b > 0:        # iteration
        result += a     # current value of computation, a running sum
        b -= 1          # current value of iteration variable
    return result
```

## Multiplication - Recursive

Recursive step: How to reduce problem to a simpler/small version of the same problem.

`a * b = a + (a + a + ... + a) = a + [a * (b - 1)]`

The brackets show the recursive reduction.

Base case: Keep reducing the problem until a we reach a simple case that can be solved directly.

If `b = 1`, then `a * b = a`.

``` python
def recursive_multiply(a, b):
    if b == 1:      # base case
        return a
    else:
        return a + mult(a, b-1)
```

## Factorial

`n! = n * (n-1) * (n-2) * ... * 2 * 1`

``` python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

Observe **call stack** on Python Tutor.

## Observation

Each recursive call to a function creates its own scope.

Flow of control passes back to previous scope once a function call returns the value.

## Recursion with Multiple Base Cases (Fibonacci)

Base cases: `fib(1) == 1` and `fib(2) == 1`
Recursive case: `fib(n) = fib(n-1) + fib(n-1)`

``` python
# Inefficient Fibonacci
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-1)

print(fib(10))
print(fib(34))  # 11,405,774 recursive calls to the function
```

Correctness follows from mathematical induction.

How can this computation's efficiency be improved?

[Fibonacci Visualization 6:25 - 11:00](https://youtu.be/oBt53YbR9Kk?t=384)

The time complexity is $2^n$ (exponential).

Notice that there is repeated computations. The algorithm can "remember" computations by using a technique known as **memoization**.

More on time complexity and memoization later.

## Exercises

Complete exercises 20 though 21.
