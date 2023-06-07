## LEVEL: Beginner
## LANG: Python
## LIBS: Time
## CONCEPTS: Functions, Input, Conditionals

import time

def antIntro():
  print('.-.  .-..----. .-. .-..----. .----.')
  print(' \ \/ //  {}  \| { } || {}  }| {_  ')
  print('  }  { \      /| {_} || .-. \| {__ ')
  print("  `--'  `----' `-----'`-' `-'`----'")
  time.sleep(1)
  print('   .--.  .-. .-.')
  print('  / {} \ |  `| |')
  print(' /  /\  \| |\  |')
  print(" `-'  `-'`-' `-'")
  time.sleep(0.25)
  os.system('clear')
  print('.-.  .-..----. .-. .-..----. .----.')
  print(' \ \/ //  {}  \| { } || {}  }| {_  ')
  print('  }  { \      /| {_} || .-. \| {__ ')
  print("  `--'  `----' `-----'`-' `-'`----'")
  print('   .--.  .-. .-.     .--.  .-. .-. .---. ')
  print('  / {} \ |  `| |    / {} \ |  `| |{_   _}')
  print(' /  /\  \| |\  |   /  /\  \| |\  |  | |  ')
  print(" `-'  `-'`-' `-'   `-'  `-'`-' `-'  `-'  ")
  time.sleep(1)
  print('.-. .-.  .--.  .----. .----. .-.  .-.')
  print('| {_} | / {} \ | {}  }| {}  } \ \/ / ')
  print('| { } |/  /\  \| .-. \| .-. \  }  {  ')
  print("`-' `-'`-'  `-'`-' `-'`-' `-'  `--'  ")
  time.sleep(1)

def antScene1():
  print()
  print("you are an ant.")
  time.sleep(1)
  print()

def antScene2():
  print()
  print("you are in an ant hill.")
  time.sleep(1)
  print()

def antScene3():
  print()
  print("you are in an ant line.")
  time.sleep(1)
  print()

def antScene4():
  print()
  print("You march and get a leaf and then bring it back to the hill and then sleep.")
  time.sleep(1)
  print()

# main!
def ant():  
  antScene1()
  choiceA = input("yes or no? ")
  
  if choiceA != "yes":
    print("you're not an ant.")
    
  elif choiceA == "yes":
    antScene2()
    choiceB = input("yes or no? ")
    if choiceB != "yes":
      print("you're not in an ant hill.")
      
    elif choiceB == "yes":
      antScene3()
      choiceC = input("yes or no? ")
      if choiceC != "yes":
        print("you're not in an ant line.")
        
      elif choiceC == "yes":
        antScene4()
  
  print("The End")
  
def main():
    antIntro()
    ant()

if __name__ == "__main__":
    main()  
