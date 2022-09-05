# The Famous Fizzbuzz Challenge

*Challenge time! You are going to use what you've learned so far to solve the famous FizzBuzz Coding Challenge. The challenge is one of the most common coding interview questions.*

**Here's the FizzBuzz challenge.**

- Create a new file called `fizzbuzz.py`:

```py
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

```
*Good luck!*



# FizzBuzz Challenge: Solution

*Here's the answer to FizzBuzz in Python. Hopefully, you gave the FizzBuzz challenge a try. Whether you got the solution or not, let's work through the logic together.*

## Step #1

- First print out the numbers from 1 to 100:
```py
for number in range(1,101):
    print(number)
```

## Step #2

- Print "Fizz" if the number is divisible by 3:

```py
for number in range(1,101):
    if number % 3 == 0:
        print("Fizz")
    else:
        print(number)
```

## Step #3

- Print "Buzz" if the number is divisible by 5:

```py
for number in range(1,101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

## Step #4

- Print "FizzBuzz" if the number is divisible by 3 and 5:

```py
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

**(Note that this new condition `number % 3 == 0 and number % 5 == 0` has to go above the other two because otherwise the others run first.)**