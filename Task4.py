from web_scraping import *
from bs4 import BeautifulSoup
import requests,json,os
from pprint import pprint

def movie_detailss(url):
    a=requests.get(url).text
    soup=BeautifulSoup(a,"html.parser")
    ################
    div_=soup.find("div",id="wrapper")
    title_=div_.find("h1").text
    movie_name=""
    for i in title_:
        if "("  in i:
            break
        else:
            movie_name+=i.strip()
    ################
    bio=div_.find("div",class_="summary_text").text.strip()
    ###############################
    runtime =div_.find("div",class_="subtext")
    runtime=runtime.find("time").text.strip()
    ########################
    a=[]
    div1_=div_.find("div",class_="subtext")
    genre=div1_.find_all("a")
    for i in genre:
        a.append(i.text)
        genres=a[:-1]
    # # # ##################
    div1_=soup.find("div",id="titleDetails")
    # print(div1_)
    s_div=div1_.find_all("div",class_="txt-block")
    for i in s_div:
       if "Country:" in i.text:
            country=(i.find("a").text)

    # ###################
    languages=[]
    for i in s_div:
        if "Language:" in i.text:
            a=i.find_all("a")
            for i in a:
                languages.append(i.text)

    #############################################
    directors = []
    director = soup.find("div",class_="credit_summary_item")
    a = director.find_all('a')
    for j in a:
        directors.append(j.text)
    #######################
    poster_image_url=soup.find("div",class_="title-overview")
    p=poster_image_url.find("div",class_="poster")
    p=p.find("a")
    poster_image_url=p.find("img")["src"]
    ##############################
    movie_details={}
    movie_details["Name"]=movie_name
    movie_details["country"]=country
    movie_details["director"]=directors
    movie_details["language"]=languages
    movie_details["poster_image_url"]=poster_image_url
    movie_details["bio"]=bio
    movie_details["runtime"]=runtime
    movie_details["genre"]=genres
    a=movie_details.copy()
    return a
count=1
dataList=[]
for i in data:
    # print(data[0]["url"])
    # print(count)
    # pprint(i['url'])
    b = i["url"]
    a = ""
    for j in b[21:]:
        if "/" in j:
            continue
        else:
            a += j
    file_name1 = (a + ".json")

    data1=movie_detailss(i['url'])
    # dataList.append(data1)
    # count += 1
    # if count==5:
    #     break
    #
    # # pprint(data)
    # pprint(data1)



with open("Task04.json", "w+") as write_file:
    json.dump(data1, write_file, indent=2)
    write_file.close()




