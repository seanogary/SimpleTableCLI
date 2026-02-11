import csv
import json
import sys
from contextlib import contextmanager

@contextmanager
def load_data(file, delimiter):
	try:
		with open(file, newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter = delimiter, quotechar='"', skipinitialspace=True)
			# validate csv 
			try:
				first_row = next(reader)
			except StopIteration:
				raise ValueError("CSV file is empty")
			except csv.Error as e:
				raise ValueError(f"CSV Parsing error: {e}")

	except FileNotFoundError: raise
	except PermissionError: raise
	except Exception as e: raise
	
	with open(file, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = delimiter, quotechar='"', skipinitialspace=True)
		yield reader
