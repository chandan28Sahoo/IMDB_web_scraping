import json
from pprint import pprint
with open("Task4.json","r") as write_file:
    data_list=json.load(write_file)

b=[]
for i in data_list:
    for j in i["language"]:
        if j not in b:
            b.append(j)
# print(b)
x={}
for i in b:
    count=0
    for j in data_list:
        for k in j["language"]:
            if k in i:
                count+=1
        x[i]=count
print(x)
with open("Task6.json","w") as write_file:
    json.dump(x,write_file,indent=2)
    write_file.close()