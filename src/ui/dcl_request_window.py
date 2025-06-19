from PySide6.QtWidgets import QWidget

from .form.generate.dcl_request_window import Ui_DCL


class DCLRequestWindow(QWidget, Ui_DCL):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
