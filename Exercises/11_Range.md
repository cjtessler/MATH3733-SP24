# `Range`

This exercise will expose you to the other uses of the `range` function.

The range function behaves in one of two ways:

- `range`(_stop_)
- `range`(_start_, _stop_[, _step_])

Any arguments in brackets [] are optional. Type and run the following code:

```python
for i in range(0, 5, 1):
    print(i, end=" ")
print() # adds new lines for next for loop
```

Now, change the `range`'s arguments to each of the following and observe the output:

```
range(0, 10, 2)

range(2, 10, 3)

range(0, 5)

range(100, 75, -2)

range(75, 100, -2)
```

Notice that i takes on the values beginning at _start_, but strictly less than _stop_.

Now, using the `range` function, print the sequence `2, 5, 8`, a new line, and then the sequence `20, 15, 10, 5, 0 , -5`.


## Expected Output

```
2 5 8

20 15 10 5 0 -5
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
for i in range(2, 9, 3):
    print(i, end=" ")
print()
for i in range(20, -6, -5):
    print(i, end=" ")
print()
```

</details>