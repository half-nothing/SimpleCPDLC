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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

from src.ui.message_window import MessageWindow
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(563, 460)
        MainWindow.setMinimumSize(QSize(563, 460))
        self.actionConfig = QAction(MainWindow)
        self.actionConfig.setObjectName(u"actionConfig")
        self.action_option = QAction(MainWindow)
        self.action_option.setObjectName(u"action_option")
        icon = QIcon()
        icon.addFile(u":/icon/settings", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_option.setIcon(icon)
        self.action_about_this = QAction(MainWindow)
        self.action_about_this.setObjectName(u"action_about_this")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.page_tab = QTabWidget(self.centralwidget)
        self.page_tab.setObjectName(u"page_tab")
        self.system_info_page = QWidget()
        self.system_info_page.setObjectName(u"system_info_page")
        self.gridLayout_6 = QGridLayout(self.system_info_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.atc_callsign = QLabel(self.system_info_page)
        self.atc_callsign.setObjectName(u"atc_callsign")

        self.gridLayout_6.addWidget(self.atc_callsign, 7, 1, 1, 1)

        self.label_1 = QLabel(self.system_info_page)
        self.label_1.setObjectName(u"label_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMinimumSize(QSize(60, 25))
        self.label_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.label_1, 4, 0, 1, 1)

        self.label_2 = QLabel(self.system_info_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))

        self.gridLayout_6.addWidget(self.label_2, 5, 0, 1, 1)

        self.change_network_btn = QPushButton(self.system_info_page)
        self.change_network_btn.setObjectName(u"change_network_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.change_network_btn.sizePolicy().hasHeightForWidth())
        self.change_network_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.change_network_btn, 2, 3, 1, 1)

        self.label_3 = QLabel(self.system_info_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))

        self.gridLayout_6.addWidget(self.label_3, 7, 0, 1, 1)

        self.cpdlc_status = QLabel(self.system_info_page)
        self.cpdlc_status.setObjectName(u"cpdlc_status")

        self.gridLayout_6.addWidget(self.cpdlc_status, 5, 1, 1, 1)

        self.network_select = QComboBox(self.system_info_page)
        self.network_select.setObjectName(u"network_select")
        sizePolicy1.setHeightForWidth(self.network_select.sizePolicy().hasHeightForWidth())
        self.network_select.setSizePolicy(sizePolicy1)
        self.network_select.setMinimumSize(QSize(100, 0))

        self.gridLayout_6.addWidget(self.network_select, 2, 2, 1, 1)

        self.callsign = QLabel(self.system_info_page)
        self.callsign.setObjectName(u"callsign")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.callsign.sizePolicy().hasHeightForWidth())
        self.callsign.setSizePolicy(sizePolicy2)
        self.callsign.setMinimumSize(QSize(100, 0))

        self.gridLayout_6.addWidget(self.callsign, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 10, 0, 1, 4)

        self.acars_server_url = QLabel(self.system_info_page)
        self.acars_server_url.setObjectName(u"acars_server_url")

        self.gridLayout_6.addWidget(self.acars_server_url, 0, 1, 2, 1)

        self.label_4 = QLabel(self.system_info_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 2, 1)

        self.network = QLabel(self.system_info_page)
        self.network.setObjectName(u"network")
        self.network.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.network, 2, 1, 1, 1)

        self.label_5 = QLabel(self.system_info_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))

        self.gridLayout_6.addWidget(self.label_5, 2, 0, 1, 1)

        self.label = QLabel(self.system_info_page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))

        self.gridLayout_6.addWidget(self.label, 6, 0, 1, 1)

        self.atc_unit = QLabel(self.system_info_page)
        self.atc_unit.setObjectName(u"atc_unit")

        self.gridLayout_6.addWidget(self.atc_unit, 6, 1, 1, 1)

        self.page_tab.addTab(self.system_info_page, "")
        self.flight_plan_page = QWidget()
        self.flight_plan_page.setObjectName(u"flight_plan_page")
        self.gridLayout_2 = QGridLayout(self.flight_plan_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.flight_plan_page)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(0, 25))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_15 = QLabel(self.flight_plan_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_9 = QLabel(self.flight_plan_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_11 = QLabel(self.flight_plan_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_13 = QLabel(self.flight_plan_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.aircraft_type = QLabel(self.flight_plan_page)
        self.aircraft_type.setObjectName(u"aircraft_type")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.aircraft_type.sizePolicy().hasHeightForWidth())
        self.aircraft_type.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.aircraft_type, 2, 2, 1, 1)

        self.simbrief_id = QLabel(self.flight_plan_page)
        self.simbrief_id.setObjectName(u"simbrief_id")
        sizePolicy4.setHeightForWidth(self.simbrief_id.sizePolicy().hasHeightForWidth())
        self.simbrief_id.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.simbrief_id, 0, 2, 1, 1)

        self.dep_airport = QLabel(self.flight_plan_page)
        self.dep_airport.setObjectName(u"dep_airport")

        self.gridLayout_2.addWidget(self.dep_airport, 1, 2, 1, 1)

        self.arr_airport = QLabel(self.flight_plan_page)
        self.arr_airport.setObjectName(u"arr_airport")

        self.gridLayout_2.addWidget(self.arr_airport, 3, 2, 1, 1)

        self.route = QLabel(self.flight_plan_page)
        self.route.setObjectName(u"route")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.route.sizePolicy().hasHeightForWidth())
        self.route.setSizePolicy(sizePolicy5)
        self.route.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.route, 4, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 5, 0, 1, 3)

        self.page_tab.addTab(self.flight_plan_page, "")

        self.gridLayout.addWidget(self.page_tab, 1, 0, 1, 2)

        self.message = QGroupBox(self.centralwidget)
        self.message.setObjectName(u"message")
        sizePolicy2.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.message)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.message_2 = MessageWindow(self.message)
        self.message_2.setObjectName(u"message_2")

        self.verticalLayout_2.addWidget(self.message_2)


        self.gridLayout.addWidget(self.message, 2, 1, 1, 1)

        self.option = QGroupBox(self.centralwidget)
        self.option.setObjectName(u"option")
        sizePolicy3.setHeightForWidth(self.option.sizePolicy().hasHeightForWidth())
        self.option.setSizePolicy(sizePolicy3)
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


        self.gridLayout.addWidget(self.option, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 563, 21))
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_option)
        self.menu_help.addAction(self.action_about_qt)
        self.menu_help.addAction(self.action_about_this)

        self.retranslateUi(MainWindow)

        self.page_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimpleCPDLC", None))
        self.actionConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.action_option.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.action_about_this.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
