from random import randint
from art import logo


def checker(n, guess_no):
  # print(guess_no)
  for i in range(int(n)):
      user_choice = int(
          input((f"You have {n-i} Attempts remaining.\n Guess number:")))
      if (user_choice == guess_no):
          print(f"You got it .The answer was {guess_no}")
          return
      elif (user_choice > guess_no):
          print("Too High. \nGuess Again.")
          continue
      else:
          print("Too Low. Guess again")
          continue
  print("You Loose. You've run out of Guess.")

print(f"\n {logo}")
print('Welcome to Guessing Game.')
guess_no = randint(1, 100)
easy_hard = (input("Choose Difficulty. Type easy or hard :"))

if (easy_hard == 'easy'):
    checker(10, guess_no)
else:
    checker(5, guess_no)
