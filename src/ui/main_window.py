from asyncio import run

from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from python_cpdlc import CPDLC, Network
from .form.generate.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cpdlc = CPDLC("halfnothingno@gmail.com", "9BWuJZBNLUyB9m")
        self.cpdlc.set_callsign("CES2352")
        self.cpdlc.change_network(Network.PDAsim)
        run(self.cpdlc.start_poller())

    def ccc(self):
        self.cpdlc.cpdlc_login("ZSHA")
