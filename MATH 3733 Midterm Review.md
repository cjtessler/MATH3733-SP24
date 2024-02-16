# MATH 3733 Mathematical Computing Midterm Review

The exam will be closed-note and paper-based. The following problems provide examples of the problems you could encounter on the midterm.

## Fill-in

**Evaluate the expressions and note the data type of the result.**

| Expression                | Evaluates to... | Data Type |
| ------------------------- | --------------- | --------- |
| `5 - 2`                   |                 |           |
| `5 ** 2`                  |                 |           |
| `'5' + '2'`               |                 |           |
| `'5' * 2`                 |                 |           |
| `5 / 2`                   |                 |           |
| `5 // 2`                  |                 |           |
| `5 % 2`                   |                 |           |
| `5 + 2.0`                 |                 |           |
| `5.0 * 2.0`               |                 |           |
| `10 > 2`                  |                 |           |
| `2 < 1`                   |                 |           |
| `ord('A') == ord('a')`    |                 |           |
| `2 != 4`                  |                 |           |
| `5 > 2 and 10 > 11`       |                 |           |
| `5 < 2 or not(10 > 11)`   |                 |           |
| `'hello'[2]`              |                 |           |
| `len('hello')`            |                 |           |
| `len('cat' + 'dog')`      |                 |           |
| `not('False' and 1)`      |                 |           |
| `'!!help!!'.strip('!')`   |                 |           |

## Short Answer

1. Explain what a Boolean expression is and why you would use one while programming. Give three different examples of a Boolean expression being used.

2. Identify three functions that convert data from one data type to another. Provide a practical example of each function and describe when you would use it in an actual program.

3. Name and describe three different data types in Python and when they could be used in a program.

4. Design a problem that requires iteration. Write a solution to the problem using a `for` loop and using a `while` loop.

5. Describe two different ways to stop the following `while` loop from iterating:

   ```python
   keepgoing = 'yes'
   while keepgoing == 'yes':
       # statements go here
   ```

6. Consider the list `[-100, -4, 0, 1, 8, 9, 11, 20, 21, 24, 30, 45, 99, 100, 101]`, and the number `100`. How many steps would it take to find the number, and what numbers would be encountered doing a bisection for the number?

7. What is the difference between local and global scope? Give an example.

8. What is memoization?

## Trace the Output

**State the output for the following programs.**

``` python
for x in range(5):
    print(x)
print()
    
for p in range(1,10):
    print(p)
print()
    
for q in range(100,50,-10):
    print(q)
```

``` python
def fun1():
    print("hi!")

def fun2():
    print("bye!")

if 10 < 5 or 5 > 6:
    fun1()
    fun2()
else:
    fun2()
    fun1()
```

``` python
def fun(a):
    print("a =", a)

for x in range(5):
    fun(x)
```

``` python
def fun2(a):
    print(a+100)

c = 5

while c < 10:
    fun2(c)
    c+=1
```

``` python
def fun(a,b):
    c = a**b
    return c

for x in range(2,4):
    for y in range(2,4):
        print(x,y, fun(x,y))
```

``` python
for row in range(7):
    for col in range(4 - abs(3 - row)):
        print('#', end='')
    print()
```

``` python
def f1(a):
    if a < 0:
        return 0
    elif a < 2:
        return 1
    elif a < 4:
        return 2
    else:
        return 3

for x in range(5):
    print('*' * f1(x))
```

``` python
word = "banana"
for c in word:
    # Recall:
    # bool(0) == False
    # bool(1) == True
    if word.index(c) % 2:
        print(c.upper())
    else:
        print(c)
```

``` python
word = "hello, world"
newword = word[0:2] + word[-2:]

print(newword)
```

```python
def foo(a):
    b = ""
    for c in a:
        if c.isalpha():
            b += c
    return b

print( foo("Hello, There!") )
```

``` python
phrase = "4 score and 7 years ago..."

for c in phrase:
    if not (c.isdigit()):
        print(c, end="")
    else:
        x = int(c)
        if x % 2 == 0:
            print(x+1, end="")
        else:
            print(x-1, end="")
```

``` python
x = 'cupid'
z = 'arrow'

if x < z:
    t = x
    x = z
    z = t

v = x + " <--> " + z

if ( ( (5 + 2 >= 6.0) and (1.0 < 0.5) ) or True):
    print (x,z,v, sep=' ')
else:
    print (v,z,x, sep='\n')
```

```python
a = 5
b = 10
c = 25

if a + b == c:
    print ("X1")
else:
    if c == a + b*2:
        print ("Y1")
    elif a == c - 2 * b:
        print ("Y2")
    else:
        print ("Y3")
```

