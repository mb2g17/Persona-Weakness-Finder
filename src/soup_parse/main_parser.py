from typing import List, Tuple, Optional
from bs4 import BeautifulSoup

from model.shadow import Shadow
from soup_parse.table_parser import parse_table
from soup_parse.variation_factory import VariationFactory


def parse(soup: BeautifulSoup) -> List[Shadow]:
    # Finds h2 with 'Stats' in it
    h2 = soup.find(lambda tag: tag.name == 'h2' and 'Stats' in tag.text)

    # If there is no h2, throw error
    if h2 is None:
        raise Exception("No h2 tag found")

    # Iterates through h2 siblings
    siblings = h2.next_siblings
    variation_factory = VariationFactory()
    shadows: List[Shadow] = []

    for sibling in siblings:
        if sibling.name == 'h2':
            break

        elif sibling.name == 'h3':
            variation_factory.h3_name = sibling.text.replace("Edit", "")

        elif sibling.name == 'h4':
            variation_factory.h4_name = sibling.text.replace("Edit", "")

        # A weakness table with tabs
        elif sibling.name == 'div' and 'tabber' in sibling.attrs['class']:

            tables = __get_tables_from_tabber__(sibling)
            for (tab_name, table) in tables:

                variation_factory.tab_name = tab_name

                shadow = parse_table(table, variation_factory)

                if shadow is not None:
                    shadows.append(shadow)

            # Reset tab name
            variation_factory.tab_name = ""

        # A weakness table with no tabs
        elif sibling.name == 'table':

            shadow = parse_table(sibling, variation_factory)

            if shadow is not None:
                shadows.append(shadow)

    return shadows


def __get_tables_from_tabber__(tabber) -> List[Tuple[str, any]]:
    tables = []

    # Iterates through all tabs
    tabs = tabber.find_all("div", {"class": "tabbertab"})
    for tab in tabs:

        # Fetch table from this tab
        tab_name = tab.attrs['title']
        table = tab.find("table")

        tables.append((tab_name, table))

    return tables
