import random

Places = ["MacDo",
        "LCW",
        "Marjan",
        "Picsin",
        "Burger King",
        "Hamam"]

people = ["Ali",
          "Hamza",
          "Hassan Sensei",
          "Salma",
          "Ghelo",
          "Sokky",
          "Robi",
          "Oummy"]

random_place = random.choice(Places)
random_person_one = random.choice(people)
random_person_two = random.choice(people)

print(f"How about you go to {random_place} with {random_person_one} and {random_person_two}?")
