# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 07:45:56 2019

Practice for scraping movie data from IMDB search results

@author: Sween
"""

from requests import get
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
#url = 'https://www.imdb.com/search/title?languages=hi&count=250'
#url = 'http://www.imdb.com/search/title?languages=hi&page=1'
#url = 'https://www.imdb.com/title/tt0070947/'
#url = 'https://www.barcindia.co.in/statistic.aspx'

# get function to capture html from url
response = get(url)
#print(response.text[:500])

# parse html into beautiful soup text object
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

# find_all function to extract html div containers w/ class attribute 'lister-item mode-advanced'
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
#print(type(movie_containers))
print(len(movie_containers))

"""
for i in len(movie_containers)):
    name[i] = movie_containers[i].h3.a.text
    date[i] = movie_containers[i].h3.find('span', class_ = 'lister-item-year text-muted unbold')
    runtime[i] = movie_containers[i].p.find('span', class_ = "runtime")
    genre[i] = movie_containers[i].p.find('span', class_ = "genre")
    imdbrating[i] = float(movie_containers[i].find('div', class_ = "inline-block ratings-imdb-rating").text)
"""


# access information about the first movie
first_movie = movie_containers[4]
#print(first_movie)

# acess title information
first_name = first_movie.h3.a.text
print(first_name)

first_date = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
print(first_date.text)

first_runtime = first_movie.p.find('span', class_ = "runtime")
print(first_runtime.text)

#first_genre = string(first_movie.p.find('span', class_ = "genre").text)
first_genre = first_movie.p.find('span', class_ = "genre")
print(first_genre.text)
#print(first_genre)

first_imdbrating = float(first_movie.find('div', class_ = "inline-block ratings-imdb-rating").text)
print(first_imdbrating)

#first_imdb = float(first_movie.strong.text)