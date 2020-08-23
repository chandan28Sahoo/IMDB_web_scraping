#TSAK-1#
import requests,json,string
from bs4 import BeautifulSoup
import os
a=requests.get("https://www.imdb.com/india/top-rated-indian-movies/").text
# print(a)

###################333
soup=BeautifulSoup(a,"html.parser")
# print(soup)
def scrsp_top_list():

    div_=soup.find("div",class_="lister")
    tbody=div_.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")

    movie_url=[]
    movie_name=[]
    movie_rank=[]
    year_of_realease=[]
    movie_rating=[]

    for tr in trs:
        rank=tr.find("td",class_="titleColumn").text.split()[0][:-1]
        movie_rank.append(int(rank))
        # print(movie_rank)

        #get anchor-.a
        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)



        year=tr.find("td",class_="titleColumn").span.get_text()
        a=""
        for i in year:
            if i in string.digits:
                a+=i

        year_of_realease.append(a)
    # return year_of_realease


        rating=tr.find("td",class_="ratingColumn imdbRating").text.strip()
        # return rating
        movie_rating.append(rating)
        # print(movie_rating)


        url=tr.find("td",class_="titleColumn").a["href"]
        # a_tag = url.find("a")["href"]
        link="https://www.imdb.com/"+(url)
        movie_url.append(link)

        top_movie=[]
        details={"rank":"","title":"","year":"","rating":"","url":""}

        for i in range(0,len(movie_rank)):
            details["rank"]=int(movie_rank[i])
            details["title"]=str(movie_name[i])
            details["year"]=(year_of_realease[i])
            details["rating"]=float(movie_rating[i])
            details["url"]=movie_url[i]
            top_movie.append(details.copy())

    return top_movie

data=scrsp_top_list()

with open("web.json","w") as write_file:
    json.dump(data,write_file,indent=2)
    write_file.close()

# with open("web.json","r") as write_file:
#     json.load(write_file)
#     write_file.close()

