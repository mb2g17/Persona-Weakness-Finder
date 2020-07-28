from typing import List, Tuple
from bs4 import BeautifulSoup
from model.shadow import Shadow


def parse_soup(soup: BeautifulSoup) -> List[Tuple[str, Shadow]]:
    """
    :return: List of tuples [(variation, shadow)]
    """
    # Finds h2 with 'Stats' in it
    h2 = soup.find(lambda tag: tag.name == 'h2' and 'Stats' in tag.text)

    # Iterates through h2 siblings
    siblings = h2.next_siblings
    h3_name = ""
    h4_name = ""
    shadows: List[(str, Shadow)] = []

    for sibling in siblings:
        if sibling.name == 'h2' or sibling.name == 'p':
            break

        if sibling.name == 'h3':
            h3_name = sibling.text.replace("Edit", "")
        if sibling.name == 'h4':
            h4_name = sibling.text.replace("Edit", "")

        # A weakness table with tabs
        if sibling.name == 'div' and "tabber" in sibling.attrs['class']:

            tables = __get_tables_from_tabber__(sibling)
            for (tab_name, table) in tables:
                full_variation = __create_full_variation_name__(h3_name, h4_name, tab_name)
                shadow = __create_shadow_from_table__(table)

                shadows.append((full_variation, shadow))

        # A weakness table with no tabs
        if sibling.name == 'table':
            shadow = __create_shadow_from_table__(sibling)
            shadows.append(("No variation", shadow))

    return shadows


def __get_tables_from_tabber__(tabber) -> List[Tuple[str, any]]:
    tables = []

    tabs = tabber.find_all("div", {"class": "tabbertab"})
    for tab in tabs:
        tab_name = tab.attrs['title']
        table = tab.find("table")

        tables.append((tab_name, table))

    return tables


def __create_full_variation_name__(h3_name: str, h4_name: str, tab_name: str) -> str:
    names = []
    if h3_name != "":
        names.append(h3_name)
    if h4_name != "":
        names.append(h4_name)
    if tab_name != "":
        names.append(tab_name)
    return " - ".join(names)


def __create_shadow_from_table__(table) -> Shadow:
    # Create shadow
    shadow = Shadow()

    # Fill shadow with weaknesses
    weakness_tuples = __get_weaknesses_from_table__(table)
    for (weakness_type, weakness_status) in weakness_tuples:
        shadow.add_weakness(weakness_type, weakness_status)

    # Return shadow
    return shadow


def __get_weaknesses_from_table__(table) -> List[Tuple[str, str]]:
    """
    :return: List of weakness tuples [(type, status)]
    """
    weakness_table = table.find_all("table", {
        "class": "customtable"
    })[1]

    rows = weakness_table.find_all("tr")
    type_row = rows[0].find_all("th")
    status_row = rows[1].find_all("td")

    return list(zip(
        map(lambda row: row.text.strip(), type_row),
        map(lambda row: row.text.strip(), status_row)
    ))