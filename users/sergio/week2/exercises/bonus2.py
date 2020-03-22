import argparse
import csv
from pathlib import Path
import sys
import argparse


def transform_csv(*args, **kwargs):


    read_csv_path = Path('data', args[0])
    write_csv_path = Path('data', args[1])
    with open(read_csv_path, 'r') as file_to_read:
        dialect = csv.Sniffer().sniff(file_to_read.read(1024))
        file_to_read.seek(0)
        reader = csv.reader(file_to_read, dialect)

        with open(write_csv_path, 'w') as file_to_write:
            writer = csv.writer(file_to_write, delimiter=',', lineterminator='\n')
            if not kwargs.get('header', True):
                next(reader)
            for row_readed in reader:
                writer.writerow(row_readed)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('readfile', default='cars-original.csv')
    parser.add_argument('writefile', default='csv-output.csv')
    args = parser.parse_args()

    transform_csv(args.readfile, args.writefile)
    print(open(Path('data', sys.argv[2])).read())
