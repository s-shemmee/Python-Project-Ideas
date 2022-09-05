## Introduction to Conditional Statements in Python

*Conditional statements (also known as if/than statements) let you define specific times when something should happen. For example,"if" you say yes "than" I'll tell you a joke. Or on a website, "if" you are logged into the site, "than" I will send you a special announcement. In this lesson, I'll show you how to write conditionals in Python.*

- Create a new file
- Create a new file called if.py:

```py
answer = input("Do you want to hear a joke? ")

if answer == "Yes":
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedberg (RIP)
```

- Running the file, we see our joke, or we don't. 

```bash
$ python if.py
Do you want to hear a joke? Yes
I'm against picketing, but I don't know how to show it.
$ python if.py
Do you want to hear a joke? No
$
```

## How does == work in Python?

*`==` checks to see whether two things are equal. It returns `True` if they are and `False` if they aren't.*

```bash
$ python
>>> "Yes" == "Yes"
True
>>> "No" == "Yes"
False
```

*Remember that even though they look similar, `=` and `==` are very different.*

```bash
$ python
>>> answer = "Yes"
>>> answer == "Yes"
True
>>> answer = "No"
>>> answer == "Yes"
False
```

*You can also use `!=` to check if two things are different:*

```bash
>>> answer != "Blue"
True
>>> answer != "No"
False
```

## How does if work?

*`if` will check to see if something is `True` and then run any indented code after (after the colon).* 

```py
if True:
    # Anything here will run
```

*And accordingly:* 

```py
if False:
    # This will never run
```

*In this lesson, we expand our knowledge of Python conditional statements by looking at ways of checking for more than one condition by using the if...else, if...elif...else and nested if conditional statements.*

## if, elif, and else 

- In `if.py`:

```py
answer = input("Do you want to hear a joke? ")

if answer == "Yes":
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedberg (RIP)
elif answer == "No":
    print("Fine.")
else:
    print("I don't understand.")
```

*`else` lets you say what code you want to run if the `if` part doesn't turn out to be true.*

*You can also add another `if` condition below the `if` with `elif` (you can actually add as many `elifs `as you want).*