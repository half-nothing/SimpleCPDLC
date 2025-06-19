import typing

from PySide6.QtCore import QPoint, QRect
from PySide6.QtGui import QBitmap, QPaintDevice, QPainter, QPolygon, QRegion
from PySide6.QtWidgets import QMainWindow, QWidget

from .atis_window import ATISWindow
from .cpdlc_connect_window import CPDLCConnectWindow
from .dcl_request_window import DCLRequestWindow
from .form.generate.main_window import Ui_MainWindow
from .meter_window import MeterWindow
from .start_window import StartWindow
from .telex_message_window import TelexMessageWindow
from ..config import config
from python_cpdlc import Network

from ..cpdlc import cpdlc_manager


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.telex_window = TelexMessageWindow(self)
        self.dcl_window = DCLRequestWindow(self)
        self.cpdlc_logon_window = CPDLCConnectWindow(self)
        self.meter_window = MeterWindow(self)
        self.atis_window = ATISWindow(self)
        self.start_window = StartWindow(self)
        self.start_window.show()
        for network in Network:
            self.network_select.addItem(network.value)
        self.telex_text.clicked.connect(self.show_telex)
        self.dcl_request.clicked.connect(self.show_dcl_window)
        self.cpdlc_logon.clicked.connect(self.show_cpdlc_logon_window)
        self.meter.clicked.connect(self.show_meter_window)
        self.atis.clicked.connect(self.show_atis_window)
        self.change_network_btn.clicked.connect(self.change_network)
        cpdlc_manager.add_create_callback(self.cpdlc_client_create_callback)

    def cpdlc_client_create_callback(self):
        cpdlc_manager.cpdlc.cpdlc_connect_callback = self.cpdlc_connect_callback
        cpdlc_manager.cpdlc.cpdlc_atc_info_update_callback = self.cpdlc_atc_info_update_callback
        cpdlc_manager.cpdlc.cpdlc_disconnect_callback = self.cpdlc_disconnect_callback

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
        self.callsign.setText(config.callsign)
        self.network.setText(cpdlc_manager.cpdlc.network.value)
        self.acars_server_url.setText(cpdlc_manager.cpdlc.acars_url)
        super().show()

    def change_network(self):
        network = self.network_select.currentText()
        self.network.setText(network)
        cpdlc_manager.cpdlc.change_network(Network(network))

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
