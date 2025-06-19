from PySide6.QtWidgets import QWidget

from .form.generate.start_window import Ui_Start


class StartWindow(QWidget, Ui_Start):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
