import random


def weasel_program():
	seed = prompt_user()


def prompt_user():
	info = ('The weasel program, Dawkins weasel, or the Dawkins weasel is a' +
			'thought experiment and a variety of computer simulations ' +
			'illustrating it. Their aim is to demonstrate that the process' +
			' that drives evolutionary systems—random variation combined ' + 
			'with non-random cumulative ' +
			'selection—is different from pure chance.'
			 )

	print (normalize_string(info, 4, 78))


def normalize_string(string, start_space, max_line_ength):
	"""
	Normalizes length of lines and returns each line as a list.
	Also adds some space to the begging of each line.
	"""
	string = str(string)
	lines = []
	line = ' ' * start_space
	for character in string:
		if len(line) >= max_line_ength:
			print (line)
			lines.append(line)
			line = ' ' * start_space
		line += character
	return (lines)


	
weasel_program()
raw_input = ('stawp')

