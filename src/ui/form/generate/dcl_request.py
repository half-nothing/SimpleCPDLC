# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dcl_request.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_DCL(object):
    def setupUi(self, DCL):
        if not DCL.objectName():
            DCL.setObjectName(u"DCL")
        DCL.resize(400, 242)
        DCL.setMinimumSize(QSize(400, 242))
        self.gridLayout = QGridLayout(DCL)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dest = QLineEdit(DCL)
        self.dest.setObjectName(u"dest")

        self.gridLayout.addWidget(self.dest, 3, 3, 1, 1)

        self.label = QLabel(DCL)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.label_3 = QLabel(DCL)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.stand_number = QLineEdit(DCL)
        self.stand_number.setObjectName(u"stand_number")

        self.gridLayout.addWidget(self.stand_number, 5, 1, 1, 1)

        self.callsign = QLabel(DCL)
        self.callsign.setObjectName(u"callsign")

        self.gridLayout.addWidget(self.callsign, 1, 1, 1, 3)

        self.label_7 = QLabel(DCL)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)

        self.label_5 = QLabel(DCL)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.atis_letter = QComboBox(DCL)
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.addItem("")
        self.atis_letter.setObjectName(u"atis_letter")

        self.gridLayout.addWidget(self.atis_letter, 6, 1, 1, 1)

        self.aircraft_type = QLineEdit(DCL)
        self.aircraft_type.setObjectName(u"aircraft_type")

        self.gridLayout.addWidget(self.aircraft_type, 4, 1, 1, 1)

        self.label_2 = QLabel(DCL)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 0, 1, 3)

        self.label_1 = QLabel(DCL)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 4)

        self.dep = QLineEdit(DCL)
        self.dep.setObjectName(u"dep")

        self.gridLayout.addWidget(self.dep, 3, 1, 1, 1)

        self.label_4 = QLabel(DCL)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_6 = QLabel(DCL)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.send = QPushButton(DCL)
        self.send.setObjectName(u"send")

        self.gridLayout.addWidget(self.send, 8, 3, 1, 1)

        self.target_station = QLineEdit(DCL)
        self.target_station.setObjectName(u"target_station")

        self.gridLayout.addWidget(self.target_station, 2, 1, 1, 1)


        self.retranslateUi(DCL)

        QMetaObject.connectSlotsByName(DCL)
    # setupUi

    def retranslateUi(self, DCL):
        DCL.setWindowTitle(QCoreApplication.translate("DCL", u"DCL Request", None))
        self.label.setText(QCoreApplication.translate("DCL", u"DCL Request Sender", None))
        self.label_3.setText(QCoreApplication.translate("DCL", u"Stand Number:", None))
        self.callsign.setText(QCoreApplication.translate("DCL", u"----", None))
        self.label_7.setText(QCoreApplication.translate("DCL", u"to", None))
        self.label_5.setText(QCoreApplication.translate("DCL", u"ATIS Letter:", None))
        self.atis_letter.setItemText(0, QCoreApplication.translate("DCL", u"A", None))
        self.atis_letter.setItemText(1, QCoreApplication.translate("DCL", u"B", None))
        self.atis_letter.setItemText(2, QCoreApplication.translate("DCL", u"C", None))
        self.atis_letter.setItemText(3, QCoreApplication.translate("DCL", u"D", None))
        self.atis_letter.setItemText(4, QCoreApplication.translate("DCL", u"E", None))
        self.atis_letter.setItemText(5, QCoreApplication.translate("DCL", u"F", None))
        self.atis_letter.setItemText(6, QCoreApplication.translate("DCL", u"G", None))
        self.atis_letter.setItemText(7, QCoreApplication.translate("DCL", u"H", None))
        self.atis_letter.setItemText(8, QCoreApplication.translate("DCL", u"I", None))
        self.atis_letter.setItemText(9, QCoreApplication.translate("DCL", u"J", None))
        self.atis_letter.setItemText(10, QCoreApplication.translate("DCL", u"K", None))
        self.atis_letter.setItemText(11, QCoreApplication.translate("DCL", u"L", None))
        self.atis_letter.setItemText(12, QCoreApplication.translate("DCL", u"M", None))
        self.atis_letter.setItemText(13, QCoreApplication.translate("DCL", u"N", None))
        self.atis_letter.setItemText(14, QCoreApplication.translate("DCL", u"O", None))
        self.atis_letter.setItemText(15, QCoreApplication.translate("DCL", u"P", None))
        self.atis_letter.setItemText(16, QCoreApplication.translate("DCL", u"Q", None))
        self.atis_letter.setItemText(17, QCoreApplication.translate("DCL", u"R", None))
        self.atis_letter.setItemText(18, QCoreApplication.translate("DCL", u"S", None))
        self.atis_letter.setItemText(19, QCoreApplication.translate("DCL", u"T", None))
        self.atis_letter.setItemText(20, QCoreApplication.translate("DCL", u"U", None))
        self.atis_letter.setItemText(21, QCoreApplication.translate("DCL", u"V", None))
        self.atis_letter.setItemText(22, QCoreApplication.translate("DCL", u"W", None))
        self.atis_letter.setItemText(23, QCoreApplication.translate("DCL", u"X", None))
        self.atis_letter.setItemText(24, QCoreApplication.translate("DCL", u"Y", None))
        self.atis_letter.setItemText(25, QCoreApplication.translate("DCL", u"Z", None))

        self.label_2.setText(QCoreApplication.translate("DCL", u"Callsign:", None))
        self.label_1.setText(QCoreApplication.translate("DCL", u"Aircraft Type:", None))
        self.label_4.setText(QCoreApplication.translate("DCL", u"Target Station:", None))
        self.label_6.setText(QCoreApplication.translate("DCL", u"Flight from", None))
        self.send.setText(QCoreApplication.translate("DCL", u"Send", None))
    # retranslateUi

