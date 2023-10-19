#!/usr/bin/python3
"""
Log parsing

Write a script that reads stdin line by line and computes metrics
"""

import re
import sys


def get_status_code_and_size(line):
    """
    This helper function gets the code and the size of each log line
    """
    # Define the regex pattern to match the status code
    pattern1 = r'"GET /projects/260 HTTP/1.1" (\d+)'

    # Define the regex pattern to match the file size
    pattern2 = r'"GET /projects/260 HTTP/1.1" \d+ (\d+)'

    # Use re.search to find the status code in the log line
    match1 = re.search(pattern1, line)

    # Use re.search to find the file size in the log line
    match2 = re.search(pattern2, line)

    status_code = match1.group(1) if match1 else None

    size = int(match2.group(1)) if match2 else 0

    return status_code, size


def log_parsing():
    """
    Function to perform Log Parsing
    Reads 'stdin' line by line
    """
    codes, counter, sizes = {}, 0, 0

    try:
        for line in sys.stdin:
            counter += 1
            line = line.strip()

            status_code, size = get_status_code_and_size(line)
            if status_code is not None:
                codes[status_code] = codes.get(status_code, 0) + 1
                sizes += size

            if counter % 10 == 0:
                print(f"File size: {sizes}")
                for key in sorted(codes):
                    print(f"{key}: {codes[key]}")

                # Reset the counter, sizes, and codes for the next batch
                counter = 0
                sizes = 0
                codes = {}

    except KeyboardInterrupt:
        # Print the final statistics if a keyboard interruption occurs
        print(f"File size: {sizes}")
        for key in sorted(codes):
            print(f"{key}: {codes[key]}")


if __name__ == "__main__":
    """Call the function to perfom Log Parsing"""
    log_parsing()
