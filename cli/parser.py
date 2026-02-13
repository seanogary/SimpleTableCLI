from argparse import ArgumentParser, FileType
from .columns import columns_command
from .select import select_command

def build_parser():
	parser = ArgumentParser(
		prog="simple-cli",
		description="This is a simple CLI tool that supports basic CSV reading and transformation.",
		epilog="Godspeed."
	)

	parser.add_argument("-nh", "--no-header", action="store_true", help="specifies presence of header")
	parser.add_argument("-d", "--delimiter", type=str, help="delimit", default=",")

	subparsers = parser.add_subparsers(dest="command", required=True)

	# columns command
	columns_parser = subparsers.add_parser("columns", help="columns")

	# select command
	select_parser = subparsers.add_parser("select", help="select")
	select_parser.add_argument("column_list", type=str, help="cols")
	select_parser.add_argument("-im", "--ignore-missing", action="store_true")

	# filter command
	filter_parser = subparsers.add_parser("filter", help="filter")
	filter_parser.add_argument("--column", help="cols")
	filter_parser.add_argument("--regex",  action="store_true", help="regex")
	filter_parser.add_argument("--ignore-case", action="store_true")
	filter_parser.add_argument("--first", help="specify number of cols to match")

	def add_input_file_argument(command_parser):
		command_parser.add_argument("file", type=str, help="file")

	add_input_file_argument(columns_parser)
	add_input_file_argument(select_parser)
	add_input_file_argument(filter_parser)


	def select_handler(args):
		print(args)

	def filter_handler(args):
		print(args)

	# command handlder dispatcher
	select_parser.set_defaults(func=select_handler)
	filter_parser.set_defaults(func=filter_handler)

	return parser

if __name__ == "__main__":
	parser = build_parser()
	args = parser.parse_args(['columns', '--match', '', '--regex', 'test_regex.csv'])
	args.func(args)

def dispatch(args):
	if (args.command == 'columns'):
		try:
			columns_command(args)
		except Exception as e:
			print(f"Error: {e}")
	if (args.command == 'select'):
			select_command(args)

