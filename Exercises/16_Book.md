# Functions

Functions are very useful in programming, as they give us the oppertunity to have some variety. For example, observe this function:
```python
def add(x,y,z):
  addedNumbers = x + y + z
  print(addedNumbers)

add(1,2,3)
add(4,9,2)
```
The cool part, is that we can call the add() function as many times as we would like, with different arguments for our x,y,and z parameters.

# Book

Write a function called `favorite_book` that accepts one parameter, `title`. The function should **print** the message "One of my favorite books is {`title`}".


# Test Case 1
```
>>> favorite_book("The Bible")
'One of my favorite books is The Bible'
