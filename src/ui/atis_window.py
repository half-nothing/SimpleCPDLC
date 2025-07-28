from datetime import datetime
from enum import Enum

from PySide6.QtGui import QStandardItem, QStandardItemModel, Qt
from PySide6.QtWidgets import QMessageBox, QTableView, QWidget
from python_cpdlc.enums import InfoType
from python_cpdlc.cpdlc_message import AcarsMessage

from .form.generate.atis_window import Ui_ATIS
from ..manager import cpdlc_manager


class Platform(Enum):
    VATSIM = "VATSIM"
    PE = "PilotEdge"
    IVAO = "IVAO"


class ATISWindow(QWidget, Ui_ATIS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for platform in Platform:
            self.platform.addItem(platform.value)
        self.model = QStandardItemModel()
        self.setupTable()
        self.send.clicked.connect(self.query_atis)

    def setupTable(self):
        self.model.setHorizontalHeaderLabels(["Time", "ATIS"])
        self.historys.setModel(self.model)
        self.historys.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.historys.horizontalHeader().setStretchLastSection(True)
        self.historys.verticalHeader().setVisible(False)
        self.historys.setColumnWidth(0, 60)
        self.historys.setWordWrap(True)

    def query_atis(self):
        if self.target_airport.text() == "":
            self.target_airport.setStyleSheet("background-color: #ef9a9a;color: white")
            QMessageBox.critical(self, "Error", "Please enter a target airport.")
            return
        else:
            self.target_airport.setStyleSheet("")
        res: AcarsMessage
        match Platform(self.platform.currentText()):
            case Platform.IVAO:
                res = cpdlc_manager.cpdlc.query_info(InfoType.IVAO_ATIS, self.target_airport.text().upper())
            case Platform.PE:
                res = cpdlc_manager.cpdlc.query_info(InfoType.PE_ATIS, self.target_airport.text().upper())
            case Platform.VATSIM:
                res = cpdlc_manager.cpdlc.query_info(InfoType.VAT_ATIS, self.target_airport.text().upper())
            case _:
                raise ValueError()
        self.atis.setText(res.message)
        item = [QStandardItem(datetime.now().strftime("%H:%M:%S")), QStandardItem(res.message)]
        item[0].setData(Qt.AlignmentFlag.AlignCenter, Qt.ItemDataRole.TextAlignmentRole)
        item[1].setData(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap,
                        Qt.ItemDataRole.TextAlignmentRole)
        self.model.insertRow(0, item)
        self.historys.resizeRowToContents(0)
