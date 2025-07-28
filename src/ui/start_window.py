from re import compile

from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QInputDialog, QMessageBox, QWidget
from httpx import get
from loguru import logger

from .config_window import ConfigWindow
from .form.generate.start_window import Ui_Start
from ..config import config
from ..manager import client_manager, cpdlc_manager, flight_plan_manager
from ..manager.flight_plan_manager import FlightPlan
from ..meta import app_title

_SIMBRIEF_ID_PATTERN = compile(r"\d{7}")


def open_website(url: str):
    QDesktopServices.openUrl(QUrl(url))


class StartWindow(QWidget, Ui_Start):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.start.clicked.connect(self.start_cpdlc)
        self.setWindowTitle(app_title)
        self.register_label.setTextFormat(Qt.TextFormat.RichText)
        self.register_label.setText(
            'You dont have one? <a href="https://www.hoppie.nl/acars/system/register.html">Register now!</a>')
        self.register_label.setOpenExternalLinks(False)
        self.register_label.linkActivated.connect(open_website)
        self.from_simbrief.clicked.connect(self.import_from_simbrief)
        self.settings.clicked.connect(lambda: ConfigWindow().exec())
        config.add_config_save_callback(self.flush_from_config)

    def flush_from_config(self):
        self.remember_me.setChecked(config.remember_me)
        if config.remember_me:
            self.callsign.setText(config.callsign)
            self.email.setText(config.email)
            self.hoppie_code.setText(config.hoppie_code)
        else:
            self.callsign.setText("")
            self.email.setText("")
            self.hoppie_code.setText("")

    def import_from_simbrief(self):
        if config.simbrief_id == "":
            simbrief_id, ok = QInputDialog.getText(None, "Error",
                                                   "It looks like we don't have your Simbrief ID or Username\n"
                                                   "Please enter your Simbrief ID or Username")
            if not ok:
                QMessageBox.warning(self, "Error", "Import from simbrief failed because the user canceled the action")
                return
            if simbrief_id == "":
                QMessageBox.warning(self, "Error", "Import from simbrief fail due to missing simbrief ID")
                return
            config.simbrief_id = simbrief_id
            config.save_config()

        if _SIMBRIEF_ID_PATTERN.match(config.simbrief_id):
            res = client_manager.client.get(
                f"https://www.simbrief.com/api/xml.fetcher.php?userid={config.simbrief_id}&json=v2")
        else:
            res = client_manager.client.get(
                f"https://www.simbrief.com/api/xml.fetcher.php?username={config.simbrief_id}&json=v2")
        if res.status_code != 200:
            QMessageBox.warning(self, "Error",
                                f"Failed to fetch data from simbrief\n{res.json()['fetch']['status'].split(': ')[1]}")
            return
        data = res.json()
        callsign = data["general"]["icao_airline"] + data["general"]["flight_number"]
        dep = data["origin"]["icao_code"]
        arr = data["destination"]["icao_code"]
        route = data["general"]["route"]
        aircraft = data["aircraft"]["icao_code"]
        config.callsign = callsign
        config.save_config()
        plan = FlightPlan(callsign, dep, arr, aircraft, route)
        flight_plan_manager.set_flight_plan(plan)
        self.start_cpdlc()

    def show(self, /):
        self.flush_from_config()
        super().show()

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
        cpdlc_manager.set_client()
        self.hide()
        self.parent.show()
