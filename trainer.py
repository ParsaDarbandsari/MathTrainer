from time_attack import time_attack
from Q_king import q_king
from utils import *

operation = get_operation()

operating_number_range = int(input("How big do you want the numbers on each side to be? "))
mistakes = []
mode = input("\n"
			 "SELECT A GAME MODE:\n"
			 "(Put the letter of your choosing game mode in order to play it)\n\n"
			 "\tA) Time Attack\tB) Q king"
			 "\n\n")

mode = mode.lower()

if mode == 'a':
	testing_questions = int(input("How many questions do you want to answer? "))
	time_attack(operation, operating_number_range, testing_questions)
if mode == 'b':
	time_limit = float(input("How much is your time limit(in secs)? "))
	q_king(operation, operating_number_range, time_limit)
