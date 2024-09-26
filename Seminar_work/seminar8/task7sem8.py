import csv
import pickle

with open("new_c.csv", "r", encoding="utf-8") as c:
    reader = csv.reader(c)
    data = pickle.dumps(list(reader))
    print(pickle.loads(data))

# Output:   [['level', 'id', 'name'],
#  ['4', '002', 'Петя'],
#  ['4', '002', 'Петя'],
#  ['4', '002', 'Петя'],
#  ['4', '002', 'Петя'],
#  ['4', '002', 'Петя']]