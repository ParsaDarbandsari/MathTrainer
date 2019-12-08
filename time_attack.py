from random import randint as rand
from utils import *
import time

def time_attack(operation, number_range, testing_qs):
	correct_answers = 0
	mistakes = []
	
	starting_time = time.time()
	for i in range(testing_qs):
		current_operation = operation[rand(0, (len(operation) - 1))]
		first_number = rand(1, number_range)
		second_number = rand(1, number_range)
		if first_number < second_number:
			temp = first_number
			first_number = second_number
			second_number = temp
		question = f"{first_number} {current_operation} {second_number} = "
		player_answer = input(question)
		mark = check_answer(first_number, second_number, player_answer, current_operation)
		if mark is True:
			correct_answers += 1
		else:
			mistakes.append(f"{question}{player_answer}, correct answer: {calculate(first_number, second_number, current_operation)}")
	ending_time = time.time()
	time_lapsed = ending_time - starting_time
	mins_taken, secs_taken = time_convector(time_lapsed)
	print(f"\n"
		  f"You Have got {correct_answers} questions right out of {testing_qs} questions.\n"
		  f"in {mins_taken} minute(s) and {secs_taken} second(s)")
	
	if mistakes != []:
		input("Press Enter to view mistakes")
		view_mistakes(mistakes)
