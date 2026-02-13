from .data_loader import load_data
from .formatter import format_row
from .search_utils import match

def filter_command(args):
	max_width = 15
	with load_data(args.file, args.delimiter) as reader:
		col_list = "".join(args.column_list.split()).split(",")
		first_row = next(reader)
		if (not args.ignore_missing):
			for col in col_list:
				if not col in first_row:
					raise ValueError(f"Invalid columns: {col}")	
		columns = [
			i for i, col in enumerate(first_row) if col in col_list
		]
		print(format_row(first_row, max_width, header = True))	
		matches = 0
		for row in reader:
			filtered_row = [row[i] for i in columns]
			for entry in filtered_row:
				if (match(entry, args.match, args.regex, args.ignore_case)):
					print(format_row(row, max_width))
					matches += 1
					break
			if (matches >= args.first):
				return