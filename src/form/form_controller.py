import threading
from typing import Optional

from PyQt5.QtGui import QPixmap

import form.form_view as form_view
from api import get_shadow_page, save_shadow_portrait
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
        self.display_start_loading_view()

        shadow_name = self.form.search_input.text()

        def get_shadow_weakness():
            self.update_page(shadow_name)
            self.update_variation_list()
            self.display_finished_loading_view()

        def get_shadow_portrait():

            pixmap = QPixmap("assets/loading.png")
            self.form.persona_display.setPixmap(pixmap)

            if save_shadow_portrait(shadow_name):

                pixmap = QPixmap("assets/portrait.png")
                self.form.persona_display.setPixmap(pixmap)

            else:

                pixmap = QPixmap("assets/noportraitfound.png")
                self.form.persona_display.setPixmap(pixmap)


        weakness_thread = threading.Thread(target=get_shadow_weakness)
        portrait_thread = threading.Thread(target=get_shadow_portrait)
        weakness_thread.start()
        portrait_thread.start()

    def update_page(self, shadow_name):
        self.page = get_shadow_page(shadow_name)

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

    def display_start_loading_view(self):
        self.form.search_button.setEnabled(False)
        self.form.search_button.setText("Loading...")
        self.form.variation_list.clear()

    def display_finished_loading_view(self):
        self.form.search_button.setEnabled(True)
        self.form.search_button.setText("Search")
