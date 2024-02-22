# Day 12: Memoization and Passing by Assignment

## Memoization

Let's revisit the Fibonacci sequence.

[Fibonacci Visualization 6:25 - 11:00](https://youtu.be/oBt53YbR9Kk?start=384)

Discuss how many leaves there are at level *n*.

``` python
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

memo = {
    1: 1, 
    2: 1
}

def fib_memo(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]


from time import time
n = 35

start = time()
print(fib(n))
end = time()
print(f"fib({n}) took {end-start} seconds")         # 3.393 seconds

start = time()
print(memo_fib(n, memo))
end = time()
print(f"memo_fib({n}) took {end-start} seconds")    # 0.000038 seconds
```

[Fibonacci Memoized Tree](https://youtu.be/oBt53YbR9Kk?t=1913)

The following definition of `fib_memo` does not require the declaration of a `memo` with the base cases pre-initialized.

``` python
def fib_memo(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]
```

## Passing by Assignment

Values can be passed to function either "by value" or "by reference" depending on the data type. Immutable data types are passed by value, whereas mutable data types are passed by reference. Here is a summary of various data types in Python:

| Data Type    | Built-in Class      | Mutable |
|--------------|---------------------|---------|
| Numbers      | int, float, complex | ❌       |
| Strings      | str                 | ❌       |
| Tuples       | tuple               | ❌       |
| Bytes        | bytes               | ❌       |
| Booleans     | bool                | ❌       |
| Frozen sets  | frozenset           | ❌       |
| Lists        | list                | ✅       |
| Dictionaries | dict                | ✅       |
| Sets         | set                 | ✅       |
| Byte arrays  | bytearray           | ✅       |

Let's look at an example to understand the difference between passing by value and passing by reference.

```python
def func(x: int, y: list) -> None:
    x = x + 1
    y.pop()

if __name__ == "__main__":
    i = 1
    lst = ['a', 'b']

    func(i, lst)

    print(i, lst)   # 1 ['a']
```

If you pass an copy of the list using the `copy` method of `[:]` syntax, then the list will not change.

```python
def func(x: int, y: list) -> None:
    x = x + 1
    y.pop()

if __name__ == "__main__":
    i = 1
    lst = ['a', 'b']

    func(i, lst[:])

    print(i, lst)   # 1 ['a', 'b']
```

## Operator: `is`

The `is` keyword is used to check if variables are referencing the same object.

```text
>>> l = ['a', 'b', 'c']
>>> m = l
>>> n = l.copy()
>>> m == l
True
>>> n == l
True
>>> l
['a', 'b', 'c']
>>> m
['a', 'b', 'c']
>>> n
['a', 'b', 'c']
>>> l is m
True
>>> m is l
True
>>> n is l
False
>>> l.pop()
'c'
>>> l
['a', 'b']
>>> m
['a', 'b']
>>> n
['a', 'b', 'c']
>>> id(l)
4303458176
>>> id(m)
4303458176
>>> id(n)
4303478912
```

Recommended Reading: [Python's Mutable vs Immutable Types: What's the Difference?](https://realpython.com/python-mutable-vs-immutable-types/) on Real Python