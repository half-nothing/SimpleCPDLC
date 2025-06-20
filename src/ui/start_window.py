from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget
from loguru import logger

from .form.generate.start_window import Ui_Start
from ..config import config
from ..cpdlc import cpdlc_manager
from ..meta import app_title


class StartWindow(QWidget, Ui_Start):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.start.clicked.connect(self.start_cpdlc)
        self.setWindowTitle(app_title)
        self.register_label.setTextFormat(Qt.TextFormat.RichText)
        self.register_label.setText('You dont have one? <a href="https://www.hoppie.nl/acars/system/register.html">Register now!</a>')
        self.register_label.setOpenExternalLinks(False)
        self.register_label.linkActivated.connect(self.open_website)

    def show(self, /):
        if config.remember_me:
            self.callsign.setText(config.callsign)
            self.email.setText(config.email)
            self.hoppie_code.setText(config.hoppie_code)
            self.remember_me.setChecked(True)
        super().show()

    def open_website(self, url: str):
        QDesktopServices.openUrl(QUrl(url))

    def start_cpdlc(self):
        callsign = self.callsign.text()
        if callsign == "":
            logger.error(f"Callsign can't be empty")
            self.callsign.setStyleSheet("background-color: #ef9a9a;color: white")
        else:
            self.callsign.setStyleSheet("")
        email = self.email.text()
        if email == "":
            logger.error(f"Email can't be empty")
            self.email.setStyleSheet("background-color: #ef9a9a;color: white")
        else:
            self.email.setStyleSheet("")
        code = self.hoppie_code.text()
        if code == "":
            logger.error(f"Code can't be empty")
            self.hoppie_code.setStyleSheet("background-color: #ef9a9a;color: white")
        else:
            self.hoppie_code.setStyleSheet("")
        remember_me = self.remember_me.isChecked()
        if callsign == "" or email == "" or code == "":
            return
        config.callsign = callsign
        config.email = email
        config.hoppie_code = code
        if remember_me:
            config.remember_me = True
            config.save_config()
        elif remember_me != config.remember_me:
            config.remember_me = False
            config.save_config()
        cpdlc_manager.create_client()
        self.hide()
        self.parent.show()
