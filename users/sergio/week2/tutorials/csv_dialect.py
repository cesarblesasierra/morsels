import csv
from pathlib import Path

csv.register_dialect('pipes', delimiter='|')
readpath = Path('..', 'data', 'csv_dialect.pipe')
with open(readpath, mode='r') as file_to_read:
    reader = csv.reader(file_to_read, dialect='pipes')
    for row in reader:
        print(row)


TEMPLATE = '''\
Dialect: "{name}"

  delimiter   = {dl!r:<6}    skipinitialspace = {si!r}
  doublequote = {dq!r:<6}    quoting          = {qu}
  quotechar   = {qc!r:<6}    lineterminator   = {lt!r}
  escapechar  = {ec!r:<6}
'''



