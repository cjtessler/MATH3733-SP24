# Quadratic Formula

Given numbers a, b, and c, the quadratic equation can have zero, one, or two real solutions. The quadratic formula can be used to compute the solutions. The expression within the radical is the _discriminant_ associated with the equation.  If the discriminant is positive, the equation has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the equation has no solutions.  

# Instructions

Write a Python function `smaller_root` that takes that takes as input the numbers `a`, `b`  and `c` and returns the smaller solution of the quadratic equation, if one exists. If the equation has no real solution, return `None`.

# Examples

```
>>> smaller_root(1, 5, 4)
-4.0

>>> smaller_root(1, 2, 3)
None

>>> smaller_root(0, -10, 3) # x is not defined if a == 0
None

>>> smaller_root(2, 0, -10)
-2.2360679775
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

```python
import math

def smaller_root(a, b, c):

    disc = b**2 - 4*a*c

    if disc < 0 or a == 0:
        return None

    x = (- b - math.sqrt(disc)) / (2 * a)

    return x
```

</details>