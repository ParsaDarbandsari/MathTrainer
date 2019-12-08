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

def swap(a, b):
	temp = a
	a = b
	b = temp
	
	return a, b
