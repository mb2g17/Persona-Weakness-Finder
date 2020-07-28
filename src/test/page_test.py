import unittest
import api


class PageTest(unittest.TestCase):
    def test_get_names(self):
        games = api.get_shadow_page("avenger knight")
        # self.assertListEqual(games, ["Persona 3", "Persona 4", "Persona 4 Golden"])


if __name__ == '__main__':
    unittest.main()
