# String Count

Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method `count`.

**The solution is one line of code.**

# Example input

```
Hello world
```

# Example output

```
2
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
s = input()
print(s.count(" ") + 1)
```

</details>