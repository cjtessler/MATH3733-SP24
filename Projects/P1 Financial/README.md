# Project 1: Financial

*Read through the entire project description before beginning.*

This project will consist of three parts. In part 1, you will write a program that calculates the minimum number of coins required to give the user change. In part 2, you will write a program to determine how long it will take you to save enough money to make a down payment on a house. In part 3, you will compute how change should be returned.

## Collaboration Policy

Students may collaborate on the projects, meaning you're free to seek help from the professor, the internet, or your friends. Any code referenced on internet forums, Stack Overflow, tutorials, or any similar resource that is used to solve a problem should be cited in comments. If two or more students choose to solve a problem together, they are required to write code independently and note all the collaborators. Students cannot use the exact same code (for example, by dictating to each other). Students are not permitted to look at or copy each other’s code or code structure. Students are not permitted to share/send code to others. The official collaboration policy is that two students may discuss a solution together, but the code must be written separately by each student. No plagiarism or copying of solutions is allowed. Project submissions will be run against similarity software. **Violations of this policy will result in a zero on the project.**

**Background on policy:** The first concern is what the students in the class learn. It is assumed that everyone in the class is here because they want to learn, and will behave in a manner consistent with that goal and their personal learning style. Much of the learning takes place while working on the projects or exercises. Working with other students often enhances the learning process. Keep in mind that collaborative learning works best when the students working together have roughly the same level of knowledge and skill so that each participant in the collaboration can contribute more or less equally to solving the problem. When one student is consistently showing another how to do things, it is not a true collaboration. When one student bases their solution on the completed work of another or on a found solution, little to no learning takes place. If students choose to lean heavily on the work of others, such students will be cheating themselves and will learn less. Moreover, while these students may end up with excellent grades on the problem sets, they will almost surely struggle with the exams, which account for 30% the final grade.

## Generative AI Policy

TODO

## Part 1: Change

Write a program that calculates the minimum number of coins required to give a user change. Here is an example of the program's execution:

``` text
1   Project-1-Financial$ python change.py
2   Change owed: -0.20
3   Change owed: 
4   Change owed: 1.001
5   Change owed: 0.43
6   6
```

On line 1, the Python interpreter is invoked with the file to run.\
On line 2, the user is prompted and enters a negative number. The program rejects this input and reprompt the user, as seen on line 3.\
On line 3, the user is prompted and presses enter without entering an input. The program rejects this input and reprompts the user, as seen on the line 4.\
On line 4, the user is prompted and enters 1.001, which is an invalid change amount. the program rejects this input and reprompts the user as seen on line 5.\
On line 5, the user is prompted and enters 0.43. The program accepts this input and completes the computation.
On line 6, the program prints 6 because 43 cents is made using 1 quarter, 1 dime, 1 nickel, and 3 pennies, i.e., 6 coins.

### Specificiation

- In `change.py`, write a program that first asks the user how much change is owed and then splits out the minimum number of coins with which said change can be made.
- Assume that the user will input their change in dollars (e.g., `0.50` and not `50 cents`
- Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
- The user may enter a string, integer, or float.
- The user should continually be asked for input until the user enters a valid input.
- If the user inputs a negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
- The output should be an integer.

### Testing

The assignment will be autograded by GitHub Classroom for correctness. Consider all of the different possible inputs and how they should be handled. Here are a few possible tests:

- Run your program as `python change.py`, and wait for a prompt for input. Type in `0.41` and press enter. Your program should output `4`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `0.01` and press enter. Your program should output `1`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `0.15` and press enter. Your program should output `2`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `1.60` and press enter. Your program should output `7`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `23` and press enter. Your program should output `92`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `4.2` and press enter. Your program should output `18`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `0` and press enter. Your program should output `0`.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `1.001` and press the enter key. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python change.py`, and wait for a prompt for input. Type in `-1` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python change.py`, and wait for a prompt for input. Do not type anything, and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.

**Make sure your program behaves as shown above. Your submission might be autograded locally.**

## Part 2: Saving

It's time to buy a house! It is a big purchase, so it might be some time before you can afford the down payment. Our goal in `saving.py` is to determine how long it will take you to save for a down payment. Write a program to calculate how many months it will take to save up enough money for a down payment.*

### Specification

1. Ask the user for their annual salary and call it `annual_salary`.
2. Ask the user how much how much of the salary will be set aside each month to saving for the down payment and call it `portion_saved`. This variable should be in decimal form, i.e., 0.1 for 10%.
3. Ask the user for the cost of the home and call it `total_cost`.
4. Ask the user how much percentage the down payment will be and call the portion of the cost needed for a down payment `portion_down_payment`.
5. Ask the user for the annual rate of return and call it `r`. For example, if the annual rate of return is 4%, the user should enter 0.04.
6. Call the amount that you saved thus far `current_savings`. You start with $0 in savings.
7. Assume that you invest your current savings wisely, with an annual return of `r`. That is, at the end of each month, you receive an additional `current_savings * r / 12` funds to put into your savings. The 12 in the previous expression is because `r` is an **annual** rate.
8. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (notice you asked the user for their *annual* salary).

You will want your main variables to be floats, so be sure to cast user inputs to floats.

### Testing

There is no automated testing. Regardless, you should still thoroughly test your program. Consider all of the different possible inputs and how they should be handled. **Make sure your program prints results in the format shown below. Your submission might be autograded.**

#### Test Case 1

``` text
~Project-1-Financial$ python savings.py
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of the home: 1000000
Enter the necessary down payment percent, as a decimal: .25
Enter the annual rate of return, as a decimal: 0.04
It will take 183 months to save for the down payment.
```

#### Test Case 2

``` text
~Project-1-Financial$ python savings.py
Enter your annual salary: 80000
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of the home: 500000
Enter the necessary down payment percent, as a decimal: .25
Enter the annual rate of return, as a decimal: 0.04
It will take 105 months to save for the down payment.
```

There will be other test cases not shown here. **Although unlike part 1, you may assume the user will enter appropriate information so you do not need to validate input.**

## Bonus: Change Challenge

- In `challenge.py`, write a program that computes how change should be given for a user's input.
- The denominations available are $100 bill, $50 bill, $20 bill, $10 bill, $5 bill, $1 bill, quarter, nickel, dime, and penny.
- Unused denominations should be ignored.
- You do NOT need to account for plurality. E.g. "5 penny" is fine, although "5 pennies" is grammatically correct.

``` text
~Project-1-Financial$ python change_challenge.py
Change owed: 1.42
1 $1 dollar, 1 quarter, 1 dime, 1 nickel, and 2 penny
```

``` text
~Project-1-Financial$ python change_challenge.py
Change owed: 123.27
1 $100 dollar, 1 $20 dollar, 3 $1 dollar, 1 quarter, 2 penny
```

## Closing Remarks

Any edits or clarifications to the project will be announced in class and shown in the changelog below. Good luck and have fun!

### Tips

- Try working out the computations by hand.
- Try "Rubber Duck Debugging": [https://rubberduckdebugging.com/](https://rubberduckdebugging.com/)
- Use the VS Code debugging tools: TODO

### Changelog
