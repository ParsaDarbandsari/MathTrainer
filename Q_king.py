from random import randint as rand
from utils import *
import time

def q_king(operation, number_range, time_limit):
	correct_answers = 0
	mistakes = []
	time_lapsed = 0
	qs_answered = 0

	while time_lapsed <= time_limit:
		starting_time = time.time()
		current_operation = operation[rand(0, (len(operation) - 1))]
		first_number = rand(1, number_range)
		second_number = rand(1, number_range)
		if first_number < second_number:
			first_number, second_number = swap(first_number, second_number)
		question = f"{first_number} {current_operation} {second_number} = "
		player_answer = input(question)
		qs_answered += 1
		mark = check_answer(first_number, second_number, player_answer, current_operation)
		if mark is True:
			correct_answers += 1
		else:
			mistakes.append(f"{question}{player_answer}, correct answer: {first_number + second_number}")
		ending_time = time.time()
		time_lapsed += ending_time - starting_time
	
	print(f"\n"
		  f"You Have got managed to answer {qs_answered} question(s) and {correct_answers} of them were correct")
	
	if mistakes != []:
		input("Press Enter to view mistakes")
		view_mistakes(mistakes)
