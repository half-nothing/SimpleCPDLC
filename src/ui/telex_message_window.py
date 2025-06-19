from PySide6.QtWidgets import QWidget

from .form.generate.telex_message_window import Ui_Telex


class TelexMessageWindow(QWidget, Ui_Telex):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
