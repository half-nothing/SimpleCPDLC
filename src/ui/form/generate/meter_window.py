# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meter_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QTableView)

class Ui_Meter(object):
    def setupUi(self, Meter):
        if not Meter.objectName():
            Meter.setObjectName(u"Meter")
        Meter.resize(400, 300)
        Meter.setMinimumSize(QSize(400, 300))
        self.gridLayout = QGridLayout(Meter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.target_airport = QLineEdit(Meter)
        self.target_airport.setObjectName(u"target_airport")
        self.target_airport.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.target_airport, 1, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 3)

        self.meter = QLabel(Meter)
        self.meter.setObjectName(u"meter")
        self.meter.setWordWrap(True)

        self.gridLayout.addWidget(self.meter, 2, 1, 1, 2)

        self.label_1 = QLabel(Meter)
        self.label_1.setObjectName(u"label_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

        self.historys = QTableView(Meter)
        self.historys.setObjectName(u"historys")

        self.gridLayout.addWidget(self.historys, 3, 0, 1, 3)

        self.send = QPushButton(Meter)
        self.send.setObjectName(u"send")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.send.sizePolicy().hasHeightForWidth())
        self.send.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.send, 4, 2, 1, 1)

        self.label_2 = QLabel(Meter)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 2)

        self.label = QLabel(Meter)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)


        self.retranslateUi(Meter)

        QMetaObject.connectSlotsByName(Meter)
    # setupUi

    def retranslateUi(self, Meter):
        Meter.setWindowTitle(QCoreApplication.translate("Meter", u"Meter", None))
        self.meter.setText(QCoreApplication.translate("Meter", u"----", None))
        self.label_1.setText(QCoreApplication.translate("Meter", u"Target Airport:", None))
        self.send.setText(QCoreApplication.translate("Meter", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("Meter", u"Meter:", None))
        self.label.setText(QCoreApplication.translate("Meter", u"Meter Query", None))
    # retranslateUi

