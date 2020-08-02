import unittest
from bs4 import BeautifulSoup

from soup_parse.table_parser import parse_table
from soup_parse.variation_factory import VariationFactory


class TestTableParser(unittest.TestCase):
    def test_persona_3_table(self):
        # Parses table
        shadow = parse_table_from_file("src/test/html_files/avenger_knight.html", "The Journey")

        # Asserts shadow
        self.assertEqual("Null", shadow.get_weaknesses("Slash"))
        self.assertEqual("-", shadow.get_weaknesses("Strike"))
        self.assertEqual("-", shadow.get_weaknesses("Pierce"))
        self.assertEqual("-", shadow.get_weaknesses("Fire"))
        self.assertEqual("-", shadow.get_weaknesses("Ice"))
        self.assertEqual("-", shadow.get_weaknesses("Elec"))
        self.assertEqual("-", shadow.get_weaknesses("Wind"))
        self.assertEqual("Weak", shadow.get_weaknesses("Light"))
        self.assertEqual("-", shadow.get_weaknesses("Dark"))
        self.assertEqual("-", shadow.get_weaknesses("Almi"))

    def test_persona_4_table(self):
        # Parses table
        shadow = parse_table_from_file("src/test/html_files/shadow_yukiko.html", "Persona 4")

        # Asserts shadow
        self.assertEqual("-", shadow.get_weaknesses("Phys"))
        self.assertEqual("Drain", shadow.get_weaknesses("Fire"))
        self.assertEqual("-", shadow.get_weaknesses("Ice"))
        self.assertEqual("-", shadow.get_weaknesses("Elec"))
        self.assertEqual("-", shadow.get_weaknesses("Wind"))
        self.assertEqual("Null", shadow.get_weaknesses("Light"))
        self.assertEqual("Null", shadow.get_weaknesses("Dark"))
        self.assertEqual("-", shadow.get_weaknesses("Almi"))

    def test_persona_5_table(self):
        # Parses table
        shadow = parse_table_from_file("src/test/html_files/nebiros.html", "Shadow")

        # Asserts shadow
        self.assertEqual("-", shadow.get_weaknesses("Phys"))
        self.assertEqual("-", shadow.get_weaknesses("Gun"))
        self.assertEqual("-", shadow.get_weaknesses("Fire"))
        self.assertEqual("-", shadow.get_weaknesses("Ice"))
        self.assertEqual("-", shadow.get_weaknesses("Elec"))
        self.assertEqual("-", shadow.get_weaknesses("Wind"))
        self.assertEqual("Strong", shadow.get_weaknesses("Psy"))
        self.assertEqual("-", shadow.get_weaknesses("Nuke"))
        self.assertEqual("Weak", shadow.get_weaknesses("Bless"))
        self.assertEqual("Repel", shadow.get_weaknesses("Curse"))
        self.assertEqual("-", shadow.get_weaknesses("Almi"))


def parse_table_from_file(filename, tabbertab_title):
    # Reads html
    file = open(filename, mode='r', encoding='utf-8')
    html = file.read()
    file.close()

    # Gets table
    soup = BeautifulSoup(html, 'html.parser')
    tabbertab = soup.find("div", {
        "class": "tabbertab",
        "title": tabbertab_title
    })
    table = tabbertab.find("table")

    # Parses table
    shadow = parse_table(table, VariationFactory())
    return shadow
