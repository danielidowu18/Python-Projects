from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2"

with requests.get(url=URL) as response:
    contents = response.text
    
soup = BeautifulSoup(markup=contents, features="html.parser")
titles_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
titles = reversed([tag.get_text().split(") ")[1] for tag in titles_tags])

ordered_titles = []
n = 0
for title in titles:
    n += 1
    num_titile = f"{n}. {title}"
    ordered_titles.append(num_titile)

file = open("100 Greatest Movies/movies.txt", "w")
for ordered_title in ordered_titles:
    file.write(f"{ordered_title}\n")
