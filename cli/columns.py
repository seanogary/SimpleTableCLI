from data_loader import load_data
import re
from shutil import get_terminal_size

def print_row(row_data, max_width, columns = None, header = False):	
	row = ""
	if columns is not None:
		tmp_row_data = []
		for col_index in columns:
			tmp_row_data.append(row_data[col_index])
	row_data = tmp_row_data
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
	terminal_width = get_terminal_size().columns
	print(row[:(terminal_width - max_width)])
	if (header):
		divider = ("-" * len(row))[:(terminal_width - max_width)]
		print(divider)

def match(value, matchValue, isRegex):
	if (isRegex):
		return re.search(matchValue, value)
	else:
		return value == matchValue

def columns_command(args):
	max_width = 15
	with load_data(args.file, args.delimiter) as reader:
		first_row = next(reader)
		columns = [
			i for i, col in enumerate(first_row) if match(col, args.match, args.regex)
		]
		print_row(first_row, max_width, columns, header = True)
		for row in reader:
			print_row(row, max_width, columns)