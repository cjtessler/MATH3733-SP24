# Parity

Write a program that takes an integer input and prints "even" if the input is even or "odd" if the input is odd.

You may assume the valid input is provided, i.e., you are not expected to guard against non-integer inputs.

## Example input

``` python
2
```

## Example output

``` python
even
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
n = int(input())

if n % 2 == 0:
    print("even")
else:
    print("odd")
```

</details>
