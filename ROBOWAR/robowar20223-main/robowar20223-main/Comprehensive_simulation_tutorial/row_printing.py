#!/usr/bin/python3

import time

def count_rows(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for row in file)
    except FileNotFoundError:
        return 0

if __name__ == '__main__':
    csv_file_path = 'robot1_positions.csv'  # Replace with your file path

    while True:
        row_count = count_rows(csv_file_path)
        print(f"Number of rows: {row_count}")
        time.sleep(10)  # Wait for 10 seconds
