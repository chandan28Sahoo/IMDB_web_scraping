import json
from pprint import pprint
with open("Task4.json","r") as write_file:
    data_list=json.load(write_file)
    write_file.close()
b=[]
for i in data_list:
    # print(i["director"])
    for j in i["director"]:
        if j not in b:
            b.append(j)
# print(b)
x={}
for i in b:
    c = 0
    # a=[]
    for j in data_list:
        for k in j["director"]:
            if k in i:
                c+=1
    x[i]=c
print(x)

# with open("Task7.json","w") as write_file:
#     json.dump(x,write_file,indent=2)
#     write_file.close()