
import random
# from replit import clear
from art import logo



def deal_card():
  card_pack = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  n=random.randint(0,12)
  return card_pack[n]

def display(com_cards,user_cards):
  print(f"Comuters final hand:{com_cards},final score: {sum(com_cards)} ")
  print(f"Users final hand:{user_cards},final score: {sum(user_cards)} ")

def calculate_score(cards_list):
  """takes list and returns sum if sum is 21 returns 0"""
  score=int(sum(cards_list))
  if(score==21 ):
    return 0
  elif(score>21 and len(cards_list)==2):
    
    cards_list.remove(11)
    cards_list.append(1)
    return sum(cards_list)
  else:
    return score

def compare(user_score,computer_score):
  if user_score == computer_score:
    return 'Draw 😐'
  elif computer_score==0:
    return 'Lose, Openent has  BlackJack😫😱'
  elif user_score==0:
    return 'Win with BlackJack😍🤩'
  elif user_score>21:
    return 'You Went Over. You lose🤯😲'
  elif computer_score>21:
    return 'Opponent Went over. You Win 🤣 😁'
  elif user_score>computer_score:
    return 'You Win 😊😎'
  else:
    return 'You Lose😱😒'
def play_game()  :
  print(logo)
  
  com_cards=[]
  user_cards=[]
  
  total_cc=0 
  total_uc=0
  is_game_over=False
  
  for i in range(2):
    com_cards.append(deal_card())
    user_cards.append(deal_card())
  while not is_game_over:
  
    total_cc=(calculate_score(com_cards))
    total_uc=(calculate_score(user_cards))
    print(f"Your cards: {user_cards} , curreent score {total_uc} ")
    print(f"Compter's first card :{com_cards[0]} ")
    
    if(total_uc==0 or total_cc==0 or total_uc > 21):
      is_game_over=True
    else:
      user_choise=input("Enter 'y' to get another card, type 'n' to pass: ")
      if(user_choise=='y'):
        user_cards.append(deal_card())
      else:
        is_game_over=True 
  while total_cc!=0 and total_cc<17:
    com_cards.append(deal_card())
    total_cc=calculate_score(com_cards)
  print(display(com_cards,user_cards))    
  print(compare(total_uc,total_cc)    )


while input("Do You Want to play BlackJack? Enter y or n: ")== 'y' :
  
  play_game()



  