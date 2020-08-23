import requests,json
with open("web.json", "r") as write_file:
    data_=json.load(write_file)
    write_file.close()

# for j in data_:
for i in data_:
    b=i["url"]
    a=""
for j in b[21:]:
    if "/" in j:
        continue
    else:
        a+=j
file_name=(a+".json")

with open("file_name","w+") as write_file:
    json.dumps(write_file)
