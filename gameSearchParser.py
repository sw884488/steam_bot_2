import requests
import gameSearchAnswer as gsa
from bs4 import BeautifulSoup

def gameSearch(request):
    gameSearchResult = {}
    response = requests.get("https://store.steampowered.com/search/?term=" + str(request))
    soup = BeautifulSoup(response.text, 'html.parser')
    counter = 0
    for i in soup.find_all("a", class_="search_result_row ds_collapse_flag"):
        if counter != 10:
            gameSearchResult[i.find("span", class_="title").string] = i["href"]
            counter += 1
        else:
            break
    # return gsa.gameSearchAnswer(gameSearchResult)
    return gameSearchResult



