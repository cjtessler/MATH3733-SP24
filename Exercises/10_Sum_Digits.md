# Digits

Given a number. Find the sum of its digits.

## Example input 1

```text
123
```

## Example output 1

```text
6
```

## Example input 2

```text
13579
```

## Example output 2

```text
25
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
# Read an integer:
a = int(input())

total = 0
while a > 0:
    rem = a % 10
    total += rem
    a= a // 10

print(total)
```

</details>
