import inspect
from argparse import ArgumentParser
import cli.parser as parser_builder
import pytest

def assert_parse_error(args, expected_message, capfd):
    parser = parser_builder.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(args)
    err = capfd.readouterr().err
    assert expected_message in err

def test_cli_requires_command(capfd):
    assert_parse_error([], "required: command", capfd)

def test_columns_requires_match(capfd):
    assert_parse_error(['columns', 'v'], "required: -m/--match", capfd)

def test_columns_requires_match_value(capfd):
    assert_parse_error(['columns', '--match'], "-m/--match: expected one argument", capfd)

def test_columns_requires_file_value(capfd):
    assert_parse_error(['columns', '--match', 'regex'], "the following arguments are required: value", capfd)

