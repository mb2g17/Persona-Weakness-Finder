from typing import List, Tuple, Optional

from bs4 import Tag

from model.shadow import Shadow
from soup_parse.variation_factory import VariationFactory


def parse_table(table: Tag, variation_factory: VariationFactory) -> Optional[Shadow]:
    full_variation = variation_factory.create_full_variation_name()

    # If this is a Persona Q variation, skip it (we don't support them)
    if 'Persona Q' in full_variation:
        return None

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


def __get_weaknesses_from_table__(table: Tag) -> List[Tuple[str, str]]:
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
