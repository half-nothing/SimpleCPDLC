# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpdlc_connect_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 136)
        Login.setMinimumSize(QSize(400, 136))
        self.gridLayout = QGridLayout(Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 2)

        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.send = QPushButton(Login)
        self.send.setObjectName(u"send")

        self.gridLayout.addWidget(self.send, 3, 2, 1, 1)

        self.callsign = QLabel(Login)
        self.callsign.setObjectName(u"callsign")

        self.gridLayout.addWidget(self.callsign, 1, 1, 1, 2)

        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_1 = QLabel(Login)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.target_station = QLineEdit(Login)
        self.target_station.setObjectName(u"target_station")
        self.target_station.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.target_station, 2, 1, 1, 2)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"CPDLC", None))
        self.label.setText(QCoreApplication.translate("Login", u"CPDLC Connect Request Sender", None))
        self.send.setText(QCoreApplication.translate("Login", u"Send", None))
        self.callsign.setText(QCoreApplication.translate("Login", u"----", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Target Station:", None))
        self.label_1.setText(QCoreApplication.translate("Login", u"Callsign:", None))
    # retranslateUi

