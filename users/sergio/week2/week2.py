import argparse
import csv
from pathlib import Path
import sys

def custom_read_csv(*args):

    pathtocsv = Path('data', args[0])
    l = []
    csv.register_dialect('pipes', delimiter='|')
    with open(pathtocsv, 'rt') as f:
        reader = csv.reader(f, dialect='pipes')
        for row in reader:
            l.append(row)
    return l


def custom_write_csv(*args):
    path_to_csv = Path('data', args[0])
    with open(path_to_csv, 'wt') as f:
        writer = csv.writer(f, lineterminator='\n')
        for row in args[1]:
            writer.writerow(row)



if __name__ == "__main__":

    list_csv_file = custom_read_csv(sys.argv[1])
    custom_write_csv(sys.argv[2], list_csv_file)

    print('Original:')
    print(list_csv_file)
    print('#################')
    print('Formatted')
    print("\n".join(str(row) for row in custom_read_csv(sys.argv[2])))
