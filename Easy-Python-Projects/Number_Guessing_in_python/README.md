# Guess The Number Game in Python – Mini Project

*This is one of the simple python projects for beginners but still the interesting one. In this project, we will create a python program in which the system will choose a random number between any ranges defined, and then the user is given a hint to guess the number. Every time the user guesses the number wrongly, he is given another clue leading him towards the answer. The clue can be of any type like smaller, greater, multiples, dividers, etc. We will also need a function for checking the input is correct or not and to check the difference between the original number and the number guessed.*

## What we are gonna do?

*The random function generates the number between 1 to 100. The user has 10 chances to guess the number. So, we ask max 10 times to user to enter a number. Once the user guess is matched with an actual number then the game is over. Every time user also sees how many no. of chances are left. If the user can’t guess the number then the game is over. Simple!!*

## Which Python concepts are covered?

- If-else
- While Loop
- Random function
- break statement

## Let’s code

- **Imports and declaration**

```py
import random
n = random.randint(1, 100)
count = 1
guess_chances = 10
```

*So we need a random module to generate a random number. Variable n holds the one random number between 1 to 100. count variable for the count the number of guess user took, initially 1. guess_chances holds a number of chances code give to a user to guess the number.*

- **Inside the while loop**

```py
num = int(eval(input("Guess the number " )))
if num > n:
  print('Your guess was too high: Guess a number lower than ', num)
elif num < n:
  print('Your guess was too low: Guess a number higher than ', num)
else:
  print('YOU WIN!')
  print('You guessed the number in ' + str(count) + ' tries!')
  break
```

- We ask the user to guess the number. And store guessed number in `num` variable. Then we do comparisons with the generated number `n`.

*In the first condition, if the guessed number is higher then the actual number than prints **Your guess was too high: Guess a number lower than** (your number). So, the user can get the idea, and next time he/she enters a lower number.*

- If the first condition is false, then flow goes for check second condition, if the guessed number is lower than actual number then prints **Your guess was too low: Guess a number higher than** (your number). So, the user can get the idea, and next time he/she enters a higher number.

- If above both condition returns false. Then the user guessed number is matched with the actual number and the loop will be terminated by a break statement. Code also prints **YOU WIN!** message and number of guesses taken by the user that counted by count variable.

*With this above all condition, code also prints the number of guesses left for the user, and the count variable increases by one in every iteration to print a number of guesses taken by the user once the user wins the game.*

```py
guess_chances -= 1
  print(guess_chances, 'Guesses Left')
  count += 1
```

*So, the above all conditions are written in a while loop. **while** loop gets terminated once the user wins the game or no. of guesses reaches the limit.*

```py
while 1 <= guess_chances:
```

*Outside of the loop, code will print the Game Over message with the actual number.*

```py
print("GAME OVER")
print("Number is ", n)
```

## The full code

```py
import random

n = random.randint(1, 100)
count = 1
guess_chances = 10
player_name = input("Hey, What's ur name? ")

print('Lovely to meet you! ' + player_name)

answer = input('Do You want to play guessing game with me? ')
if answer == 'no':
  print('oh okay, maybe next time')
elif answer == 'yes' :
  print('Alright ' + player_name + ' I am thinking about a number between 1 and 100 and you have 10 chances to guess it ;D')
  print('Lets get started')
  while 1 <= guess_chances:
    num = int(eval(input("Guess the number " )))
    if num > n:
      print('Your guess was too high: Guess a number lower than ', num)
    elif num < n:
      print('Your guess was too low: Guess a number higher than ', num)
    else:
      print('YOU WIN!')
      print('You guessed the number in ' + str(count) + ' tries!')
      break
    guess_chances -= 1
    print(guess_chances, 'Guesses Left')
    count += 1

  print("GAME OVER")
  print("Number is ", n)
  print('Thanks for playing :D')

else:
  print('sorry, I didnt get it')
```

## Output

```
$ py number_guessing.py 
Hey, What's ur name? 
shemmee

Lovely to meet you! shemmee

Do You want to play guessing game with me? 
yes
Alright shemmee I am thinking about a number between 1 and 100 and you have 10 chances to guess it ;D      

Lets get started

Guess the number 
37
Your guess was too high: Guess a number lower than  37
9 Guesses Left

Guess the number 
20
Your guess was too low: Guess a number higher than  20
8 Guesses Left

Guess the number 
30
Your guess was too high: Guess a number lower than  30
7 Guesses Left

Guess the number 
29
YOU WIN!
You guessed the number in 4 tries!
GAME OVER
Number is  29
Thanks for playing :D
```