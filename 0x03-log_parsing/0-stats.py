#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys
import signal

"""Initialize variables to store total file size and status code counts."""
total_size = 0
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics:
    
    - Outputs the total file size.
    - Outputs counts for each status code that has been encountered.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) by printing the stats and exiting."""
    print_stats()
    sys.exit(0)

"""Register the signal handler to capture CTRL + C interruptions."""
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        """Increment line count for each line of input and split the line into parts."""
        line_count += 1
        parts = line.split()
        
        """Update total file size by attempting to convert the last item to an integer."""
        try:
            total_size += int(parts[-1])
        except (IndexError, ValueError):
            continue

        """Update status code count if the second-to-last item matches a valid code."""
        try:
            status = parts[-2]
            if status in status_counts:
                status_counts[status] += 1
        except IndexError:
            continue
        
        """Print stats every 10 lines of input."""
        if line_count % 10 == 0:
            print_stats()

    """Print final stats after processing all input."""
    print_stats()

except KeyboardInterrupt:
    """If interrupted by keyboard, print final stats and exit."""
    print_stats()
    sys.exit(0)

