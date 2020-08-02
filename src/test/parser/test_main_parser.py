import unittest
from bs4 import BeautifulSoup

from soup_parse.main_parser import parse
from test.html_files.avenger_knight_weaknesses import avenger_knight_weaknesses
from test.html_files.death_seeker_weaknesses import death_seeker_weaknesses
from test.html_files.happiness_hand_weaknesses import happiness_hand_weaknesses
from test.html_files.laughing_table_weaknesses import laughing_table_weaknesses
from test.html_files.nebiros_weaknesses import nebiros_weaknesses
from test.html_files.shadow_yukiko_weaknesses import shadow_yukiko_weaknesses


class TestMainParser(unittest.TestCase):
    def test_avenger_knight(self):
        self.run_test_case("src/test/html_files/avenger_knight.html", avenger_knight_weaknesses)

    def test_shadow_yukiko(self):
        self.run_test_case("src/test/html_files/shadow_yukiko.html", shadow_yukiko_weaknesses)

    def test_death_seeker(self):
        self.run_test_case("src/test/html_files/death_seeker.html", death_seeker_weaknesses)

    def test_happiness_hand(self):
        self.run_test_case("src/test/html_files/happiness_hand.html", happiness_hand_weaknesses)

    def test_laughing_table(self):
        self.run_test_case("src/test/html_files/laughing_table.html", laughing_table_weaknesses)

    def test_nebiros(self):
        self.run_test_case("src/test/html_files/nebiros.html", nebiros_weaknesses)

    def run_test_case(self, filename: str, test_case):
        # Reads html
        file = open(filename, mode='r', encoding='utf-8')
        html = file.read()
        file.close()

        # Gets table
        soup = BeautifulSoup(html, 'html5lib')

        # Parses table
        shadows = parse(soup)

        # Asserts variations
        expected_variations = test_case.keys()
        actual_variations = map(lambda s: s.get_variation(), shadows)

        for expected_variation in expected_variations:
            self.assertIn(expected_variation, actual_variations)

        # Asserts weaknesses
        for shadow in shadows:
            # Gets expected weakness from variation
            variation = shadow.get_variation()
            expected_weakness = test_case[variation]

            # Assert
            for expected_weakness_type in expected_weakness.keys():

                expected_weakness_status = expected_weakness[expected_weakness_type]
                actual_weakness_status = shadow.get_weaknesses(expected_weakness_type)

                self.assertEqual(expected_weakness_status, actual_weakness_status,
                                 f'{actual_weakness_status} is not {expected_weakness_status} in variation {variation}')