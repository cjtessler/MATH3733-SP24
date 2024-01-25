# Is Even

Write a function `is_even` that takes as input an integer parameter and **returns** `True` if the input is even and `False` otherwise.

## Example

```python
>>> is_even(2)
True
>>> is_even(3)
False
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

</details>
