# String Slices

First, copy the following starter code into your python file. Then read the instructions.


```python
# Read a string:
s = input()

# 1. In the first line, print the third character of this string.
print()

# 2. In the second line, print the second to last character of this string.
print()

# 3. In the third line, print the first five characters of this string.
print()

# 4. In the fourth line, print all but the last two characters of this string.
print()

# 5. In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
print()

# 6. In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
print()

# 7. In the seventh line, print all the characters of the string in reverse order.
print()

# 8. In the eighth line, print every second character of the string in reverse order, starting from the last one.
print()

# 9. In the ninth line, print the length of the given string.
print()
```

# Instructions

You are given a string. Complete the input to the `print()` function that satisfies the directions in the above comment.

Here is a review of Python string slicing: [https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)

# Example input

```
Abrakadabra
```

# Example output

```
r
r
Abrak
Abrakadab
Arkdba
baaar
arbadakarbA
abdkrA
11
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
# Read a string:
s = input()

# 1. In the first line, print the third character of this string.
print(s[2])

# 2. In the second line, print the second to last character of this string.
print(s[-2])

# 3. In the third line, print the first five characters of this string.
print(s[:5])

# 4. In the fourth line, print all but the last two characters of this string.
print(s[:-2])

# 5. In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
print(s[0::2])

# 6. In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
print(s[1::2])

# 7. In the seventh line, print all the characters of the string in reverse order.
print(s[::-1])

# 8. In the eighth line, print every second character of the string in reverse order, starting from the last one.
print(s[::-2])

# 9. In the ninth line, print the length of the given string.
print(len(s))
```

</details>