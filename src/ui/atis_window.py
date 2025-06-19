from PySide6.QtWidgets import QWidget

from .form.generate.atis_window import Ui_ATIS


class ATISWindow(QWidget, Ui_ATIS):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
