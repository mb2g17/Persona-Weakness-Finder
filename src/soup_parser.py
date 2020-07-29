from typing import List, Tuple, Optional
from bs4 import BeautifulSoup
from model.shadow import Shadow


def parse_soup(soup: BeautifulSoup) -> List[Shadow]:
    # Finds h2 with 'Stats' in it
    h2 = soup.find(lambda tag: tag.name == 'h2' and 'Stats' in tag.text)

    # If there is no h2, throw error
    if h2 is None:
        raise Exception("No h2 tag found")

    # Iterates through h2 siblings
    siblings = h2.next_siblings
    h3_name = ""
    h4_name = ""
    shadows: List[Shadow] = []

    for sibling in siblings:
        if sibling.name == 'h2':
            break

        elif sibling.name == 'h3':
            h3_name = sibling.text.replace("Edit", "")
        elif sibling.name == 'h4':
            h4_name = sibling.text.replace("Edit", "")

        # A weakness table with tabs
        elif sibling.name == 'div' and 'tabber' in sibling.attrs['class']:

            tables = __get_tables_from_tabber__(sibling)
            for (tab_name, table) in tables:
                full_variation = __create_full_variation_name__(h3_name, h4_name, tab_name)

                # If this is a Persona Q variation, skip it (we don't support them)
                if 'Persona Q' in full_variation:
                    break

                shadow = __try_create_shadow_from_table__(table, full_variation)

                if shadow is not None:
                    shadows.append(shadow)

        # A weakness table with no tabs
        elif sibling.name == 'table':

            full_variation = __create_full_variation_name__(h3_name, h4_name, '')

            # If this is a Persona Q variation, skip it (we don't support them)
            if 'Persona Q' in full_variation:
                break

            shadow = __try_create_shadow_from_table__(sibling, full_variation)

            if shadow is not None:
                shadows.append(shadow)

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

    full_variation = " - ".join(names)

    if full_variation == '':
        full_variation = "No variation"

    return full_variation


def __try_create_shadow_from_table__(table, full_variation: str) -> Optional[Shadow]:
    # Create shadow
    shadow = Shadow(full_variation)

    # Fill shadow with weaknesses
    weakness_tuples = __get_weaknesses_from_table__(table)
    for (weakness_type, weakness_status) in weakness_tuples:

        shadow.add_weakness(weakness_type, weakness_status)

    # If there were no weaknesses, return None (for no shadow from table)
    if len(weakness_tuples) == 0:
        return None
    else:
        return shadow


def __get_weaknesses_from_table__(table) -> List[Tuple[str, str]]:
    """
    :return: List of weakness tuples [(type, status)], or empty list if there are no weaknesses
    """
    custom_tables = table.find_all("table", {
        "class": "customtable"
    })

    # If there are no custom tables, there is no weakness table
    if len(custom_tables) == 0:
        return []

    weakness_table = custom_tables[1]

    rows = weakness_table.find_all("tr")
    type_row = rows[0].find_all("th")
    status_row = rows[1].find_all("td")

    return list(zip(
        map(lambda row: row.text.strip(), type_row),
        map(lambda row: row.text.strip(), status_row)
    ))
