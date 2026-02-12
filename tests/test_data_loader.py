import inspect
from argparse import ArgumentParser
import cli.parser as parser_builder
import cli.data_loader as data_loader
import pytest
import os
import csv
import collections.abc 

test_dir = os.path.dirname(__file__)

def right_path(file):
	return os.path.join(test_dir, "testdata", file)

csvFile = right_path("test.csv")
emptyFile = right_path("empty.csv")
malformedFile = right_path("bad_parse.csv")

def test_reader_is_returned():
	with data_loader.load_data(csvFile, ",") as reader:
		assert isinstance(reader, collections.abc.Iterator)

def test_handle_bad_file(capfd):
	with pytest.raises(FileNotFoundError):
		with data_loader.load_data("blorpp", ",") as reader:	
			pass

def test_handle_empty_file(capfd):
	with pytest.raises(ValueError):
		with data_loader.load_data(emptyFile, ",") as reader:
			pass

def test_handle_malformed_file(capfd):
	with pytest.raises(ValueError):
		with data_loader.load_data(malformedFile, ",") as reader:
			pass

