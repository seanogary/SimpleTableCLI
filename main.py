from cli.parser import build_parser
from cli.parser import dispatch

def main(argv=None):
	parser = build_parser()
	args = parser.parse_args(argv)
	dispatch(args)


if __name__ == "__main__":
	main()