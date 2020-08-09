import unittest
from unittest import mock

from model.page import Page
from model.shadow import Shadow


class TestPageModel(unittest.TestCase):
    def setUp(self):
        # Creates shadows
        self.shadow1 = Shadow("Persona 3 - Shadow 1")
        self.shadow1.add_weakness("Phys", "Weak")
        self.shadow1.add_weakness("Fire", "Strong")

        self.shadow2 = Shadow("Persona 4 - Shadow 2")
        self.shadow2.add_weakness("Ice", "Reflect")
        self.shadow2.add_weakness("Wind", "-")

    def test_variations(self):
        page = self.get_page()

        # Asserts retrieved variations
        variations = page.get_variations()
        self.assertIn("Persona 3 - Shadow 1", variations)
        self.assertIn("Persona 4 - Shadow 2", variations)

    def test_shadows(self):
        page = self.get_page()

        # Asserts retrieved shadows
        self.assertIs(self.shadow1, page.get_shadow("Persona 3 - Shadow 1"))
        self.assertIs(self.shadow2, page.get_shadow("Persona 4 - Shadow 2"))

    def get_page(self):
        # Mocks parser
        with mock.patch('soup_parse.main_parser') as mock_parser:
            mock_parser.parse.return_value = [self.shadow1, self.shadow2]

            # Creates page (empty HTML because parser is mocked)
            page = Page("")

            return page


if __name__ == '__main__':
    unittest.main()
