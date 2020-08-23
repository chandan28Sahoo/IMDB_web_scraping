import json
from pprint import pprint
with open("Task4.json","r") as write_file:
    data=json.load(write_file)
    write_file.close()
a=[]
for i in data:
    for j in i["genre"]:
        if j not in a:
            a.append(j)
print(a)
data1={}
for x in a:
   count=0
   for i in data:
       for j,k in i.items():
           if j =="genre":
               for l in k:
                   if l in x:
                       count+=1
           data1[x]=count
print(data1)

with open("Task11.json","w") as write_file:
    json.dump(data1,write_file,indent=2)