import sys

from PySide6.QtWidgets import QApplication, QStyleFactory
from loguru import logger

from src.ui.main_window import MainWindow
from src.utils.logger import logger_init

import resource


def main() -> None:
    logger_init()
    logger.info("Application started")
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("light fusion"))
    MainWindow()
    exit_code = app.exec()
    resource.qCleanupResources()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
