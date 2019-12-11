from random import randint as rand
import time


def check_answer(first_num, second_num, given_answer, operation):
	if operation == "+":
		if str(first_num + second_num) == given_answer:
			return True
		else:
			return False
	if operation == "-":
		if str(first_num - second_num) == given_answer:
			return True
		else:
			return False
	if operation == "*":
		if str(first_num * second_num) == given_answer:
			return True
		else:
			return False
	if operation == "/":
		if str(first_num // second_num) == given_answer:
			return True
		else:
			return False


def time_convector(seconds):
	mins = int(seconds // 60)
	rounded_sec = int(seconds % 60)
	
	return mins, rounded_sec


def view_mistakes(mistakes):
	mistake_number = 0
	for m in mistakes:
		mistake_number += 1
		print(f"{mistake_number}.\t{m}")

def calculate(a, b, operation):
	if operation == '+':
		return a + b
	if operation == '-':
		return a - b
	if operation == '*':
		return a * b
	if operation == '/':
		return a // b


def get_operation():
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
	
	return operation

def swap(a, b):
	temp = a
	a = b
	b = temp
	
	return a, b

def countdown(game_mode, countdown_range=3, time_gap=1.5):
	print(f"Your game of {game_mode}\nstarts in...\n")
	countdown_numbers = [i for i in range(countdown_range)]
	countdown_numbers.reverse()
	
	for i in countdown_numbers:
		print(f"{i + 1}...\n")
		time.sleep(time_gap)


def generate_question(first_number, second_number, operation):
	if first_number < second_number:
		first_number, second_number = swap(first_number, second_number)
	
	return f"{first_number} {operation} {second_number} = "
