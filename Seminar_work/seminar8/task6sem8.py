import pickle
import csv

with open('task8_2.pickle', 'rb') as p:
    data = pickle.load(p)
    print(data)

with open("new_c.csv", "w", encoding="utf-8", newline='') as c:
    writer = csv.DictWriter(c, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)