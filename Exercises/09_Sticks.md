# Sticks

You are given three sticks, you may or not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle:

> If any of the three lengths is greater than the sum of the other two then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a *“degenerate”* triangle.)

Write a program that prompts the user to input three stick lengths, converts them to integers, and determines if it is possible to form a triangle with the given lengths. Print the boolean `True` if it is possible, and `False` if it is not.

The user may enter non-negative numbers. It is **not** possible to form a triangle if one of the side lengths is zero. Your program should account for this case.

## Example input 1

### Input

```text
1
2
3
```

### Output

```text
True
```

Consider the cases:

- 3 is less than or equal to 1+2
- 2 is less than or equal to 1+3
- 1 is less than or equal to 2+3

## Example input 2

### Input

```text
1
2
6
```

### Output

```text
False
```
6 is greater than 1+2