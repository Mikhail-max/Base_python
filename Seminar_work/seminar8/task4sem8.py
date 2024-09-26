import csv
import json

with open('task8_2.csv', encoding="utf-8") as f:
    fr = csv.reader(f)
    res = list(fr)
    print(res)
    for i in range(1, len(res)):
        cur_id = res[i][1]
        res[i][1] = f"{cur_id.zfill(10)}"
        res[i][2] = res[i][2].title()
        res[i].append(hash(res[i][2]))
    res[0].append('hash')

with open('new_json.json', "w", encoding="utf-8") as j:
    json.dump(res, j, ensure_ascii=False)