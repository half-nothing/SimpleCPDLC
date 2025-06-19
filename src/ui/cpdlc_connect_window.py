from PySide6.QtWidgets import QWidget

from .form.generate.cpdlc_connect_window import Ui_Login


class CPDLCConnectWindow(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
