from data_loader import load_data
import re

def print_row(row_data, max_width, header = False):	
	row = ""
	for entry in row_data:
		entry_length = len(entry)
		if (max_width - entry_length < 0):
			row += f"|{entry[:(max_width - 3)]}..."
		else:
			padding = " " * (max_width - entry_length)
			split_index = len(padding) // 2
			padding_left = padding[:split_index]
			padding_right = padding[split_index:]
			row += "|" + padding_left + f"{entry}" + padding_right
	row += "|"
	print("\x1b[?7l", end="")  # Disable line wrap, temporary hack, implement term width calc later
	print(row)
	print("\x1b[?7h", end="")  # enable line wrap, temporary hack, implement term width calc later
	if (header):
		print("-" * len(row))

def match(value, matchValue, isRegex):
	if (isRegex):
		return re.search(matchValue, value)
	else:
		return value == matchValue

def columns_command(args):
	max_width = 30
	with load_data(args.file, args.delimiter) as reader:
		first_row = next(reader)
		columns = [
			i for i, col in enumerate(first_row) if match(col, args.match, args.regex)
		]
		print_row(first_row, max_width, header = True)
		for row in reader:
			print_row(row, max_width)