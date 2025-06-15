import pytest
import os
from src.services.files import parse_file
import click
from unittest import mock


def test_parse_file_success(tmp_path):
    csv_content = "a,b\n1,2\n3,4"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    with mock.patch("click.echo"):
        result = parse_file(str(file_path), expected_schema=["a", "b"])
    assert result == {"a": ["1", "3"], "b": ["2", "4"]}


def test_parse_file_file_not_found():
    with mock.patch("click.echo"):
        with pytest.raises(click.exceptions.FileError):
            parse_file("nonexistent.csv")


def test_parse_file_schema_mismatch(tmp_path):
    csv_content = "x,y\n1,2"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    with mock.patch("click.echo"):
        with pytest.raises(click.exceptions.FileError) as excinfo:
            parse_file(str(file_path), expected_schema=["a", "b"])
        assert "Schema mismatch" in str(excinfo.value)


def test_parse_file_row_length_mismatch(tmp_path):
    csv_content = "a,b\n1"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    with mock.patch("click.echo"):
        with pytest.raises(click.exceptions.FileError) as excinfo:
            parse_file(str(file_path), expected_schema=["a", "b"])
        assert "Row length mismatch" in str(excinfo.value)


def test_parse_file_csv_error(tmp_path):
    # Malformed CSV: unclosed quote
    csv_content = 'a,b\n"1,2\n3,4'
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    with mock.patch("click.echo"):
        with pytest.raises(click.exceptions.FileError) as excinfo:
            parse_file(str(file_path), expected_schema=["a", "b"])
        assert "Error reading CSV file" in str(excinfo.value)
