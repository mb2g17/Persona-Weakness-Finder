from bs4 import BeautifulSoup


class Page:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_weaknesses(self):
        # Finds h2 with 'Stats' in it
        h2 = self.soup.find(lambda tag: tag.name == 'h2' and 'Stats' in tag.text)

        # Iterates through h2 siblings
        siblings = h2.next_siblings
        h3_name = ""
        h4_name = ""
        tab_name = ""
        weaknesses = []

        for sibling in siblings:
            if sibling.name == 'h2':
                break

            if sibling.name == 'h3':
                h3_name = sibling.text.replace("Edit", "")
            if sibling.name == 'h4':
                h4_name = sibling.text.replace("Edit", "")

            if sibling.name == 'div' and "tabber" in sibling.attrs['class']:
                tabs = sibling.find_all("div", {"class": "tabbertab"})
                for tab in tabs:
                    tab_name = tab.attrs['title']
                    table = tab.find("table")
                    weaknesses.append({
                        "name": h3_name + " - " + h4_name + " - " + tab_name,
                        "weakness": list(self.get_weaknesses_from_table(table))
                    })

        return weaknesses

    def get_weaknesses_from_table(self, table):
        weakness_table = table.find_all("table", {
            "class": "customtable"
        })[1]
        weakness_row = weakness_table.find_all("tr")[1]
        weaknesses = map(lambda td: td.text.strip(), weakness_row.find_all("td"))

        return weaknesses
