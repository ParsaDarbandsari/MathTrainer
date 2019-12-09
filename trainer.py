from time_attack import time_attack
from Q_king import q_king
from utils import *

game_mode = input("\n"
			 "SELECT A GAME MODE:\n"
			 "(Put the letter of your choosing game mode in order to play it)\n\n"
			 "\tA) Time Attack\tB) Q king"
			 "\n\n")

game_mode = game_mode.lower()

operating_number_range = int(input("What do you want the maximum of two terms to be? "))
mistakes = []

operation = get_operation()

if game_mode == 'a':
	testing_questions = int(input("How many questions do you want to answer? "))
	countdown('time attack')
	time_attack(operation, operating_number_range, testing_questions)
if game_mode == 'Q king':
	time_limit = float(input("How much is your time limit(in secs)? "))
	q_king(operation, operating_number_range, time_limit)
