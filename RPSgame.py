"""This is a rock scissors paper game"""

from random import randint
from time import sleep

options = ["R", "P", "S"]

loss_message = "You lost!"
win_message = "You won!"

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer select: %s" % computer_choice
  
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
  	print win_message
  elif user_choice_index == 1 and computer_choice_index == 0:
  	print win_message
  elif user_choice_index == 2 and computer_choice_index == 1:
  	print win_message
  elif user_choice_index > 2:
  	print "That's an invalid option"
    	return
  else:
  	print loss_message
    
def play_RPS():
  print "This is a Rock Paper Scissors Game"
  user_choice = raw_input("R - Rock, P - Paper, S - Scissors. Type in your selection: ").upper()
  sleep(1)
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()