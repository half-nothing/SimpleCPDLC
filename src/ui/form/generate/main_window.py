# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from messagewindow import MessageWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.system_info = QGroupBox(self.centralwidget)
        self.system_info.setObjectName(u"system_info")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_info.sizePolicy().hasHeightForWidth())
        self.system_info.setSizePolicy(sizePolicy)
        self.system_info.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.system_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.system_info)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.atc_unit = QLabel(self.system_info)
        self.atc_unit.setObjectName(u"atc_unit")

        self.gridLayout_2.addWidget(self.atc_unit, 3, 1, 1, 2)

        self.atc_callsign = QLabel(self.system_info)
        self.atc_callsign.setObjectName(u"atc_callsign")

        self.gridLayout_2.addWidget(self.atc_callsign, 4, 1, 1, 2)

        self.label_1 = QLabel(self.system_info)
        self.label_1.setObjectName(u"label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy1)
        self.label_1.setMinimumSize(QSize(60, 0))
        self.label_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)

        self.label_3 = QLabel(self.system_info)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.cpdlc_status = QLabel(self.system_info)
        self.cpdlc_status.setObjectName(u"cpdlc_status")

        self.gridLayout_2.addWidget(self.cpdlc_status, 2, 1, 1, 2)

        self.label = QLabel(self.system_info)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.callsign = QLabel(self.system_info)
        self.callsign.setObjectName(u"callsign")
        sizePolicy.setHeightForWidth(self.callsign.sizePolicy().hasHeightForWidth())
        self.callsign.setSizePolicy(sizePolicy)
        self.callsign.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.callsign, 1, 1, 1, 2)

        self.label_4 = QLabel(self.system_info)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.acars_server_url = QLabel(self.system_info)
        self.acars_server_url.setObjectName(u"acars_server_url")

        self.gridLayout_2.addWidget(self.acars_server_url, 0, 1, 1, 2)


        self.gridLayout.addWidget(self.system_info, 0, 0, 1, 2)

        self.option = QGroupBox(self.centralwidget)
        self.option.setObjectName(u"option")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.option.sizePolicy().hasHeightForWidth())
        self.option.setSizePolicy(sizePolicy2)
        self.option.setMinimumSize(QSize(0, 0))
        self.option.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout = QVBoxLayout(self.option)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.telex_text = QPushButton(self.option)
        self.telex_text.setObjectName(u"telex_text")

        self.verticalLayout.addWidget(self.telex_text)

        self.dcl_request = QPushButton(self.option)
        self.dcl_request.setObjectName(u"dcl_request")

        self.verticalLayout.addWidget(self.dcl_request)

        self.cpdlc_logon = QPushButton(self.option)
        self.cpdlc_logon.setObjectName(u"cpdlc_logon")

        self.verticalLayout.addWidget(self.cpdlc_logon)

        self.meter = QPushButton(self.option)
        self.meter.setObjectName(u"meter")

        self.verticalLayout.addWidget(self.meter)

        self.atis = QPushButton(self.option)
        self.atis.setObjectName(u"atis")

        self.verticalLayout.addWidget(self.atis)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.option, 1, 0, 1, 1)

        self.message = QGroupBox(self.centralwidget)
        self.message.setObjectName(u"message")
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.message)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.message_2 = MessageWindow(self.message)
        self.message_2.setObjectName(u"message_2")

        self.verticalLayout_2.addWidget(self.message_2)


        self.gridLayout.addWidget(self.message, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimpleCPDLC", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.system_info.setTitle(QCoreApplication.translate("MainWindow", u"SystemInfo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPDLC Status:", None))
        self.atc_unit.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.atc_callsign.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Callsign:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ATC Callsign:", None))
        self.cpdlc_status.setText(QCoreApplication.translate("MainWindow", u"no connection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ATC Unit:", None))
        self.callsign.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ACARS server:", None))
        self.acars_server_url.setText(QCoreApplication.translate("MainWindow", u"http://www.hoppie.nl/acars/system", None))
        self.option.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
        self.telex_text.setText(QCoreApplication.translate("MainWindow", u"TELEX Text", None))
        self.dcl_request.setText(QCoreApplication.translate("MainWindow", u"DCL Request", None))
        self.cpdlc_logon.setText(QCoreApplication.translate("MainWindow", u"CPDLC Logon", None))
        self.meter.setText(QCoreApplication.translate("MainWindow", u"Meter", None))
        self.atis.setText(QCoreApplication.translate("MainWindow", u"ATIS", None))
        self.message.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
    # retranslateUi

