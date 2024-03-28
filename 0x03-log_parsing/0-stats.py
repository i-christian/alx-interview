#!/usr/bin/python3
""".0-stats.py"""
import sys
from typing import Dict


def print_statistics(status_codes: Dict[str, int], total_file_size: int) -> None:
    """Print statistics of status codes and total file size.

    Args:
        status_codes (dict): Dictionary containing status codes and their counts.
        total_file_size (int): Total size of the file.
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print(f"{code}: {count}")


total_file_size: int = 0
status_codes: Dict[str, int] = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
counter: int = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Trim and split the line
        parsed_line = parsed_line[::-1]  # Reverse the list to get status code and file size

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # Accumulate file size
                status_code = parsed_line[1]  # Extract status code

                if status_code in status_codes:
                    status_codes[status_code] += 1  # Increment status code count

            if counter == 10:
                print_statistics(status_codes, total_file_size)
                counter = 0

finally:
    print_statistics(status_codes, total_file_size)
