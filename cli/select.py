from .data_loader import load_data
from .formatter import format_row
from .search_utils import match


def select_command(args):
	max_width = 15
	with load_data(args.file, args.delimiter) as reader:
		col_list = args.column_list.split(",")
		first_row = next(reader)
		if (not args.ignore_missing):
			for col in col_list:
				if not col in first_row:
					raise ValueError(f"Invalid columns: {col}")
		columns = [
			i for i, col in enumerate(first_row) if col in col_list
		]
		print(format_row([first_row[i] for i in columns], max_width, header = True))	
		for row in reader:
			filtered_row = [row[i] for i in columns]
			print(format_row(filtered_row, max_width))