# Power

## Instructions

Write a recursive function named `is_power` that takes two integers, `a` and `b`, as arguments. The function should return `True` if `a` is a power of `b`, and `False` otherwise. For the purposes of this exercise, any number to the power of 0 is considered 1, and 1 is considered a power of every number.

Here are some specific conditions your function should consider:

1. If `a` is 1, the function should return `True` because any number to the power of 0 is 1.
2. If `a` is divisible by `b` and recursively, `a/b` is a power of `b`, then the function should return `True`.
3. In all other cases, the function should return `False`.

Please handle edge cases where the inputs might not be standard positive integers.

To validate your function, test it with the following cases and include any other tests you find necessary:

```python
print(is_power(4, 2))       # Expected output: True, because 2^2 is 4
print(is_power(65536, 4))   # Expected output: True, because 4^8 is 65536
print(is_power(0, 10))      # Handle this edge case appropriately
print(is_power(10, 2))      # Expected output: False, because 10 is not a power of 2
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

```python
def is_power(a,b):
    if a == 1:
        return True
    elif a % b == 0 and is_power(a / b, b):
        return True
    else:
        return False
```

</details>