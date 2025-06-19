# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meter_window.ui'
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

class Ui_Meter(object):
    def setupUi(self, Meter):
        if not Meter.objectName():
            Meter.setObjectName(u"Meter")
        Meter.resize(400, 136)
        Meter.setMinimumSize(QSize(400, 136))
        self.gridLayout = QGridLayout(Meter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_1 = QLabel(Meter)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

        self.send = QPushButton(Meter)
        self.send.setObjectName(u"send")

        self.gridLayout.addWidget(self.send, 3, 2, 1, 1)

        self.meter = QLabel(Meter)
        self.meter.setObjectName(u"meter")
        self.meter.setWordWrap(True)

        self.gridLayout.addWidget(self.meter, 2, 1, 1, 2)

        self.label = QLabel(Meter)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 2)

        self.target_airport = QLineEdit(Meter)
        self.target_airport.setObjectName(u"target_airport")
        self.target_airport.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.target_airport, 1, 1, 1, 2)

        self.label_2 = QLabel(Meter)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)


        self.retranslateUi(Meter)

        QMetaObject.connectSlotsByName(Meter)
    # setupUi

    def retranslateUi(self, Meter):
        Meter.setWindowTitle(QCoreApplication.translate("Meter", u"Meter", None))
        self.label_1.setText(QCoreApplication.translate("Meter", u"Target Airport:", None))
        self.send.setText(QCoreApplication.translate("Meter", u"Send", None))
        self.meter.setText(QCoreApplication.translate("Meter", u"----", None))
        self.label.setText(QCoreApplication.translate("Meter", u"Meter Query", None))
        self.label_2.setText(QCoreApplication.translate("Meter", u"Meter:", None))
    # retranslateUi

