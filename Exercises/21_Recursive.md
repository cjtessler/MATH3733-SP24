# Recursive Arithmetic Sequence

An **arithmetic sequence** is a sequence of the form 

`a,  a + b,  a + 2b, a + 3b, ...`

where `a` is the first term, and `b` is the common difference. For example, if `a = 2` and `b=3`, then the sequence is 

`2, 5, 8, 11, ...`

When we sum of terms of an arithmetic sequence, we are finding the **arithmetic series**. Learn more above the arithmetic sequence and series here: [https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html](https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html). 

# Instructions

Write a *recursive* function `f(n, a, b)` to find the sum of the first `n` terms in the arithmetic sequence with first term `a` and common difference `b`.

The problem will be manually checked to ensure a recursive algorithm was used, but be sure that all automated tests pass before submission.

## Example

``` python
>>> f(2, 2, 3)
7
>>> f(5, -5, 5)
25
>>> f(100, 11, 7)
35750
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
def f(n, a, b):
    if n == 0:
        return 0
    else:
        return a + f(n-1, a + b, b)
```

</details>