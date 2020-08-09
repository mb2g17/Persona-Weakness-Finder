import unittest

from model.game import Game
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

    def test_game_by_variation(self):
        shadow_3 = Shadow("Persona 3 - The Journey")
        shadow_4 = Shadow("Persona 4 - Charming Prince - Golden")
        shadow_5 = Shadow("Persona 5 - Boss (Niijima Palace")
        shadow_none = Shadow("Nothing")

        self.assertEqual(Game.PERSONA_3, shadow_3.get_game())
        self.assertEqual(Game.PERSONA_4, shadow_4.get_game())
        self.assertEqual(Game.PERSONA_5, shadow_5.get_game())
        self.assertRaises(Exception, shadow_none.get_game)

    def test_game_by_attack_types(self):
        shadow_3 = Shadow("P3")
        shadow_3.add_weakness("Slash", "-")
        shadow_3.add_weakness("Strike", "-")
        shadow_3.add_weakness("Pierce", "-")
        shadow_3.add_weakness("Fire", "-")
        shadow_3.add_weakness("Ice", "-")
        shadow_3.add_weakness("Elec", "-")
        shadow_3.add_weakness("Wind", "-")
        shadow_3.add_weakness("Light", "-")
        shadow_3.add_weakness("Dark", "-")
        shadow_3.add_weakness("Almi", "-")

        shadow_4 = Shadow("P4")
        shadow_4.add_weakness("Phys", "-")
        shadow_4.add_weakness("Fire", "-")
        shadow_4.add_weakness("Ice", "-")
        shadow_4.add_weakness("Elec", "-")
        shadow_4.add_weakness("Wind", "-")
        shadow_4.add_weakness("Light", "-")
        shadow_4.add_weakness("Dark", "-")
        shadow_4.add_weakness("Almi", "-")

        shadow_5 = Shadow("P5")
        shadow_5.add_weakness("Phys", "-")
        shadow_5.add_weakness("Gun", "-")
        shadow_5.add_weakness("Fire", "-")
        shadow_5.add_weakness("Ice", "-")
        shadow_5.add_weakness("Elec", "-")
        shadow_5.add_weakness("Wind", "-")
        shadow_5.add_weakness("Psy", "-")
        shadow_5.add_weakness("Nuke", "-")
        shadow_5.add_weakness("Bless", "-")
        shadow_5.add_weakness("Curse", "-")
        shadow_5.add_weakness("Almi", "-")

        self.assertEqual(Game.PERSONA_3, shadow_3.get_game())
        self.assertEqual(Game.PERSONA_4, shadow_4.get_game())
        self.assertEqual(Game.PERSONA_5, shadow_5.get_game())
