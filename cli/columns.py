from .data_loader import load_data
from .formatter import format_row
from .search_utils import match

def columns_command(args):
	max_width = 15

	try:
		with load_data(args.file, args.delimiter) as reader:
			first_row = next(reader)
			col_counts = [0] * len(first_row)
			for row in reader:
				for index, entry in enumerate(row):
					if entry:
						col_counts[index]+=1
			col_summary = [""] * len(col_counts)
			for index, entry in enumerate(first_row):
				entry += f" ({col_counts[index]})"
				col_summary[index] = entry

			print(format_row(col_summary, max_width, header=True))


	except Exception:
		raise