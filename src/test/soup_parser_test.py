import unittest
from bs4 import BeautifulSoup
from soup_parser import parse_soup


class SoupParserTest(unittest.TestCase):
    def test_avenger_knight(self):
        # Reads avenger knight html
        file = open("html_files/avenger_knight.html", mode='r', encoding='utf-8')
        html = file.read()
        file.close()

        # Parses html
        soup = BeautifulSoup(html, 'html.parser')
        parsed_result = parse_soup(soup)

        # Tests variations
        variations = map(lambda result: result[0], parsed_result)
        self.assertIn("Persona 3 - The Journey", variations)
        self.assertIn("Persona 3 - The Answer", variations)
        self.assertIn("Persona 4 - Boss", variations)
        self.assertIn("Persona 4 - Normal Enemy", variations)
        self.assertIn("Persona 4 Golden - Boss", variations)
        self.assertIn("Persona 4 Golden - Normal Enemy", variations)

if __name__ == '__main__':
    unittest.main()
