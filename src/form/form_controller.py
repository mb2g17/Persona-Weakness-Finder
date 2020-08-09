import threading
from typing import Optional

from PyQt5.QtGui import QPixmap

import form.form_view as form_view
from api import get_shadow_page, save_shadow_portrait
from model.game import Game
from model.page import Page
from model.shadow import Shadow


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
        self.display_shadow(shadow)

    def display_shadow(self, shadow: Shadow):
        game_name = shadow.get_game()

        if game_name == Game.PERSONA_3:
            self.display_persona_3_shadow(shadow)
        elif game_name == Game.PERSONA_4:
            self.display_persona_4_shadow(shadow)
        elif game_name == Game.PERSONA_5:
            self.display_persona_5_shadow(shadow)

    def display_persona_3_shadow(self, shadow: Shadow):
        self.form.slash_3_weakness.setText(shadow.get_weaknesses("Slash"))
        self.form.strike_3_weakness.setText(shadow.get_weaknesses("Strike"))
        self.form.pierce_3_weakness.setText(shadow.get_weaknesses("Pierce"))
        self.form.fire_3_weakness.setText(shadow.get_weaknesses("Fire"))
        self.form.ice_3_weakness.setText(shadow.get_weaknesses("Ice"))
        self.form.elec_3_weakness.setText(shadow.get_weaknesses("Elec"))
        self.form.wind_3_weakness.setText(shadow.get_weaknesses("Wind"))
        self.form.light_3_weakness.setText(shadow.get_weaknesses("Light"))
        self.form.dark_3_weakness.setText(shadow.get_weaknesses("Dark"))
        self.form.almi_3_weakness.setText(shadow.get_weaknesses("Almi"))

        self.enable_persona_tab(0)

    def display_persona_4_shadow(self, shadow: Shadow):
        self.form.phys_4_weakness.setText(shadow.get_weaknesses("Phys"))
        self.form.fire_4_weakness.setText(shadow.get_weaknesses("Fire"))
        self.form.ice_4_weakness.setText(shadow.get_weaknesses("Ice"))
        self.form.elec_4_weakness.setText(shadow.get_weaknesses("Elec"))
        self.form.wind_4_weakness.setText(shadow.get_weaknesses("Wind"))
        self.form.light_4_weakness.setText(shadow.get_weaknesses("Light"))
        self.form.dark_4_weakness.setText(shadow.get_weaknesses("Dark"))
        self.form.almi_4_weakness.setText(shadow.get_weaknesses("Almi"))

        self.enable_persona_tab(1)

    def display_persona_5_shadow(self, shadow: Shadow):
        self.form.phys_5_weakness.setText(shadow.get_weaknesses("Phys"))
        self.form.gun_5_weakness.setText(shadow.get_weaknesses("Gun"))
        self.form.fire_5_weakness.setText(shadow.get_weaknesses("Fire"))
        self.form.ice_5_weakness.setText(shadow.get_weaknesses("Ice"))
        self.form.elec_5_weakness.setText(shadow.get_weaknesses("Elec"))
        self.form.wind_5_weakness.setText(shadow.get_weaknesses("Wind"))
        self.form.psy_5_weakness.setText(shadow.get_weaknesses("Psy"))
        self.form.nuke_5_weakness.setText(shadow.get_weaknesses("Nuke"))
        self.form.bless_5_weakness.setText(shadow.get_weaknesses("Bless"))
        self.form.curse_5_weakness.setText(shadow.get_weaknesses("Curse"))
        self.form.almi_5_weakness.setText(shadow.get_weaknesses("Almi"))

        self.enable_persona_tab(2)

    def enable_persona_tab(self, index: int):
        for i in range(0, 3):
            self.form.persona_tabs.setTabEnabled(i, True)

        self.form.persona_tabs.setCurrentIndex(index)

        for i in range(0, 3):
            self.form.persona_tabs.setTabEnabled(i, i == index)

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
