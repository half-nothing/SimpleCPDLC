# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atis_window.ui'
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

class Ui_ATIS(object):
    def setupUi(self, ATIS):
        if not ATIS.objectName():
            ATIS.setObjectName(u"ATIS")
        ATIS.resize(400, 163)
        ATIS.setMinimumSize(QSize(400, 163))
        self.gridLayout = QGridLayout(ATIS)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(ATIS)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(ATIS)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.atis = QLabel(ATIS)
        self.atis.setObjectName(u"atis")
        self.atis.setWordWrap(True)

        self.gridLayout.addWidget(self.atis, 3, 1, 1, 2)

        self.target_airport = QLineEdit(ATIS)
        self.target_airport.setObjectName(u"target_airport")
        self.target_airport.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.target_airport, 1, 1, 1, 2)

        self.pushButton = QPushButton(ATIS)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)

        self.label_1 = QLabel(ATIS)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

        self.label_3 = QLabel(ATIS)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 3)

        self.platform = QComboBox(ATIS)
        self.platform.addItem("")
        self.platform.addItem("")
        self.platform.addItem("")
        self.platform.setObjectName(u"platform")
        self.platform.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.platform, 2, 1, 1, 2)


        self.retranslateUi(ATIS)

        QMetaObject.connectSlotsByName(ATIS)
    # setupUi

    def retranslateUi(self, ATIS):
        ATIS.setWindowTitle(QCoreApplication.translate("ATIS", u"ATIS", None))
        self.label_2.setText(QCoreApplication.translate("ATIS", u"ATIS Info:", None))
        self.label.setText(QCoreApplication.translate("ATIS", u"ATIS Query", None))
        self.atis.setText(QCoreApplication.translate("ATIS", u"----", None))
        self.pushButton.setText(QCoreApplication.translate("ATIS", u"Send", None))
        self.label_1.setText(QCoreApplication.translate("ATIS", u"Target Airport:", None))
        self.label_3.setText(QCoreApplication.translate("ATIS", u"Platform:", None))
        self.platform.setItemText(0, QCoreApplication.translate("ATIS", u"VATSIM", None))
        self.platform.setItemText(1, QCoreApplication.translate("ATIS", u"PilotEdge", None))
        self.platform.setItemText(2, QCoreApplication.translate("ATIS", u"IVAO", None))

    # retranslateUi

