# Primes

An integer $p$ is prime if $1$ and $p$ are its only divisors. Show that $149$ is a prime number. Use the fact that $p$ is prime if $p$ `%` $n \neq 0$ for all $n \leq \sqrt{p}$.

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

```python
from math import sqrt
>>> sqrt(149) 
12.206555615733702
>>> 149 % 2
1
>>> 149 % 3
2
>>> 149 % 5
4
>>> 149 % 7
2
>>> 149 % 11
6
```
</details>
