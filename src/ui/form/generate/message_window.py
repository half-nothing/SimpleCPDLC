# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(399, 329)
        Form.setMinimumSize(QSize(399, 329))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.message_list = QFrame(Form)
        self.message_list.setObjectName(u"message_list")
        self.message_list.setMaximumSize(QSize(150, 16777215))
        self.message_list.setFrameShape(QFrame.Shape.StyledPanel)
        self.message_list.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.message_list)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.messages = QListWidget(self.message_list)
        self.messages.setObjectName(u"messages")
        self.messages.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.messages, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.message_list, 0, 0, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.content = QLabel(self.frame_2)
        self.content.setObjectName(u"content")
        self.content.setWordWrap(True)

        self.gridLayout_2.addWidget(self.content, 2, 1, 1, 1)

        self.to = QLabel(self.frame_2)
        self.to.setObjectName(u"to")

        self.gridLayout_2.addWidget(self.to, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 2)

        self.from = QLabel(self.frame_2)
        self.from.setObjectName(u"from")

        self.gridLayout_2.addWidget(self.from, 0, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_1 = QLabel(self.frame_2)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)

        self.buttons = QHBoxLayout()
        self.buttons.setObjectName(u"buttons")

        self.gridLayout_2.addLayout(self.buttons, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Message Window", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Content:", None))
        self.content.setText(QCoreApplication.translate("Form", u"----", None))
        self.to.setText(QCoreApplication.translate("Form", u"----", None))
        self.from.setText(QCoreApplication.translate("Form", u"----", None))
        self.label.setText(QCoreApplication.translate("Form", u"From:", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"To:", None))
    # retranslateUi

