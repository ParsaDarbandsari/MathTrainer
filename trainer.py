from time_attack import time_attack
from Q_king import q_king

operation = []
operation_letters = input("Which operation(s) do you want to have in your questions\n"
				  "(Put the letter of one or more operation you want to have in order to add it, please separate your letters using comma)\n\n"
				  "A) Addition (+)\n"
				  "B) Subtraction (-)\n"
				  "C) Multiplication (*)\n"
				  "D) Division(/)\n"
				  "Put your operation(s) here: ")
operation_letters = operation_letters.upper()
operation_letters = operation_letters.replace(' ', '')
operation_letters = operation_letters.split(',')
operation_letter_translator = {
	"A": "+",
	"B": "-",
	"C": "*",
	"D": "/"
}
for ols in operation_letters:
	operation.append(operation_letter_translator[ols])

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
