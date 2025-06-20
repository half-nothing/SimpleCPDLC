import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QStyleFactory
from loguru import logger

import resource
from src.ui.main_window import MainWindow
from src.utils.logger import logger_init


def main() -> None:
    logger_init()
    logger.info("Application started")
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("light fusion"))
    app.setWindowIcon(QIcon(":/icon/icon"))
    MainWindow()
    exit_code = app.exec()
    resource.qCleanupResources()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
