import argparse
import csv
from pathlib import Path
import sys
import argparse


def transform_csv(*args, **kwargs):


    read_csv_path = Path('data', args[0])
    write_csv_path = Path('data', args[1])
    with open(read_csv_path, 'r') as file_to_read:
        reader = csv.reader(file_to_read,
                            quotechar=kwargs['quotechar'],
                            delimiter=kwargs['delimiter'])

        with open(write_csv_path, 'w') as file_to_write:
            writer = csv.writer(file_to_write, delimiter=',', lineterminator='\n')
            if not kwargs.get('header', True):
                next(reader)
            for row_readed in reader:
                writer.writerow(row_readed)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('readfile')
    parser.add_argument('writefile')
    parser.add_argument('-q', '--in-quote', default='"')
    parser.add_argument('-d', '--in-delimiter', default=',')
    args = parser.parse_args()

    transform_csv(args.readfile, args.writefile, header=True, quotechar=args.in_quote, delimiter=args.in_delimiter)
    print(open(Path('data', sys.argv[2])).read())
