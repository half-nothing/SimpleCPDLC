from PySide6.QtWidgets import QWidget
from .form.generate.message_window import Ui_MessageWindow


class MessageWindow(QWidget, Ui_MessageWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
