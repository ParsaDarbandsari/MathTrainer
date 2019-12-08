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
