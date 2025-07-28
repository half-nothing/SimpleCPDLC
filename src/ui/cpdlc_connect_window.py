from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QWidget

from .form.generate.cpdlc_connect_window import Ui_Login
from ..config import config
from ..manager import cpdlc_manager


class CPDLCConnectWindow(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send.clicked.connect(self.cpdlc_connect)

    def show(self, /):
        self.callsign.setText(config.callsign)
        super().show()

    def keyReleaseEvent(self, event, /):
        if event.key() == Qt.Key.Key_Enter:
            self.cpdlc_connect()

    def cpdlc_connect(self):
        if (target_station := self.target_station.text()) == "":
            self.target_station.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a station code.")
            return
        else:
            self.target_station.setStyleSheet("")
        cpdlc_manager.cpdlc.cpdlc_login(target_station)
        self.hide()
