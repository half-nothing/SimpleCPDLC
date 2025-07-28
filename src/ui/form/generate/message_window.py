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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QWidget)

class Ui_MessageWindow(object):
    def setupUi(self, MessageWindow):
        if not MessageWindow.objectName():
            MessageWindow.setObjectName(u"MessageWindow")
        MessageWindow.resize(356, 175)
        MessageWindow.setMinimumSize(QSize(356, 175))
        self.gridLayout = QGridLayout(MessageWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.message_list = QFrame(MessageWindow)
        self.message_list.setObjectName(u"message_list")
        self.message_list.setMinimumSize(QSize(230, 0))
        self.message_list.setMaximumSize(QSize(16777215, 16777215))
        self.message_list.setFrameShape(QFrame.Shape.StyledPanel)
        self.message_list.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.message_list)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.messages = QTableView(self.message_list)
        self.messages.setObjectName(u"messages")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messages.sizePolicy().hasHeightForWidth())
        self.messages.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.messages, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.message_list, 0, 0, 1, 1)

        self.message_details = QFrame(MessageWindow)
        self.message_details.setObjectName(u"message_details")
        self.message_details.setFrameShape(QFrame.Shape.StyledPanel)
        self.message_details.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.message_details)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.message_details)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.message_details)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_1 = QLabel(self.message_details)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")

        self.gridLayout_2.addLayout(self.buttons_layout, 4, 0, 1, 2)

        self.message_from = QLabel(self.message_details)
        self.message_from.setObjectName(u"message_from")

        self.gridLayout_2.addWidget(self.message_from, 0, 1, 1, 1)

        self.to = QLabel(self.message_details)
        self.to.setObjectName(u"to")

        self.gridLayout_2.addWidget(self.to, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.content = QLabel(self.message_details)
        self.content.setObjectName(u"content")
        self.content.setWordWrap(True)

        self.gridLayout_2.addWidget(self.content, 2, 1, 1, 1)

        self.close_btn = QPushButton(self.message_details)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.close_btn, 7, 0, 1, 2)

        self.delete_btn = QPushButton(self.message_details)
        self.delete_btn.setObjectName(u"delete_btn")

        self.gridLayout_2.addWidget(self.delete_btn, 6, 0, 1, 2)


        self.gridLayout.addWidget(self.message_details, 0, 1, 1, 1)


        self.retranslateUi(MessageWindow)

        QMetaObject.connectSlotsByName(MessageWindow)
    # setupUi

    def retranslateUi(self, MessageWindow):
        MessageWindow.setWindowTitle(QCoreApplication.translate("MessageWindow", u"Message Window", None))
        self.label_2.setText(QCoreApplication.translate("MessageWindow", u"Content:", None))
        self.label.setText(QCoreApplication.translate("MessageWindow", u"From:", None))
        self.label_1.setText(QCoreApplication.translate("MessageWindow", u"To:", None))
        self.message_from.setText(QCoreApplication.translate("MessageWindow", u"----", None))
        self.to.setText(QCoreApplication.translate("MessageWindow", u"----", None))
        self.content.setText(QCoreApplication.translate("MessageWindow", u"----", None))
        self.close_btn.setText(QCoreApplication.translate("MessageWindow", u"Close", None))
        self.delete_btn.setText(QCoreApplication.translate("MessageWindow", u"Delete", None))
    # retranslateUi

