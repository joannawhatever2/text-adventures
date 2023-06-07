## LEVEL: Beginner
## LANG: Python
## LIBS: Random
## CONCEPTS: Functions, Input, Conditionals, Loops, Random Choice, Random Chance, Formatting Strings, Boolean While

import random

available_toppings = ["cat", "bird", "dog"]
toppings_list = []

def randomTopping():
  item = random.choice(available_toppings)
  toppings_list.append(item)
  print(item)
  if random.randint(1, 100) > 50:
    available_toppings.remove(item)
    print(f"Ooo, that was the last {item}!")

def icecreamIntro():
  print("You're at an ice cream store.")
  print("Toppings are added randomly to your sundae.")
  print("But, you can decide when you've had enough.")
  print()

def toppings():
  enough = False
  
  while enough is False:
    print('----------------')
    print("Delivering Topping...")
    print('----------------')
    randomTopping()
    print()
    if len(available_toppings) > 0:
      a = input("would you like another topping?\n")
      if a == "no":
        enough = True
    else:
      print("I'm sorry, we're out of toppings.")
      enough = True
    
  print("Your sundae has the following toppings:")
  for item in toppings_list:
    print(item)


def main():
    icecreamIntro()
    toppings()

if __name__ == "__main__":
    main()