```python
count = 0

while count < 10:
    print ('Hello')
    count += 1
```

``` python
x = 10
y = 0

while x > y:
    print (x, y)
    x = x - 1
    y = y + 1
```

``` python
keepgoing = True
x = 100

while keepgoing:
    print (x)
    x = x - 10
    if x < 50:
        keepgoing = False
```

``` python
a = 5
b = 6
c = 20
d = 24

if a < b and b * 2 < c:

    print ("Python Case 1")
    print ("A", "B", "C")
    
    if a * 2 == c:
        print (a*2, a*2, a*2)
    elif a * 3 == c:
        print (a*3, a*3, a*3)
    elif a * 4 == c:
        print (a*4, a*4, a*4)
    else:
        print ('?', '?', '?')
        
else:

    print ("Python Case 2")
    print ("a", "b", "c")
    
    if b * 2 == d:
        print (b*2, b*2, b*2)
    elif b * 3 == d:
        print (b*3, b*3, b*3)
    elif b * 4 == d:
        print (b*4, b*4, b*4)
    else:
        print ('?', '?', '?')
```

## Write a Program

Programs will be similar to what was encountered in exercises. Here are some additional practice problems.

1. Refactor and generalize the following Python program, which currently draws a triangle using the `turtle` module. Perform the following tasks to improve the code's structure and functionality without altering its original behavior:

   **Refactor** the original code to use a `for` loop, enabling it to draw a triangle by repeating certain actions. Afterward, refactor the code again to accomplish the same task using a `while` loop. Refactoring aims to reorganize the code to enhance its readability and maintainability.

   **Encapsulate** the drawing logic into a function named `triangle`. This function should take a turtle object `t` as its parameter, utilizing this object to draw the triangle. Encapsulation helps in modularizing the code, making it more organized and reusable.

   **Generalize** the encapsulated logic to create a new function called `polygon`. This function should accept the number of sides `n` and a turtle object `t` as its parameters. It should be capable of drawing polygons with any number of sides, thus extending the functionality of your code beyond drawing just triangles.

    ```python
    import turtle

    bob = turtle.Turtle()

    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    bob.left(120)
    ```

    The `turtle` module does not work within GitHub Codespaces, but here is a sandbox you can run `turtle` programs within: [https://pythonsandbox.com/turtle](https://pythonsandbox.com/turtle).

1. Write a program that asks the user to enter in number. Then have the computer generate a random number between 1 and 6 inclusive and compare the result. If the numbers are the same print out a "You Win!" message. If not, print out a "Game over!" message.

1. Write a program that prints out all numbers between 1 and 100 on the same line.

   1. Extension 1: Write a program that prints out all *even* numbers between 1 and 100 on the same line.

   2. Extension 2: Write a program that prints out all odd numbers between 1 and 100 on the same line.

   3. Extension 3: Write a program that asks the user to indicate whether they want to see even or odd numbers. Then display the even or odd numbers between 1 and 100 on the same line based on their choice. Note: the user many not supply a valid choice! You will need to re-prompt them if necessary. Here's a sample running of the program:

        ```text
        Enter "even" or "odd": apple
        Sorry, that's not a valid choice!
        Enter "even" or "odd": odd
        1 3 5 ... 95 97 99
        ```

1. Write a program that continually asks the user for a series of prices. Keep track of the running total as the user enters prices. Prompt the user after each price to see if they wish to continue entering prices. When they are finished, print out the total amount entered.

1. Write a function that accepts two arguments and computes the first argument raised to the power of the second argument.

1. Write a function that calculates the area of a triangle.

1. Write a recursive function that returns `n!`.

1. Write a function that accepts any positive integer and returns the sum of the digits without using a list, and and then using a list.

1. Write a function that accepts a grade as a single floating point value and returns its letter equivalent. Letters grades can be determined using the following table:

    ``` text
    100-90: A
    80-89.99: B
    70-79.99: C
    65-69.99: D
    Lower than 65: F
    ```

1. Write a function that accepts a single string as an argument. Your function should then determine if the string contains a majority of uppercase characters. For example, the String "ABCab" has 3 uppercase characters out of its 5 total characters, so it contains a majority of uppercase characters. If so, return True, and if not return False.

1. Write a function that accepts a single string as an argument. Flip the case of the String so that uppercase characters become lowercase and lowercase characters become uppercase. Return the new string.

1. Write a function that receives a list of integers and returns their sum.

1. Write a function that calculates the average of a list of numbers.
