import json
from pprint import pprint
# n = {'id_name' : 'Rajesh Khanna','id_name':'Amitav Bachahan'}

with open("Task12.json","r") as write_file:
    data_cast=json.load(write_file)
actor_id_={}
for i in data_cast:

    co_actor1={}
    sub_actor = {}
    c=0
    for j in range(len(i)-1):
        c+=1
        actor_id=(i[j]['cast_id'])
        actor_name = i[j]['cast_name']
        co_actor_id=i[j+1]['cast_id']
        co_actor_name = i[j + 1]['cast_name']
        co_actor1["imdb_id"]=co_actor_id
        co_actor1["co_actor_name"]=co_actor_name


        actor_name1 = {}

        count=0
        a = []
        for k in data_cast:
            if i[j] in k:
                if i[j+1] in k:
                    count+=1



        co_actor1["num_of_movie"] = count
        a.append(co_actor1.copy())
        actor_name1["Name"] = actor_name
        actor_name1["frequent_co_actor"]=a
        actor_id_[actor_id]=actor_name1


pprint(actor_id_)


# with open("Task14.json","w+") as write_file:
#     json.dump(actor_id_,write_file,indent=2)
#     write_file.close()