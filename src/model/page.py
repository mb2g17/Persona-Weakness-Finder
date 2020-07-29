from typing import List, Dict
from bs4 import BeautifulSoup
from model.shadow import Shadow
from soup_parser import parse_soup


class Page:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.shadow: Dict[str, Shadow] = {}

        shadows = parse_soup(self.soup)

        for shadow in shadows:
            variation = shadow.get_variation()
            self.shadow[variation] = shadow

    def get_variations(self) -> List[str]:
        return list(self.shadow.keys())

    def get_shadow(self, variation: str) -> Shadow:
        return self.shadow[variation]
