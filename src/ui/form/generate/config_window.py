# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(392, 224)
        self.gridLayout_2 = QGridLayout(Config)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btns = QHBoxLayout()
        self.btns.setObjectName(u"btns")
        self.ok_btn = QPushButton(Config)
        self.ok_btn.setObjectName(u"ok_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)

        self.btns.addWidget(self.ok_btn)

        self.apply_btn = QPushButton(Config)
        self.apply_btn.setObjectName(u"apply_btn")

        self.btns.addWidget(self.apply_btn)

        self.cancel_btn = QPushButton(Config)
        self.cancel_btn.setObjectName(u"cancel_btn")
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)

        self.btns.addWidget(self.cancel_btn)


        self.gridLayout_2.addLayout(self.btns, 8, 1, 1, 2)

        self.label = QLabel(Config)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.hoppie_code = QLineEdit(Config)
        self.hoppie_code.setObjectName(u"hoppie_code")

        self.gridLayout_2.addWidget(self.hoppie_code, 6, 1, 1, 2)

        self.label_5 = QLabel(Config)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.simbrief_id = QLineEdit(Config)
        self.simbrief_id.setObjectName(u"simbrief_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.simbrief_id.sizePolicy().hasHeightForWidth())
        self.simbrief_id.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.simbrief_id, 7, 1, 1, 2)

        self.callsign = QLineEdit(Config)
        self.callsign.setObjectName(u"callsign")

        self.gridLayout_2.addWidget(self.callsign, 4, 1, 1, 2)

        self.label_3 = QLabel(Config)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_7 = QLabel(Config)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.email = QLineEdit(Config)
        self.email.setObjectName(u"email")

        self.gridLayout_2.addWidget(self.email, 5, 1, 1, 2)

        self.debug_mode = QCheckBox(Config)
        self.debug_mode.setObjectName(u"debug_mode")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.debug_mode.sizePolicy().hasHeightForWidth())
        self.debug_mode.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.debug_mode, 2, 2, 1, 1)

        self.log_level = QComboBox(Config)
        self.log_level.addItem("")
        self.log_level.addItem("")
        self.log_level.addItem("")
        self.log_level.addItem("")
        self.log_level.addItem("")
        self.log_level.addItem("")
        self.log_level.addItem("")
        self.log_level.setObjectName(u"log_level")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.log_level.sizePolicy().hasHeightForWidth())
        self.log_level.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.log_level, 2, 1, 1, 1)

        self.label_2 = QLabel(Config)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_4 = QLabel(Config)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)

        self.version = QLabel(Config)
        self.version.setObjectName(u"version")

        self.gridLayout_2.addWidget(self.version, 0, 1, 1, 1)

        self.remember_me = QCheckBox(Config)
        self.remember_me.setObjectName(u"remember_me")

        self.gridLayout_2.addWidget(self.remember_me, 0, 2, 1, 1)


        self.retranslateUi(Config)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"Config", None))
        self.ok_btn.setText(QCoreApplication.translate("Config", u"Ok", None))
        self.apply_btn.setText(QCoreApplication.translate("Config", u"Apply", None))
        self.cancel_btn.setText(QCoreApplication.translate("Config", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Config", u"Callsign", None))
        self.label_5.setText(QCoreApplication.translate("Config", u"Config Version:", None))
        self.label_3.setText(QCoreApplication.translate("Config", u"HoppieCode", None))
        self.label_7.setText(QCoreApplication.translate("Config", u"Log Level:", None))
        self.debug_mode.setText(QCoreApplication.translate("Config", u"Debug Mode", None))
        self.log_level.setItemText(0, QCoreApplication.translate("Config", u"TRACE", None))
        self.log_level.setItemText(1, QCoreApplication.translate("Config", u"DEBUG", None))
        self.log_level.setItemText(2, QCoreApplication.translate("Config", u"INFO", None))
        self.log_level.setItemText(3, QCoreApplication.translate("Config", u"SUCCESS", None))
        self.log_level.setItemText(4, QCoreApplication.translate("Config", u"WARNING", None))
        self.log_level.setItemText(5, QCoreApplication.translate("Config", u"ERROR", None))
        self.log_level.setItemText(6, QCoreApplication.translate("Config", u"CRITICAL", None))

        self.label_2.setText(QCoreApplication.translate("Config", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("Config", u"Simbrief ID", None))
        self.version.setText(QCoreApplication.translate("Config", u"1.0.0", None))
        self.remember_me.setText(QCoreApplication.translate("Config", u"Remember me", None))
    # retranslateUi

