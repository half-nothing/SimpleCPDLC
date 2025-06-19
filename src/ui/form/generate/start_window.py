# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Start(object):
    def setupUi(self, Start):
        if not Start.objectName():
            Start.setObjectName(u"Start")
        Start.resize(399, 299)
        Start.setMinimumSize(QSize(399, 299))
        self.gridLayout = QGridLayout(Start)
        self.gridLayout.setObjectName(u"gridLayout")
        self.start = QPushButton(Start)
        self.start.setObjectName(u"start")

        self.gridLayout.addWidget(self.start, 10, 1, 1, 1)

        self.callsign = QLineEdit(Start)
        self.callsign.setObjectName(u"callsign")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.callsign.sizePolicy().hasHeightForWidth())
        self.callsign.setSizePolicy(sizePolicy)
        self.callsign.setMinimumSize(QSize(200, 0))
        self.callsign.setMaximumSize(QSize(16777215, 16777215))
        self.callsign.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.callsign, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label_3 = QLabel(Start)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 1, 1, 1)

        self.remember_me = QCheckBox(Start)
        self.remember_me.setObjectName(u"remember_me")

        self.gridLayout.addWidget(self.remember_me, 8, 1, 1, 1)

        self.email = QLineEdit(Start)
        self.email.setObjectName(u"email")

        self.gridLayout.addWidget(self.email, 5, 1, 1, 1)

        self.hoppie_code = QLineEdit(Start)
        self.hoppie_code.setObjectName(u"hoppie_code")

        self.gridLayout.addWidget(self.hoppie_code, 7, 1, 1, 1)

        self.label = QLabel(Start)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMargin(20)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_1 = QLabel(Start)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 3)

        self.label_2 = QLabel(Start)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"SimpleCPDLC", None))
        self.start.setText(QCoreApplication.translate("Start", u"Start", None))
        self.label_3.setText(QCoreApplication.translate("Start", u"HoppieCode", None))
        self.remember_me.setText(QCoreApplication.translate("Start", u"Remember me", None))
        self.label.setText(QCoreApplication.translate("Start", u"SimpleCPDLC", None))
        self.label_1.setText(QCoreApplication.translate("Start", u"Callsign", None))
        self.label_2.setText(QCoreApplication.translate("Start", u"Email", None))
    # retranslateUi

