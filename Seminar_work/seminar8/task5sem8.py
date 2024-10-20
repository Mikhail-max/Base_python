import json
import os
import pickle

for el in os.listdir():
    if el.endswith('json'):
        with open(el, "r", encoding="utf-8") as j:
            res = json.load(j)
        path = ''.join(el.split(".")[:-1]) + ".pickle"
        with open(path,'wb') as f:
            pickle.dump(res,f)