import form.form_view as form_view

from PyQt5 import QtGui, QtWidgets;

class UiController:
    def __init__(self, app, window):
        self.app = app

        self.form = form_view.Ui_Form()
        self.form.setupUi(window)