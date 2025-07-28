from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QWidget

from .form.generate.dcl_request_window import Ui_DCL
from ..config import config
from ..manager import cpdlc_manager, flight_plan_manager


class DCLRequestWindow(QWidget, Ui_DCL):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send.clicked.connect(self.send_request)

    def show(self, /):
        if flight_plan_manager.flight_plan:
            plan = flight_plan_manager.flight_plan
            self.dep.setText(plan.dep)
            self.dest.setText(plan.arr)
            self.aircraft_type.setText(plan.aircraft)
        self.callsign.setText(config.callsign)
        super().show()

    def keyReleaseEvent(self, event, /):
        if event.key() == Qt.Key.Key_Enter:
            self.send_request()

    def send_request(self):
        if (target_station := self.target_station.text()) == "":
            self.target_station.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a station code.")
            return
        else:
            self.target_station.setStyleSheet("")
        if (dep_airport := self.dep.text()) == "":
            self.dep.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a departure airport.")
            return
        else:
            self.dep.setStyleSheet("")
        if (dest_airport := self.dest.text()) == "":
            self.dest.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a destination airport.")
            return
        else:
            self.dest.setStyleSheet("")
        if (aircraft_type := self.aircraft_type.text()) == "":
            self.aircraft_type.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a aircraft type.")
            return
        else:
            self.aircraft_type.setStyleSheet("")
        if (stand_number := self.stand_number.text()) == "":
            self.stand_number.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a stand number.")
            return
        else:
            self.stand_number.setStyleSheet("")
        cpdlc_manager.cpdlc.departure_clearance_delivery(target_station, aircraft_type, dest_airport, dep_airport,
                                                         stand_number, self.atis_letter.currentText())
        self.hide()
