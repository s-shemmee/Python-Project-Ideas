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