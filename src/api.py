import requests
from model.page import Page


def get_shadow_page(query: str) -> Page:
    link = search_shadow_url(query)

    # Gets HTML page
    r = requests.get(link)
    return Page(r.text)


def search_shadow_url(query: str) -> str:
    r = requests.get('https://megamitensei.fandom.com/api/v1/Search/List', params={"query": query})

    items = r.json()["items"]

    if len(items) == 0:
        raise Exception("No shadow found")
    else:
        return r.json()["items"][0]["url"]


def search_shadow_id(query: str) -> str:
    r = requests.get('https://megamitensei.fandom.com/api/v1/Search/List', params={"query": query})

    items = r.json()["items"]

    if len(items) == 0:
        raise Exception("No shadow found")
    else:
        return r.json()["items"][0]["id"]


def save_shadow_portrait(query: str) -> bool:
    # Gets shadow id
    shadow_id = search_shadow_id(query)

    # Gets portrait url
    r = requests.get('https://megamitensei.fandom.com/api/v1/Articles/Details', params={"ids": shadow_id})

    portrait_url = r.json()["items"][str(shadow_id)]["thumbnail"]

    if portrait_url is None:
        return False

    # Gets portrait
    r = requests.get(portrait_url)

    # Writes portrait
    file = open("assets/portrait.png", "wb")
    file.write(r.content)
    file.close()

    return True
