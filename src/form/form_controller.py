from typing import Optional

import form.form_view as form_view
from api import get_shadow_page
from model.page import Page


class UiController:
    def __init__(self, app, window):
        self.app = app
        self.weaknesses = []
        self.page: Optional[Page] = None

        # Sets up form UI
        self.form = form_view.Ui_form()
        self.form.setupUi(window)

        # Sets up event handlers
        self.form.search_button.clicked.connect(self.on_search_button_clicked)
        self.form.search_input.returnPressed.connect(self.on_search_button_clicked)
        self.form.variation_list.itemClicked.connect(self.on_shadow_type_selected)

    def on_search_button_clicked(self):
        try:
            self.page = get_shadow_page(self.get_search_input_text())
        except Exception as e:
            print(e)
        else:
            self.update_variation_list()

    def on_shadow_type_selected(self, item):
        variation = item.text()

        # Get shadow from variation
        shadow = self.page.get_shadow(variation)

        # Updates weakness view
        self.form.phys_weakness.setText(shadow.get_weaknesses("Phys"))
        self.form.fire_weakness.setText(shadow.get_weaknesses("Fire"))
        self.form.ice_weakness.setText(shadow.get_weaknesses("Ice"))
        self.form.elec_weakness.setText(shadow.get_weaknesses("Elec"))
        self.form.wind_weakness.setText(shadow.get_weaknesses("Wind"))
        self.form.light_weakness.setText(shadow.get_weaknesses("Light"))
        self.form.dark_weakness.setText(shadow.get_weaknesses("Dark"))
        self.form.almi_weakness.setText(shadow.get_weaknesses("Almi"))

    def update_variation_list(self):
        self.form.variation_list.clear()

        for variation in self.page.get_variations():
            self.form.variation_list.addItem(variation)

    def get_search_input_text(self):
        return self.form.search_input.text()
