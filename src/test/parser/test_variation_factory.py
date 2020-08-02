import unittest

from soup_parse.variation_factory import VariationFactory


class TestVariationFactory(unittest.TestCase):
    def test_h3_only(self):
        variation_factory = VariationFactory()
        variation_factory.h3_name = "Persona 4"

        full_variation = variation_factory.create_full_variation_name()

        self.assertEqual("Persona 4", full_variation)

    def test_h3_and_h4(self):
        variation_factory = VariationFactory()
        variation_factory.h3_name = "Persona 4"
        variation_factory.h4_name = "Shadow Yukiko"

        full_variation = variation_factory.create_full_variation_name()

        self.assertEqual("Persona 4 - Shadow Yukiko", full_variation)

    def test_h3_and_h4_and_tab(self):
        variation_factory = VariationFactory()
        variation_factory.h3_name = "Persona 4"
        variation_factory.h4_name = "Shadow Yukiko"
        variation_factory.tab_name = "Golden"

        full_variation = variation_factory.create_full_variation_name()

        self.assertEqual("Persona 4 - Shadow Yukiko - Golden", full_variation)

    def test_no_variation(self):
        variation_factory = VariationFactory()

        full_variation = variation_factory.create_full_variation_name()

        self.assertEqual("No variation", full_variation)
