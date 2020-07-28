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
