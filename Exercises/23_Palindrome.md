# Palindrome

## Instructions

Write a program to check if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

To accomplish this, you should define four functions:

1. `first(word)`: Returns the first character of a string.
2. `middle(word)`: Returns the string after removing the first and last characters.
3. `last(word)`: Returns the last character of a string.
4. `is_palindrome(word)`: Uses the above three functions to determine if `word` is a palindrome. It should return `True` if the word is a palindrome and `False` otherwise.

Your `is_palindrome` function should follow these steps:

- If the string is either empty or a single character, consider it a palindrome (return `True`).
- If the first and last characters do not match, it is not a palindrome (return `False`).
- Recursively check if the middle portion of the string is a palindrome by removing the first and last characters.

Test your program with the following strings and include any additional tests you think are necessary:

```python
is_palindrome("noon")       # Expected output: True
is_palindrome("redivider")  # Expected output: True
is_palindrome("allen")      # Expected output: False
is_palindrome("math")       # Expected output: False
```

Consider edge cases and how your program might behave with different types of input, such as single characters, strings with spaces, or punctuation.

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

```python
def first(word):
    return word[0]

def middle(word):
    return word[1:-1]

def last(word):
    return word[-1]

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

is_palindrome("noon")       # True
is_palindrome("redivider")  # True
is_palindrome("allen")      # False
is_palindrome("math")       # False
```

</details>
