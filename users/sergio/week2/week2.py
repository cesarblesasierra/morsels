import argparse
import csv
from pathlib import Path
import sys


def custom_read_csv(*args, **kwargs):
    read_csv_path = Path('data', args[0])
    with open(read_csv_path, 'r') as file_to_read:
        reader = csv.reader(file_to_read, delimiter=',')
        if not kwargs.get('header', True):
            next(reader)
        for row in reader:
            print(row)



def transform_csv(*args, **kwargs):

    read_csv_path = Path('data', args[0])
    write_csv_path = Path('data', args[1])
    with open(read_csv_path, 'r') as file_to_read:
        reader = csv.reader(file_to_read, delimiter='|')
        with open(write_csv_path, 'w') as file_to_write:
            writer = csv.writer(file_to_write, delimiter=',')
            if not kwargs.get('header', True):
                next(reader)
            for row_readed in reader:
                writer.writerow(row_readed)




if __name__ == "__main__":
    transform_csv(sys.argv[1], sys.argv[2], header=True)
    custom_read_csv(sys.argv[2], header=True)
