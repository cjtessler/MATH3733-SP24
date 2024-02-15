# List Comprehensions

1. Find all of the numbers from 1-1000 that have a 3 in them.

    <details>
    <summary>Solution</summary>

    ```python
    numbers_with_3 = [x for x in range(1, 1001) if '3' in str(x)]
    ```

    </details>

1. Count the number of spaces in a string.

    <details>

    <summary>Solution</summary>

    ```python
    sum(1 for char in s if char == ' ')
    ```

    </details>

1. Remove all of the vowels in a string.

    <details>
    <summary>Solution</summary>

    ```python
    vowels = 'aeiouAEIOU'
    ''.join(char for char in s if char not in vowels)
    ```

    </details>
