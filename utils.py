def check_answer(first_num, second_num, given_answer, operation):
	if operation == "+":
		if str(first_num + second_num) == given_answer:
			return True
		else:
			return False


def time_convector(seconds, alignment="long"):
	mins = int(seconds // 60)
	rounded_sec = int(seconds % 60)
	alignments = {
		"simple": f"{mins}:{rounded_sec}",
		"long": f"{mins} minute(s) and {rounded_sec} second(s)"
	}
	
	convented_time = alignments[alignment]
	
	
	return convented_time

def view_mistakes(mistakes):
	mistake_number = 0
	for m in mistakes:
		mistake_number += 1
		print(f"{mistake_number}.\t{m}")
