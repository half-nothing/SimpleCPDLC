from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMessageBox, QTableView, QWidget
from python_cpdlc import InfoType

from .form.generate.meter_window import Ui_Meter
from ..cpdlc import cpdlc_manager


class MeterWindow(QWidget, Ui_Meter):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.send.clicked.connect(self.query_meter)
        self.model = QStandardItemModel()
        self.setupTable()

    def setupTable(self):
        self.model.setHorizontalHeaderLabels(["Time", "Meter"])
        self.historys.setModel(self.model)
        self.historys.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.historys.horizontalHeader().setStretchLastSection(True)
        self.historys.verticalHeader().setVisible(False)
        self.historys.setColumnWidth(0, 60)
        self.historys.setWordWrap(True)

    def query_meter(self):
        if self.target_airport.text() == "":
            self.target_airport.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a target airport.")
            return
        else:
            self.target_airport.setStyleSheet("")
        res = cpdlc_manager.cpdlc.query_info(InfoType.METAR, self.target_airport.text().upper())
        self.meter.setText(res.message)
        item = [QStandardItem(datetime.now().strftime("%H:%M:%S")), QStandardItem(res.message)]
        item[0].setData(Qt.AlignmentFlag.AlignCenter, Qt.ItemDataRole.TextAlignmentRole)
        item[1].setData(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap,
                        Qt.ItemDataRole.TextAlignmentRole)
        self.model.insertRow(0, item)
        self.historys.resizeRowToContents(0)

    def resizeEvent(self, event, /):
        self.historys.resizeRowsToContents()
        super().resizeEvent(event)
