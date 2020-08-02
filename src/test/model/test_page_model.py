import unittest
from model.page import Page

from test.html_files.avenger_knight_weaknesses import avenger_knight_weaknesses
from test.html_files.death_seeker_weaknesses import death_seeker_weaknesses
from test.html_files.happiness_hand_weaknesses import happiness_hand_weaknesses
from test.html_files.laughing_table_weaknesses import laughing_table_weaknesses
from test.html_files.nebiros_weaknesses import nebiros_weaknesses
from test.html_files.shadow_yukiko_weaknesses import shadow_yukiko_weaknesses


class TestPageModel(unittest.TestCase):
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

    def run_test_case(self, file_path: str, test_case):
        # Reads html
        file = open(file_path, mode='r', encoding='utf-8')
        html = file.read()
        file.close()

        # Creates page
        page = Page(html)
        page_variations = page.get_variations()

        for expected_variation in test_case.keys():
            # Test if variation is in page
            self.assertIn(expected_variation, page_variations, f'Variation {expected_variation} not found')

            shadow = page.get_shadow(expected_variation)

            # Goes through all weaknesses
            expected_weaknesses = test_case[expected_variation]
            for expected_weakness_type in expected_weaknesses.keys():

                expected_status = expected_weaknesses[expected_weakness_type]
                actual_status = shadow.get_weaknesses(expected_weakness_type)

                # Tests weakness
                self.assertEqual(expected_status, actual_status,
                                 f'{actual_status} is not {expected_status} in variation {expected_variation}')

            # Remove variation from list
            page_variations.remove(expected_variation)

        # Variation list should be empty
        self.assertEqual(0, len(page_variations),
                         "Variation list length is non-zero; did you miss some variation cases?")


if __name__ == '__main__':
    unittest.main()
