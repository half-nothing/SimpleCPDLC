from PySide6.QtWidgets import QDialog

from .form.generate.config_window import Ui_Config
from ..config import config


class ConfigWindow(QDialog, Ui_Config):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.save_and_close)
        self.apply_btn.clicked.connect(self.save_config)
        self.cancel_btn.clicked.connect(self.reject)

    def save_and_close(self) -> None:
        self.save_config()
        self.accept()

    def save_config(self) -> None:
        config.log_level = self.log_level.currentText()
        config.debug_mode = self.debug_mode.isChecked()
        config.remember_me = self.remember_me.isChecked()
        config.callsign = self.callsign.text()
        config.email = self.email.text()
        config.hoppie_code = self.hoppie_code.text()
        config.simbrief_id = self.simbrief_id.text()
        config.save_config()

    def exec(self, /):
        self.version.setText(config.config_version)
        self.log_level.setCurrentText(config.log_level)
        self.debug_mode.setChecked(config.debug_mode)
        self.remember_me.setChecked(config.remember_me)
        self.callsign.setText(config.callsign)
        self.email.setText(config.email)
        self.hoppie_code.setText(config.hoppie_code)
        self.simbrief_id.setText(config.simbrief_id)
        return super().exec()
