import unittest
from model.page import Page


class PageTest(unittest.TestCase):
    def test_avenger_knight(self):
        self.run_test_case("src/test/html_files/avenger_knight.html", {
            "Persona 3 - The Journey": {
                "Slash": "Null",
                "Strike": "-",
                "Pierce": "-",
                "Fire": "-",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Weak",
                "Dark": "-",
                "Almi": "-"
            },
            "Persona 3 - The Answer": {
                "Slash": "-",
                "Strike": "-",
                "Pierce": "Repel",
                "Fire": "-",
                "Ice": "-",
                "Elec": "Drain",
                "Wind": "-",
                "Light": "Null",
                "Dark": "Repel",
                "Almi": "-"
            },
            "Persona 4 - Boss": {
                "Phys": "Strong",
                "Fire": "-",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            },
            "Persona 4 - Normal Enemy": {
                "Phys": "Strong",
                "Fire": "-",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Weak",
                "Dark": "-",
                "Almi": "-"
            },
            "Persona 4 Golden - Boss": {
                "Phys": "-",
                "Fire": "Weak",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            },
            "Persona 4 Golden - Normal Enemy": {
                "Phys": "-",
                "Fire": "Weak",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "-",
                "Dark": "-",
                "Almi": "-"
            },
        })

    def test_shadow_yukiko(self):
        self.run_test_case("src/test/html_files/shadow_yukiko.html", {
            "Persona 4 - Shadow Yukiko - Persona 4": {
                "Phys": "-",
                "Fire": "Drain",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            },
            "Persona 4 - Shadow Yukiko - Golden": {
                "Phys": "-",
                "Fire": "Drain",
                "Ice": "Weak",
                "Elec": "-",
                "Wind": "-",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            },
            "Persona 4 - Charming Prince - Persona 4": {
                "Phys": "-",
                "Fire": "-",
                "Ice": "Weak",
                "Elec": "-",
                "Wind": "Strong",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            },
            "Persona 4 - Charming Prince - Golden": {
                "Phys": "-",
                "Fire": "-",
                "Ice": "-",
                "Elec": "Weak",
                "Wind": "Strong",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            }
        })

    def test_death_seeker(self):
        self.run_test_case("src/test/html_files/death_seeker.html", {
            "Persona 3 - The Journey": {
                "Slash": "-",
                "Strike": "-",
                "Pierce": "-",
                "Fire": "Strong",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Weak",
                "Dark": "Repel",
                "Almi": "-"
            },
            "Persona 3 - The Answer": {
                "Slash": "-",
                "Strike": "-",
                "Pierce": "-",
                "Fire": "Null",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Weak",
                "Dark": "Repel",
                "Almi": "-"
            },
            "Persona 4 - Persona 4": {
                "Phys": "-",
                "Fire": "-",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "-",
                "Dark": "-",
                "Almi": "-"
            },
            "Persona 4 - Golden": {
                "Phys": "-",
                "Fire": "-",
                "Ice": "-",
                "Elec": "-",
                "Wind": "-",
                "Light": "Weak",
                "Dark": "Null",
                "Almi": "-"
            }
        })

    def test_happiness_hand(self):
        self.run_test_case("src/test/html_files/happiness_hand.html", {
            "No variation": {
                "Phys": "-",
                "Fire": "Strong",
                "Ice": "Strong",
                "Elec": "Strong",
                "Wind": "Strong",
                "Light": "Strong",
                "Dark": "Strong",
                "Almi": "500%"
            }
        })

    def test_laughing_table(self):
        self.run_test_case("src/test/html_files/laughing_table.html", {
            "Persona 3 - Persona 3": {
                "Slash": "-",
                "Strike": "-",
                "Pierce": "Strong",
                "Fire": "Weak",
                "Ice": "Null",
                "Elec": "-",
                "Wind": "-",
                "Light": "-",
                "Dark": "-",
                "Almi": "-"
            },
            "Persona 3 - The Answer": {
                "Slash": "Repel",
                "Strike": "-",
                "Pierce": "-",
                "Fire": "Weak",
                "Ice": "Null",
                "Elec": "-",
                "Wind": "-",
                "Light": "-",
                "Dark": "-",
                "Almi": "-"
            },
            "Persona 4 - Persona 4": {
                "Phys": "Null",
                "Fire": "Null",
                "Ice": "Null",
                "Elec": "Null",
                "Wind": "Weak",
                "Light": "Null",
                "Dark": "Null",
                "Almi": "-"
            },
            "Persona 4 - Persona 4 Golden": {
                "Phys": "-",
                "Fire": "-",
                "Ice": "-",
                "Elec": "Strong",
                "Wind": "Weak",
                "Light": "-",
                "Dark": "-",
                "Almi": "-"
            }
        })

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
