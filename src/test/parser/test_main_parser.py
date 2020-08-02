import unittest
from bs4 import BeautifulSoup

from soup_parse.main_parser import parse
from test.html_files.avenger_knight_weaknesses import avenger_knight_weaknesses


class TestMainParser(unittest.TestCase):
    def test_main_parser(self):
        # Reads html
        file = open("src/test/html_files/avenger_knight.html", mode='r', encoding='utf-8')
        html = file.read()
        file.close()

        # Gets table
        soup = BeautifulSoup(html, 'html.parser')

        # Parses table
        shadows = parse(soup)

        # Asserts variations
        variations = map(lambda s: s.get_variation(), shadows)

        self.assertIn("Persona 3 - The Journey", variations)
        self.assertIn("Persona 3 - The Answer", variations)
        self.assertIn("Persona 4 - Boss", variations)
        self.assertIn("Persona 4 - Normal Enemy", variations)
        self.assertIn("Persona 4 Golden - Boss", variations)
        self.assertIn("Persona 4 Golden - Normal Enemy", variations)

        # Asserts weaknesses
        expected_weaknesses = avenger_knight_weaknesses

        for shadow in shadows:
            # Gets expected weakness from variation
            variation = shadow.get_variation()
            expected_weakness = expected_weaknesses[variation]

            # Assert
            for expected_weakness_type in expected_weakness.keys():

                expected_weakness_status = expected_weakness[expected_weakness_type]
                actual_weakness_status = shadow.get_weaknesses(expected_weakness_type)

                self.assertEqual(expected_weakness_status, actual_weakness_status,
                                 f'{actual_weakness_status} is not {expected_weakness_status} in variation {variation}')
