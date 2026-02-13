import inspect
from argparse import ArgumentParser
import cli.parser as parser_builder
import pytest

# helper
def assert_parse_error(args, expected_message, capfd):
    parser = parser_builder.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(args)
    err = capfd.readouterr().err
    assert expected_message in err

# global
def test_cli_requires_command(capfd):
    assert_parse_error([], "required: command", capfd)

def test_global_no_header_flag():
    parser = parser_builder.build_parser()
    args = parser.parse_args(['--no-header', 'columns' ,'file'])
    assert args.no_header is True

def test_global_delimiter_option():
    parser = parser_builder.build_parser()
    args = parser.parse_args(['--delimiter', ',' , 'columns', 'file'])
    assert args.delimiter is ','

def test_columns_requires_file_value(capfd):
    assert_parse_error(['columns'], "the following arguments are required: file", capfd)

# select - parse errors
def test_select_requires_match_value(capfd):
    assert_parse_error(['select'], "the following arguments are required: column_list", capfd)

# select - flags / options
def test_select_ignore_missing_flag():
    parser = parser_builder.build_parser()
    args = parser.parse_args(['select', 'cols', '--ignore-missing', 'table'])
    assert args.ignore_missing is True

def test_select_columns_arg():
    parser = parser_builder.build_parser()
    args = parser.parse_args(['select', 'cols', 'table'])
    assert args.column_list is 'cols'

# filter - parse errors
def test_filter_requires_value(capfd):
    assert_parse_error(['filter'], "the following arguments are required: file", capfd)

def test_filter_requires_column_option(capfd):
    assert_parse_error(['filter', '--column'], "--column: expected one argument", capfd)

# filter - flags
def test_filter_regex_flag(capfd):
    parser = parser_builder.build_parser()
    args = parser.parse_args(['filter', '--regex', 'table'])
    assert args.regex is True

def test_filter_ignore_case_flag(capfd):
    parser = parser_builder.build_parser()
    args = parser.parse_args(['filter', '--ignore-case', 'table'])
    assert args.ignore_case is True

def test_filter_column_flag(capfd):
    parser = parser_builder.build_parser()
    args = parser.parse_args(['filter', '--column', 'cols', 'table'])
    assert args.column is 'cols'

def test_filter_firstN_flag(capfd):
    parser = parser_builder.build_parser()
    args = parser.parse_args(['filter', '--first', '5' ,'table'])
    assert args.first is '5'