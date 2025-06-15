import csv
import click
import os


def parse_file(path: str, expected_schema: list[str] | None = None) -> dict[str, list]:
    if not os.path.isfile(path):
        raise click.exceptions.FileError(filename=path, hint=f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    try:
        csv_reader = csv.reader(data.splitlines())
    except csv.Error as e:
        raise click.exceptions.FileError(
            filename=path, hint=f"Error reading CSV file {path}: {e}"
        )
    headers = next(csv_reader)
    if expected_schema and headers != expected_schema:
        raise click.exceptions.FileError(
            filename=path,
            hint=f"Schema mismatch in {path}. Expected: {expected_schema}, Found: {headers}",
        )
    final_data: dict[str, list] = {el: [] for el in headers}
    for row in csv_reader:
        if len(row) != len(headers):
            raise click.exceptions.FileError(
                filename=path,
                hint=f"Row length mismatch in {path}. Expected {len(headers)}, got {len(row)}.",
            )
        for header, value in zip(headers, row):
            final_data[header].append(value)

    return final_data
