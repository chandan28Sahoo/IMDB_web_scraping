import json
from pprint import pprint
with open("Task4.json","r") as write_file:
    data_list=json.load(write_file)
b=[]
for i in data_list[:10]:
    b.append(i)

with open("Task5.json","w") as write_file:
    json.dump(b,write_file,indent=2)
    write_file.close()

