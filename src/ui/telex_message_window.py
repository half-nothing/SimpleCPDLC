from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QWidget

from .form.generate.telex_message_window import Ui_Telex
from ..config import config
from ..manager import cpdlc_manager


class TelexMessageWindow(QWidget, Ui_Telex):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send.clicked.connect(self.send_telex)

    def show(self, /):
        self.callsign.setText(config.callsign)
        super().show()

    def keyReleaseEvent(self, event, /):
        if event.key() == Qt.Key.Key_Enter:
            self.send_telex()

    def send_telex(self):
        if (target_station := self.target_station.text()) == "":
            self.target_station.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a station code.")
            return
        else:
            self.target_station.setStyleSheet("")
        if (telex_content := self.telex_content.toPlainText()) == "":
            self.target_station.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter telex content.")
            return
        else:
            self.target_station.setStyleSheet("")
        cpdlc_manager.cpdlc.send_telex_message(target_station, telex_content.upper())
        self.hide()
