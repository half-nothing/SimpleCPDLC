from PySide6.QtWidgets import QMainWindow, QMessageBox
from loguru import logger
from python_cpdlc import NetworkSwitchError
from python_cpdlc.enums import Network

from .atis_window import ATISWindow
from .config_window import ConfigWindow
from .cpdlc_connect_window import CPDLCConnectWindow
from .dcl_request_window import DCLRequestWindow
from .form.generate.main_window import Ui_MainWindow
from .meter_window import MeterWindow
from .start_window import StartWindow
from .telex_message_window import TelexMessageWindow
from ..config import config
from ..manager import cpdlc_manager, flight_plan_manager
from ..meta import app_title


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        logger.trace("Creating main window")
        self.setupUi(self)
        self.telex_window = TelexMessageWindow()
        self.dcl_window = DCLRequestWindow()
        self.cpdlc_logon_window = CPDLCConnectWindow()
        self.meter_window = MeterWindow()
        self.atis_window = ATISWindow()
        self.start_window = StartWindow(self)
        self.start_window.show()
        logger.trace("Window initialized, show start window")
        self.setWindowTitle(app_title)
        for network in Network:
            if network in [Network.UNOFFICIAL, Network.UNKNOWN]:
                continue
            self.network_select.addItem(network.value)
        self.telex_text.clicked.connect(self.show_telex)
        self.dcl_request.clicked.connect(self.show_dcl_window)
        self.cpdlc_logon.clicked.connect(self.show_cpdlc_logon_window)
        self.meter.clicked.connect(self.show_meter_window)
        self.atis.clicked.connect(self.show_atis_window)
        self.change_network_btn.clicked.connect(self.change_network)
        cpdlc_manager.cpdlc.set_cpdlc_connect_callback(self.cpdlc_connect_callback)
        cpdlc_manager.cpdlc.set_cpdlc_atc_info_update_callback(self.cpdlc_atc_info_update_callback)
        cpdlc_manager.cpdlc.set_cpdlc_disconnect_callback(self.cpdlc_disconnect_callback)
        self.action_option.triggered.connect(lambda: ConfigWindow().exec())
        self.action_about_this.triggered.connect(
            lambda: QMessageBox.about(self,
                                      "About SimpleCPDLC",
                                      f"{app_title}\n"
                                      f"Copyright © 2025-2025 Half_nothing. All rights reserved."))
        self.action_about_qt.triggered.connect(lambda: QMessageBox.aboutQt(self))

    def cpdlc_connect_callback(self):
        self.cpdlc_status.setText("Connected")
        self.atc_unit.setText(cpdlc_manager.cpdlc.cpdlc_current_atc)
        self.cpdlc_logon.setText("CPDLC Logoff")

    def cpdlc_atc_info_update_callback(self):
        self.cpdlc_connect_callback()
        self.atc_callsign.setText(cpdlc_manager.cpdlc.cpdlc_atc_callsign)

    def cpdlc_disconnect_callback(self):
        self.cpdlc_status.setText("no connection")
        self.atc_unit.setText("----")
        self.atc_callsign.setText("----")
        self.cpdlc_logon.setText("CPDLC Logon")

    def show(self, /):
        if flight_plan_manager.flight_plan:
            self.page_tab.setTabEnabled(1, True)
            plan = flight_plan_manager.flight_plan
            self.simbrief_id.setText(config.simbrief_id)
            self.dep_airport.setText(plan.dep)
            self.arr_airport.setText(plan.arr)
            self.aircraft_type.setText(plan.aircraft)
            self.route.setText(plan.route)
        else:
            self.page_tab.setTabEnabled(1, False)
        self.callsign.setText(config.callsign)
        self.network.setText(cpdlc_manager.cpdlc.network.value)
        self.acars_server_url.setText(cpdlc_manager.cpdlc.acars_url)
        super().show()

    def change_network(self):
        network = self.network_select.currentText()
        try:
            if cpdlc_manager.cpdlc.change_network(Network(network)):
                self.network.setText(network)
        except NetworkSwitchError as e:
            QMessageBox.warning(self, "Network Change Error", f"Network change failed\n{e}")

    def show_telex(self):
        self.telex_window.show()

    def show_dcl_window(self):
        self.dcl_window.show()

    def show_cpdlc_logon_window(self):
        if cpdlc_manager.cpdlc.cpdlc_connect:
            cpdlc_manager.cpdlc.cpdlc_logout()
        else:
            self.cpdlc_logon_window.show()

    def show_meter_window(self):
        self.meter_window.show()

    def show_atis_window(self):
        self.atis_window.show()
