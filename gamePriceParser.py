import requests
from bs4 import BeautifulSoup

l = {}
s = []
t = []
discount = False
def gamePrice(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in soup.find_all("div", class_="game_purchase_action"):
        if i.find("div", class_="game_purchase_price price") and i.parent.find("div", class_="game_area_purchase_platform"):
            l[i.parent.find("h1").contents[0].string.strip()] = i.find("div", class_="game_purchase_price price").string.strip()
            s.append(0)
        elif i.find("div", class_="discount_final_price") and i.parent.find("div", class_="game_area_purchase_platform"):
            discount = True
            l[i.parent.find("h1").contents[0].string.strip()] = i.find("div", class_="discount_final_price").string.strip()
            if i.find("div", class_="discount_pct"):
                s.append(i.find("div", class_="discount_pct").contents[0].string.strip())
            else:
                s.append(i.find("div", class_="bundle_base_discount").contents[0].string.strip())

    return l, s, discount





# print(gamePrice("https://store.steampowered.com/app/1551360/Forza_Horizon_5/"))

# efnffff

# print(gamePrice("https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/"))

# print(gamePrice("https://store.steampowered.com/app/39210/FINAL_FANTASY_XIV_Online/"))

# print(gamePrice("https://store.steampowered.com/app/1151640/Horizon_Zero_Dawn_Complete_Edition/"))

# print(gamePrice("https://store.steampowered.com/app/534380/Dying_Light_2_Stay_Human/"))

# print(gamePrice("https://store.steampowered.com/app/47890/The_Sims_3/"))

# print(gamePrice("https://store.steampowered.com/app/617290/Remnant_From_the_Ashes/"))




















