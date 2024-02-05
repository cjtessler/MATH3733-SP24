# String Find Methods

Read about the `find` string method: [https://www.w3schools.com/python/ref_string_find.asp](https://www.w3schools.com/python/ref_string_find.asp)

Read about the `rfind` string method: [https://www.w3schools.com/python/ref_string_rfind.asp](https://www.w3schools.com/python/ref_string_rfind.asp)

Given a string that may contain a letter **p**. Print the index of the second occurrence of **p**. If the letter **p** occurs only once, then print `-1`, and if the string does not contain the letter **p**, then print `-2.`

# Example input #1

```
appropriate
```

# Example output #1

```
2
```

# Example input #2

```
spare
```

# Example output #2

```
-1
```

# Example input #3

```
reason
```

# Example output #3

```
-2
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
# Read a string:
s = input()

first_occurence = s.find("p")
last_occurence = s.rfind("p")

if first_occurence == -1:
    print(-2)
elif first_occurence == last_occurence:
    print(-1)
else:
    print(s.find("p", first_occurence+1))
```

</details>