
import argparse
import csv
from pathlib import Path

def custom_read_csv(datapath):

    with open(datapath, 'rt') as f:
        reader = csv.reader(f, dialect='pipes')
        for row in reader:
            print(row)

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--csv-file', default='cars-original.csv')
    args = parser.parse_args()


    csv.register_dialect('pipes', delimiter='|')

    datapath = Path('..', 'data', args.csv_file)
    print(custom_read_csv(datapath))

