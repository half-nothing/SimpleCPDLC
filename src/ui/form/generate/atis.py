# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atis.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 163)
        Form.setMinimumSize(QSize(400, 163))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.atis = QLabel(Form)
        self.atis.setObjectName(u"atis")
        self.atis.setWordWrap(True)

        self.gridLayout.addWidget(self.atis, 3, 1, 1, 2)

        self.target_airport = QLineEdit(Form)
        self.target_airport.setObjectName(u"target_airport")
        self.target_airport.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.target_airport, 1, 1, 1, 2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)

        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 3)

        self.platform = QComboBox(Form)
        self.platform.addItem("")
        self.platform.addItem("")
        self.platform.addItem("")
        self.platform.setObjectName(u"platform")
        self.platform.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.platform, 2, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"ATIS", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ATIS Info:", None))
        self.label.setText(QCoreApplication.translate("Form", u"ATIS Query", None))
        self.atis.setText(QCoreApplication.translate("Form", u"----", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Send", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"Target Airport:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Platform:", None))
        self.platform.setItemText(0, QCoreApplication.translate("Form", u"VATSIM", None))
        self.platform.setItemText(1, QCoreApplication.translate("Form", u"PilotEdge", None))
        self.platform.setItemText(2, QCoreApplication.translate("Form", u"IVAO", None))

    # retranslateUi