#if QT_CONFIG(tooltip)
        self.atc_callsign.setToolTip(QCoreApplication.translate("MainWindow", u"Current CPDLC Unit Callsign", None))
#endif // QT_CONFIG(tooltip)
        self.atc_callsign.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Callsign:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPDLC Status:", None))
        self.change_network_btn.setText(QCoreApplication.translate("MainWindow", u"Change Network", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ATC Callsign:", None))
#if QT_CONFIG(tooltip)
        self.cpdlc_status.setToolTip(QCoreApplication.translate("MainWindow", u"CPDLC Connection Status", None))
#endif // QT_CONFIG(tooltip)
        self.cpdlc_status.setText(QCoreApplication.translate("MainWindow", u"no connection", None))
#if QT_CONFIG(tooltip)
        self.callsign.setToolTip(QCoreApplication.translate("MainWindow", u"Using callsign", None))
#endif // QT_CONFIG(tooltip)
        self.callsign.setText(QCoreApplication.translate("MainWindow", u"----", None))
#if QT_CONFIG(tooltip)
        self.acars_server_url.setToolTip(QCoreApplication.translate("MainWindow", u"ACARS Server url", None))
#endif // QT_CONFIG(tooltip)
        self.acars_server_url.setText(QCoreApplication.translate("MainWindow", u"http://www.hoppie.nl/acars/system", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ACARS server:", None))
#if QT_CONFIG(tooltip)
        self.network.setToolTip(QCoreApplication.translate("MainWindow", u"Current ACARS Network", None))
#endif // QT_CONFIG(tooltip)
        self.network.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ACARS Network:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ATC Unit:", None))
#if QT_CONFIG(tooltip)
        self.atc_unit.setToolTip(QCoreApplication.translate("MainWindow", u"Current CPDLC Unit", None))
#endif // QT_CONFIG(tooltip)
        self.atc_unit.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.page_tab.setTabText(self.page_tab.indexOf(self.system_info_page), QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Simbrief ID:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Route:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dep Airport:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Arr Airport:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Aircraft type:", None))
        self.aircraft_type.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.simbrief_id.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.dep_airport.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.arr_airport.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.route.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.page_tab.setTabText(self.page_tab.indexOf(self.flight_plan_page), QCoreApplication.translate("MainWindow", u"Flight Plan", None))
        self.message.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.option.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
        self.telex_text.setText(QCoreApplication.translate("MainWindow", u"TELEX Text", None))
        self.dcl_request.setText(QCoreApplication.translate("MainWindow", u"DCL Request", None))
        self.cpdlc_logon.setText(QCoreApplication.translate("MainWindow", u"CPDLC Logon", None))
        self.meter.setText(QCoreApplication.translate("MainWindow", u"Meter", None))
        self.atis.setText(QCoreApplication.translate("MainWindow", u"ATIS", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

