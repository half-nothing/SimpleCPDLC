import sys

from PySide6.QtWidgets import QApplication, QStyleFactory

from src.ui.main_window import MainWindow
from src.utils import logger


def main() -> None:
    logger.info("Application started")
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("light fusion"))
    MainWindow()
    exit(app.exec())


if __name__ == '__main__':
    main()
