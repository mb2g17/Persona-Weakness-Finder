import form.form_view as form_view
import api

from PyQt5 import QtGui, QtWidgets


class UiController:
    def __init__(self, app, window):
        self.app = app
        self.weaknesses = []

        # Sets up form UI
        self.form = form_view.Ui_form()
        self.form.setupUi(window)

        # Sets up event handlers
        self.form.search_button.clicked.connect(self.on_search_button_clicked)
        self.form.search_input.returnPressed.connect(self.on_search_button_clicked)
        self.form.shadow_type_list.itemClicked.connect(self.on_shadow_type_selected)

    def on_search_button_clicked(self):
        try:
            shadow_page = api.get_shadow_page(self.get_search_input_text())
        except Exception as e:
            print(e)
        else:
            self.form.shadow_type_list.clear()
            self.weaknesses = shadow_page.get_weaknesses()

            for weakness in self.weaknesses:
                self.form.shadow_type_list.addItem(weakness["name"])

    def on_shadow_type_selected(self, item):
        shadow_type = item.text()

        for weakness in self.weaknesses:
            if weakness["name"] == shadow_type:
                self.form.phys_weakness.setText(weakness["list"][0])
                self.form.fire_weakness.setText(weakness["list"][1])
                self.form.ice_weakness.setText(weakness["list"][2])
                self.form.elec_weakness.setText(weakness["list"][3])
                self.form.wind_weakness.setText(weakness["list"][4])
                self.form.light_weakness.setText(weakness["list"][5])
                self.form.dark_weakness.setText(weakness["list"][6])
                self.form.almi_weakness.setText(weakness["list"][7])

    def get_search_input_text(self):
        return self.form.search_input.text()
