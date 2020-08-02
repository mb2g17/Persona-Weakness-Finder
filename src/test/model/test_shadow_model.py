import unittest
from model.shadow import Shadow


class TestShadowModel(unittest.TestCase):
    def test_weaknesses(self):
        shadow = Shadow("My variation")

        shadow.add_weakness("Phys", "Weak")
        shadow.add_weakness("Fire", "Strong")
        shadow.add_weakness("Ice", "Drain")
        shadow.add_weakness("Elec", "Null")
        shadow.add_weakness("Wind", "-")

        self.assertEqual("Weak", shadow.get_weaknesses("Phys"))
        self.assertEqual("Strong", shadow.get_weaknesses("Fire"))
        self.assertEqual("Drain", shadow.get_weaknesses("Ice"))
        self.assertEqual("Null", shadow.get_weaknesses("Elec"))
        self.assertEqual("-", shadow.get_weaknesses("Wind"))

    def test_variants(self):
        expected_variation = "My Variation"
        shadow = Shadow(expected_variation)

        self.assertEqual(expected_variation, shadow.get_variation())
