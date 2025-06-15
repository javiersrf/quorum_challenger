import pytest
import os
from src.services import files
import click
from unittest import mock
from unittest.mock import patch, mock_open


def test_parse_file_success():
    fake_csv = "name,age\nAlice,30\nBob,25"
    expected_output = {"name": ["Alice", "Bob"], "age": ["30", "25"]}

    with (
        patch("src.services.files.os.path.isfile", return_value=True),
        patch("src.services.files.open", mock_open(read_data=fake_csv), create=True),
    ):
        result = files.parse_file("fake/path.csv")
        assert result == expected_output


def test_parse_file_file_not_found():
    with pytest.raises(click.exceptions.FileError):
        files.parse_file("nonexistent.csv")


def test_parse_file_schema_mismatch(tmp_path):
    file_path = tmp_path / "test.csv"
    fake_csv = "name,age\nAlice,30\nBob,25"

    with (
        patch("src.services.files.os.path.isfile", return_value=True),
        patch("src.services.files.open", mock_open(read_data=fake_csv), create=True),
    ):
        with pytest.raises(click.exceptions.FileError) as excinfo:
            files.parse_file(str(file_path), expected_schema=["a", "b"])
    assert "Schema mismatch" in str(excinfo.value)


def test_parse_file_row_length_mismatch(tmp_path):
    file_path = tmp_path / "test.csv"
    fake_csv = "name,age\nAlice,30\nBob,25\nJhon"
    with (
        patch("src.services.files.os.path.isfile", return_value=True),
        patch("src.services.files.open", mock_open(read_data=fake_csv), create=True),
        pytest.raises(click.exceptions.FileError) as excinfo,
    ):
        files.parse_file(str(file_path), expected_schema=["name", "age"])
    assert "Row length mismatch" in str(excinfo.value)


def test_parse_file_csv_not_found(tmp_path):
    file_path = tmp_path / "test.csv"
    fake_csv = 'a,b\n"1,2\n3,4'
    with (
        patch("src.services.files.os.path.isfile", return_value=False),
        patch("src.services.files.open", mock_open(read_data=fake_csv), create=True),
        pytest.raises(click.exceptions.FileError) as excinfo,
    ):
        files.parse_file(str(file_path), expected_schema=["a", "b"])
    assert "File not found" in str(excinfo.value)
