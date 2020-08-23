import requests,json
from bs4 import BeautifulSoup
from pprint import pprint

with open("web.json","r") as write_file:
    data=json.load(write_file)
    write_file.close()

def scrape_movie_cast(url):
    a=requests.get(url).text
    soup=BeautifulSoup(a,"html.parser")

    div_sub=soup.find("div",id="content-2-wide")
    sub=div_sub.find("table",class_="cast_list")
    # print(sub)
    data_={}
    a=[]
    imdb=sub.find_all("td",class_="")
    for cast in imdb:
        cast_id=cast.find("a").get("href")[6:15]
        cast_name=cast.find("a").text.strip()

        data_["cast_id"]=cast_id
        data_["cast_name"]=cast_name
        a.append(data_.copy())
    return a

cast_list=[]
count=1
for i in data:
    # print(count)
    data_list1=scrape_movie_cast(i["url"])
    cast_list.append(data_list1)
    print(cast_list)
    # count+=1
    # if count==5:
    #     break
##########################

with open("Task121.json","w") as write_file:
    json.dump(cast_list,write_file,indent=2)
    write_file.close()

# print(i["url"])