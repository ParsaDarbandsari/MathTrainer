from random import randint as rand
from utils import *
import time

correct_answers = 0
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
testing_questions = int(input("How many questions do you want to answer? "))
operating_number_range = int(input("How big do you want the numbers on each side to be? "))
starting_time = time.time()
mistakes = []

for i in range(testing_questions):
	current_operation = operation[rand(0, (len(operation) - 1))]
	first_number = rand(1, operating_number_range)
	second_number = rand(1, operating_number_range)
	question = f"{first_number} {current_operation} {second_number} = "
	player_answer = input(question)
	mark = check_answer(first_number, second_number, player_answer, current_operation)
	if mark is True:
		correct_answers += 1
	else:
		mistakes.append(f"{question}{player_answer}, correct answer: {first_number + second_number}")

ending_time = time.time()
time_lapsed = ending_time - starting_time
time_taken = time_convector(time_lapsed)

print(f"\n"
	  f"You Have got {correct_answers} questions right out of {testing_questions} questions.\n"
	  f"in {time_taken}")

if mistakes != []:
	input("Press Enter to view mistakes")
	view_mistakes(mistakes)
