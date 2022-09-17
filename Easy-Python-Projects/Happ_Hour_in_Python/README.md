# Happy Hour Challenge

*Here's a step-by-step breakdown of our Python code.* 

## 1. Top of the file

```py
import random
```

*This imports other code. A library called 'random' that later allows us to pick out a random place or random person from our lists.*

## 2. Lists of Places & People 

```py
Places = ["MacDo",
        "LCW",
        "Marjan",
        "Picsin",
        "Burger King",
        "Hamam"]

people = ["Ali",
          "Hamza",
          "Hassan",
          "Salma",
          "Ghelo",
          "Sokky"
          "Robi",
          "Oummy"]
```

*These are lists of places and people. They are going to be pulled into...*

## 3. Pick a random place and a random person

```py
random_place = random.choice(Places)
random_person_one = random.choice(people)
```

*This is where our script picks a random place and a random person.*

## 4. Print out the results

```py
print(f"How about you go to {random_place} with {random_person_one}
```

*This line prints out the random place and random person.*
