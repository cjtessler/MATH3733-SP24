# Apples

N students take K apples and distribute them among each other evenly. The remaining (the indivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for the questions above.  

## Example input

```text
6
50
```

## Example output

```text
8
2
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
N = int(input())
K = int(input())

print(K // N)
print(K % N)
```

</details>