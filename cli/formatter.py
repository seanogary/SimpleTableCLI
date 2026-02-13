import sys
from shutil import get_terminal_size

def format_row(row_data, max_width, header = False):	
	if (not sys.stdout.isatty()): return ", ".join(row_data)
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

	terminal_width = get_terminal_size().columns

	row = row[:(terminal_width - max_width)]

	if (header):
		separator = "-" * len(row)
		row = separator + "\n" + row +  "\n"  + separator
	
	return row

