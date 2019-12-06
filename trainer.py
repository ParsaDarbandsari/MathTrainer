from random import randint as rand
from utils import *
import time

operation = "+"
correct_answers = 0
testing_questions = int(input("How many questions do you want to answer? "))
starting_time = time.time()
operating_number_range = int(input("How big do you want the addition numbers to be? "))
mistakes = []

for i in range(testing_questions):
	first_number = rand(1, operating_number_range)
	second_number = rand(1, operating_number_range)
	question = f"{first_number} {operation} {second_number} = "
	player_answer = input(question)
	mark = check_answer(first_number, second_number, player_answer, operation)
	if mark is True:
		correct_answers += 1
	else:
		mistakes.append(f"{question}{player_answer}")

ending_time = time.time()
time_lapsed = ending_time - starting_time
time_taken = time_convector(time_lapsed)

print(f"\n"
	  f"You Have got {correct_answers} questions right out of {testing_questions} questions.\n"
	  f"in {time_taken}")

if mistakes is not []:
	input("Press Enter to view mistakes")
	view_mistakes(mistakes)
