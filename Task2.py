###TASK-2
from web_scraping import data
import pprint
import json
y19_movie=[]
years=[]

data1={}
for i in data:
    if i["year"] not in years:
        years.append(i["year"])
#
for j in years:
    x = []
    for k in data:
        if j==k["year"]:
            x.append(k)
    data1[j]=x
# pprint.pprint(data1)
with open("TASK_2.json","w") as write_file:
    json.dump(data1,write_file,indent=2)
    write_file.close()



with open("TASK_2.json","r") as write_file:
    json.load(write_file)
    write_file.close()



