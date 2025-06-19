from PySide6.QtWidgets import QWidget

from .form.generate.meter_window import Ui_Meter


class MeterWindow(QWidget, Ui_Meter):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
