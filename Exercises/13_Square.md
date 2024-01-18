# Square

## Nested Loops

Our next step is to build a square. To do this with the restriction of using only `print("#", end="")` and `print()`, we will need **nested loops**:

```python
for i in range(3):
    for j in range(3):
        print("i: ", i)
        print("j: ", j)
        print()
```

Step through this code one line at a time and observe that values  `i` and `j` take on and in which order. For each `i`, the value of `j` iterates from 0 to 3. You can step through the code at [https://goo.gl/sUZ9X8](https://goo.gl/sUZ9X8).

## Instructions

Write a program that uses only two output statements, `print("#", end="")` and `print()` to produce a pattern of hash symbols shaped like a perfect 5x5 square:

## Expected Output

```text
#####
#####
#####
#####
#####
```
