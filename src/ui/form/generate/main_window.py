# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QGroupBox,
                               QLabel, QMenuBar, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.ui.message_window import MessageWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 600)
        MainWindow.setMinimumSize(QSize(680, 600))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.option = QGroupBox(self.centralwidget)
        self.option.setObjectName(u"option")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.option.sizePolicy().hasHeightForWidth())
        self.option.setSizePolicy(sizePolicy)
        self.option.setMinimumSize(QSize(150, 0))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.message)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.message_2 = MessageWindow(self.message)
        self.message_2.setObjectName(u"message_2")

        self.verticalLayout_2.addWidget(self.message_2)


        self.gridLayout.addWidget(self.message, 1, 1, 1, 1)

        self.system_info = QGroupBox(self.centralwidget)
        self.system_info.setObjectName(u"system_info")
        sizePolicy1.setHeightForWidth(self.system_info.sizePolicy().hasHeightForWidth())
        self.system_info.setSizePolicy(sizePolicy1)
        self.system_info.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.system_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.system_info)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.network_select = QComboBox(self.system_info)
        self.network_select.setObjectName(u"network_select")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.network_select.sizePolicy().hasHeightForWidth())
        self.network_select.setSizePolicy(sizePolicy2)
        self.network_select.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.network_select, 1, 2, 1, 1)

        self.network = QLabel(self.system_info)
        self.network.setObjectName(u"network")
        self.network.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.network, 1, 1, 1, 1)

        self.label = QLabel(self.system_info)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.change_network_btn = QPushButton(self.system_info)
        self.change_network_btn.setObjectName(u"change_network_btn")
        sizePolicy2.setHeightForWidth(self.change_network_btn.sizePolicy().hasHeightForWidth())
        self.change_network_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.change_network_btn, 1, 3, 1, 1)

        self.label_1 = QLabel(self.system_info)
        self.label_1.setObjectName(u"label_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy3)
        self.label_1.setMinimumSize(QSize(60, 0))
        self.label_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_1, 2, 0, 1, 1)

        self.label_2 = QLabel(self.system_info)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.system_info)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_5 = QLabel(self.system_info)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.callsign = QLabel(self.system_info)
        self.callsign.setObjectName(u"callsign")
        sizePolicy1.setHeightForWidth(self.callsign.sizePolicy().hasHeightForWidth())
        self.callsign.setSizePolicy(sizePolicy1)
        self.callsign.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.callsign, 2, 1, 1, 4)

        self.cpdlc_status = QLabel(self.system_info)
        self.cpdlc_status.setObjectName(u"cpdlc_status")

        self.gridLayout_2.addWidget(self.cpdlc_status, 3, 1, 1, 4)

        self.atc_unit = QLabel(self.system_info)
        self.atc_unit.setObjectName(u"atc_unit")

        self.gridLayout_2.addWidget(self.atc_unit, 4, 1, 1, 4)

        self.atc_callsign = QLabel(self.system_info)
        self.atc_callsign.setObjectName(u"atc_callsign")

        self.gridLayout_2.addWidget(self.atc_callsign, 5, 1, 1, 4)

        self.acars_server_url = QLabel(self.system_info)
        self.acars_server_url.setObjectName(u"acars_server_url")

        self.gridLayout_2.addWidget(self.acars_server_url, 0, 1, 1, 4)


        self.gridLayout.addWidget(self.system_info, 0, 0, 1, 2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 680, 21))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimpleCPDLC", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.option.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
        self.telex_text.setText(QCoreApplication.translate("MainWindow", u"TELEX Text", None))
        self.dcl_request.setText(QCoreApplication.translate("MainWindow", u"DCL Request", None))
        self.cpdlc_logon.setText(QCoreApplication.translate("MainWindow", u"CPDLC Logon", None))
        self.meter.setText(QCoreApplication.translate("MainWindow", u"Meter", None))
        self.atis.setText(QCoreApplication.translate("MainWindow", u"ATIS", None))
        self.message.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.system_info.setTitle(QCoreApplication.translate("MainWindow", u"SystemInfo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ACARS server:", None))
        self.network.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ATC Unit:", None))
        self.change_network_btn.setText(QCoreApplication.translate("MainWindow", u"Change Network", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Callsign:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPDLC Status:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ATC Callsign:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ACARS Network:", None))
        self.callsign.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.cpdlc_status.setText(QCoreApplication.translate("MainWindow", u"no connection", None))
        self.atc_unit.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.atc_callsign.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.acars_server_url.setText(QCoreApplication.translate("MainWindow", u"http://www.hoppie.nl/acars/system", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2025-2025 Half_nothing. All rights reserved.", None))
    # retranslateUi

