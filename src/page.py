from bs4 import BeautifulSoup


class Page:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_games(self):
        # Finds h2 with 'Stats' in it
        h2 = self.soup.find(lambda tag: tag.name == 'h2' and 'Stats' in tag.text)

        # Iterates through h2 siblings
        siblings = h2.next_siblings
        games = []
        for sibling in siblings:
            if sibling.name == 'h3':
                name = sibling.text.replace("Edit", "")
                games.append(name)

        return games
