#Secret Bid program
import os


from art import logo as logo

print(logo)
print('Welcome to secret Auction program.')
dict_bids = {}
flag = True
while (flag):

  name = input('What is your name:')
  bid_value = int(input("What's  your Bid: Rs."))
  dict_bids[name] = bid_value

  choice = input("Are there anu other bidders. Type yes or no:")
  if (choice == 'yes'):
    os.system.clear()
    continue
  else:
    break
high_value = 0
winner = ''
def winner_declaration(dict_bids,high_value,winner):
  for key in dict_bids:
    if (dict_bids[key] > high_value):
      high_value = dict_bids[key]
      winner = key
  print(f"Winner is {winner} with a bid Rs.{high_value} ")

winner_declaration(dict_bids,high_value=0,winner='')
