#Number Guessing Game Objectives:
from art import logo
print(logo)
import random
from replit import clear
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# level = input('enter easy for beginner and hard for expert:\n')

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
#difficulty = input('enter easy for beginner and hard for expert:\n')

#Think of a number stage
def guessNumber():
  """
  level and difficulty choice
  """
  level = input('enter easy for beginner and hard for expert:\n')
  
  BEGINNER_LEVEL = 11
  EXPERT_LEVEL = 6

  thinkAnumber = random.choice(range(1, 101)) 
  print(thinkAnumber)
  
  if level == 'easy':
    moreLife = True
    while moreLife:
      BEGINNER_LEVEL -= 1
      print(f'you have {BEGINNER_LEVEL} lives left')
      if guessResult(thinkAnumber, youGuess()) == "win":
        moreLife = False
        
      elif BEGINNER_LEVEL == 1:
        print(f"you are out of guess\nYOU LOSE")
        moreLife = False
     
  elif level == 'hard':
    moreLife = True
    while moreLife:
      EXPERT_LEVEL -= 1
      print(f'you have {EXPERT_LEVEL} lives left')
      if guessResult(thinkAnumber, youGuess()) == "win":
        moreLife = False
        
      elif EXPERT_LEVEL == 1:
        print(f"you are out of guess\nYOU LOSE")
        moreLife = False
  return thinkAnumber

#make your guess 
def youGuess():
  """
  make a guess
  """
  makeGuess = int(input('guess the number: '))
  print(f"your guess: {makeGuess}")
  return makeGuess
  
# check if guess is write or wrong
def guessResult(thinkAnumber, makeGuess):
  """
  check if guess is write or wrong
  """
  if makeGuess == thinkAnumber:
    print(f"you guessed right\nYOU WIN")
    return "win"
    
  elif thinkAnumber != makeGuess:
    if thinkAnumber > makeGuess:
      print("Too low\nTRY AGAIN")
     
    elif thinkAnumber < makeGuess:
      print("Too high\nTRY AGAIN")
      
playOn = True
while playOn:
  value = input("enter yes to play and no to end game: ")
  if value == "yes":
    clear()
    guessNumber() 
  else:
    playOn = False
