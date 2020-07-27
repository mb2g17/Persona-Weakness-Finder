import form.form_view as form_view
import api

from PyQt5 import QtGui, QtWidgets


class UiController:
    def __init__(self, app, window):
        self.app = app

        # Sets up form UI
        self.form = form_view.Ui_form()
        self.form.setupUi(window)

        # Sets up event handlers
        self.form.search_button.clicked.connect(self.on_search_button_clicked)
        self.form.search_input.returnPressed.connect(self.on_search_button_clicked)

    def on_search_button_clicked(self):
        try:
            shadow_page = api.get_shadow_page(self.get_search_input_text())
        except Exception as e:
            print(e)
        else:
            print(shadow_page.get_weaknesses())

    def get_search_input_text(self):
        return self.form.search_input.text()
