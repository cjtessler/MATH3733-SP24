# Line

## Problem Reduction

The next three exercises demonstrate the idea of **problem reduction**. When we encounter more complex problems, we want to be able to reduce such problems into simple subproblems. Our goal will be to write a program that uses only two output statements, `print("#", end="")` and `print()` to produce a hash of symbols shaped like a sideways triangle:

```text
#
##
###
####
###
##
#
```

It would be easier to start with half of a square: 

``` text
#####
####
###
##
#
```

This reduces all the way down to understanding how to print a line.

## Instructions

Write a program that uses only two output statements, `print("#", end="")` and `print()` to produce a line of five hash symbols.

You will need to use iteration, e.g., a `for` loop.


## Desired output

```text
#####
```
