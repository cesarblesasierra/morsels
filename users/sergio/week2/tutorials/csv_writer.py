
import argparse
import csv
from pathlib import Path


if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--csv-file', default='csv-output.csv')
    args = parser.parse_args()


    unicode_chars = 'å∫ç'
    datapath = Path('..','data', args.csv_file)
    with open(datapath, 'wt', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\n', quotechar='|')
        writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
        for i in range(3):
            row = (
                i + 1,
                chr(ord('a') + i),
                '08/{:02d}/07'.format(i + 1),
                unicode_chars[i],
            )
            writer.writerow(row)

    print(open(datapath, 'rt').read())

    csv.list_dialects()

