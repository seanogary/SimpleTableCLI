from .data_loader import load_data
from .formatter import format_row
from .search_utils import match

def columns_command(args):
	max_width = 15

	try:
		with load_data(args.file, args.delimiter) as reader:
			first_row = next(reader)
			columns = [
				i for i, col in enumerate(first_row) if match(col, args.match, args.regex)
			]	
			print(format_row(first_row, max_width, header = True))	
			for row in reader:
				filtered_row = [row[i] for i in columns]
				print(format_row(filtered_row, max_width))

	except Exception:
		raise