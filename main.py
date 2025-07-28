import sys
import time
from threading import Thread

from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QStyleFactory
from loguru import logger

from src.manager import cpdlc_manager


def main() -> None:
    from src.utils.logger import logger_init
    logger_init()

    start_time = time.time()
    logger.info("Application initializing")

    logger.trace("Creating application")
    Thread(target=lambda: cpdlc_manager.cpdlc.client, daemon=True).start()
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("light fusion"))
    app.setFont(QFont("Leelawadee UI", 9))
    logger.trace(f"Application created on {time.time() - start_time:.2f}s")

    logger.trace("Importing resource")
    import resource_rc
    app.setWindowIcon(QIcon(":/icon/icon"))
    logger.trace(f"Resource imported on {time.time() - start_time:.2f}s")

    logger.trace("Creating main window")
    from src.ui.main_window import MainWindow
    MainWindow()
    logger.trace(f"Main window created on {time.time() - start_time:.2f}s")

    logger.info(f"Startup completed in {time.time() - start_time:.2f}s")
    exit_code = app.exec()
    resource_rc.qCleanupResources()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
