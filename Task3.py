from web_scraping import data1
import pprint,json
years=[]
data3={}

for i in data1:
    decad=int(i)-(int(i)%10)
    if decad not in years:
        years.append(decad)
        years.sort()
# print(years)
for j in years:
    a=[]
    for i in data1:
        for k in data1[i]:
            if k["year"]<=str(j+10) and k["year"]>=str(j):
                a.append(k)
        data3[j]=a
# pprint.pprint(data3)

with open("TASK3.json","w") as write_file:
    json.dump(data3,write_file,indent=2)
    write_file.close()