import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles_list = [title.getText() for title in titles]
titles_list.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in titles_list:
        file.write(f"{movie}\n")

