# from Task4scraping import *
import json
from pprint import pprint
with open("Task4.json","r") as write_file:
    data=json.load(write_file)
    write_file.close()


# pprint(data)
languages=[]
for i in data:
    for j in i["language"]:
        if j not in languages:
            languages.append(j)
# print(languages)
directors=[]
for i in data:
    for j in i["director"]:
        # if j not in directors:
        directors.append(j)
# print(directors)
a = {}
for j in range(len(data)):

    for director in directors:
        if director in data[j]["director"]:
            b={}
            count=0
            for language in data[j]["language"]:
                count+=1
                b[language]=count
        a[director]=b
pprint(a)







# for i in directors:



# count=1
# a=[]
# for i in data:
#     print(i)
#     for k,j in i.items():
#         if k == "language":
#             a.append(j)
# print(a)

#   # z=(data[k])
    # print(z)
    # for i in z:
    #     # print(i,end="=")
    #     print(z[i])