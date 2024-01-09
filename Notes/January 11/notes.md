---
parent: Lessons
nav_order: 1
---

# Day 01: Computing Terminology, Arithmetic Operators

## Plan

- Set Up the Learning Environment
- Syllabus
- Computing
- Python Basics
  - Operators
  - Variables
 
## Set Up the Learning Environment

- Sign up for GitHub
- Explain GitHub
- Visit www.github.com/codespaces
- Set up blank codespace
- Create a lesson folder
- Create an exercise folder
- Change folder settings (optional)
- Create hello.py
- Install Python extension
- Adjust font size

# Review Syllabus

- It is fine to use ChatGPT or other generative AI tools on the programming exercises. In fact, I encourage you to use it to evaluate your solution and generate similar exercises. 

## What is a "computer"?

- The machine in front of you is a *modern* computer.
- A computer is one who computes.
- You are a computer!
- By today’s standards, you are a slow computer with bad memory… but necessary to design and implement modern computers.
- We need tools to aid in our computation as we move into the future

## What does a computer do?

- Performs calculations
- Remembers calculations
- What a human tells it to do

> “What I mean is that if you really want to understand something, the best way is to try and explain it to someone else. That forces you to sort it out in your own mind... And that’s really the essence of programming. By the time you’ve sorted out a complicated idea into little steps that even a stupid machine can deal with, you’ve certainly learned something about it yourself.”

> ― Douglas Adams, Dirk Gently's Holistic Detective Agency

## Terminology

**Computation** is any type of calculation that includes both arithmetical and non-arithmetical steps and which follows a well-defined model (e.g. an **algorithm**).

A **program** is a sequence of instructions that specify how to perform a computation.

## Guessing Game

``` text
I am thinking of a number! Try to guess it.
> 10
Too low! Guess again.
> 100
Too high! Guess again.
> -100
Too low! Guess again
> 95
That's it! Would you like to play again? (yes/no)
```

Main Ideas

- *variables* to store numbers
- Control flow
  - *conditionals* or *branching* to test guess
  - repetition (*looping*)
- input/output
- Data Types
  - numbers (*int*s, *float*s, etc)
  - words (_strings_)
- *functions* encapsulate repeated behavior
- `random` module

We will eventually build this, take care of errors, and improve gameplay.

## REPL

A **Read-Eval-Print Loop (REPL)**, also known as an interactive shell, is a simple, interactive computer programming environment that takes single user inputs (READ) (i.e. single expressions), EVALUATES them, and returns (PRINTS) the result to the user; a program written in a REPL environment is executed piecewise.

## Arithmetic Operators

[Official Python Docs: 3.10 Using Python as a Calculator](https://docs.python.org/3.10/tutorial/introduction.html#using-python-as-a-calculator)

Arithmetic operators follow the standard order of operation.

- `()` : parentheses
- `**` : exponentiation
- `+` : addition
- `-` : subtraction
- `*` : multiplication
- `/` : division
- `//` : floor dividion (quotient)
- `%` : modulus (remainder)

## calculator (interactive)

``` python
>>> 3 + 3
6
>>> (3 + 6) ** 2
81
>>> 5 / 2
2.5
>>> 100 / 50 - 1
1.0
>>> 7 // 3
2
>>> 7 % 3
1
```

## Exercises
1. An interger $p$ is prime if $1$ and $p$ are its only divisors. Find all the primes between $100$ and $1150$. Use the fact that $p$ is prime if $p$ `%` $n \neq 0$ for all $n \leq \sqrt{p}$.
