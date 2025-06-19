# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telex_message_window.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_Telex(object):
    def setupUi(self, Telex):
        if not Telex.objectName():
            Telex.setObjectName(u"Telex")
        Telex.resize(401, 213)
        Telex.setMinimumSize(QSize(401, 213))
        self.gridLayout = QGridLayout(Telex)
        self.gridLayout.setObjectName(u"gridLayout")
        self.callsign = QLabel(Telex)
        self.callsign.setObjectName(u"callsign")

        self.gridLayout.addWidget(self.callsign, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 2)

        self.label_2 = QLabel(Telex)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.telex_content = QTextEdit(Telex)
        self.telex_content.setObjectName(u"telex_content")

        self.gridLayout.addWidget(self.telex_content, 3, 1, 1, 2)

        self.label = QLabel(Telex)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_3 = QLabel(Telex)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.send = QPushButton(Telex)
        self.send.setObjectName(u"send")
        self.send.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.send, 5, 2, 1, 1)

        self.target_station = QLineEdit(Telex)
        self.target_station.setObjectName(u"target_station")
        self.target_station.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.target_station, 2, 1, 1, 2)

        self.label_1 = QLabel(Telex)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 3)


        self.retranslateUi(Telex)

        QMetaObject.connectSlotsByName(Telex)
    # setupUi

    def retranslateUi(self, Telex):
        Telex.setWindowTitle(QCoreApplication.translate("Telex", u"Telex Message", None))
        self.callsign.setText(QCoreApplication.translate("Telex", u"----", None))
        self.label_2.setText(QCoreApplication.translate("Telex", u"Callsign:", None))
        self.label.setText(QCoreApplication.translate("Telex", u"Telex Message Sender", None))
        self.label_3.setText(QCoreApplication.translate("Telex", u"Telex Content:", None))
        self.send.setText(QCoreApplication.translate("Telex", u"Send", None))
        self.label_1.setText(QCoreApplication.translate("Telex", u"Target Station:", None))
    # retranslateUi

