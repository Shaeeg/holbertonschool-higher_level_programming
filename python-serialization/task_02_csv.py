#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write it to data.json."""
    try:
        with open(csv_filename, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f)
        return True
    except FileNotFoundError:
        return False
