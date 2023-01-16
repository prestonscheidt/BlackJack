
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  random_card = random.choice(cards)
  return random_card
  
    
def play_game():    

  print(logo)
  
  deal_card()
  
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
      return 0
      
    if 11 in cards and sum(cards) > 21:
      cards.remove(11) and cards.append(1)
       
    return sum(cards)
  
  is_game_over = False
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards are {user_cards} and your score is {user_score}")
    print(f"Computer's first card is {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      print("Game Over")
    else:
      another_card = input("Do you want to draw another card? Type yes or no\n")
      if another_card == "yes":
        user_cards.append(deal_card())
      if another_card == "no":
        is_game_over = True
        print("game over")
  
  while computer_score != 0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  def compare(user_score,computer_score):
    if user_score == computer_score:
      return "It is a draw"
      
    elif computer_score == 0:
      return "Computer Wins"
  
    elif user_score == 0:
      return "User has a blackjack and wins"
  
    elif computer_score > 21:
      return "Computer Bust You Win!"
  
    elif user_score > 21:
      return "User bust"
  
    elif user_score > computer_score:
      return "User Wins"
    else:
      return "Computer Wins"
      
  print(f"Your hand was {user_cards} and your score was {user_score}")
  print(f"Computer's cards were {computer_cards} and its score was {computer_score}")
  print(compare(user_score,computer_score))

print(logo)
while input("Play Game? yes or no\n") == "yes":
  clear()
  play_game()
  

