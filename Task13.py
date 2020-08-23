import json
from pprint import pprint

with open("Task4.json","r") as write_file:
    data=json.load(write_file)
    write_file.close()

with open("Task12.json", "r") as write_file:
    data1 = json.load(write_file)
    write_file.close()

b={}
a=[]
movie_n_cast=[]

for i in range(len(data)):
    b["cast"] = (data1[i])
    for j in range(len(data1)):
        if i==j:
            movie_n_cast.append(data[i])
            movie_n_cast.append(b.copy())
pprint(movie_n_cast)
# data2=movie_n_cast
# pprint(data2)

# with open("Task13.json","w+") as write_file:
#     json.dump(movie_n_cast,write_file,indent=2)
#     write_file.close()



