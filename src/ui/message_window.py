from datetime import datetime
from threading import Semaphore
from typing import Optional

from PySide6.QtCore import QModelIndex, QUrl
from PySide6.QtGui import QBrush, QColor, QStandardItem, QStandardItemModel, Qt
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QPushButton, QStyledItemDelegate, QTableView, QWidget
from python_cpdlc import AcarsMessage, CPDLCMessage, MessageDirection, PacketType, ReplyTag

from .form.generate.message_window import Ui_MessageWindow
from ..config import config
from ..manager import cpdlc_manager
from ..meta import app_title


class MessageItem(QStandardItem):
    def __init__(self, message: AcarsMessage):
        super().__init__()
        self.message = message
        self.setText(message.message)

    def data(self, /, role=...):
        if role == Qt.ItemDataRole.UserRole + 1:
            return self.message
        return super().data(role)


class RowColorDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, data_column=0):
        super().__init__(parent)
        self.data_column = data_column

    def initStyleOption(self, option, index: QModelIndex):
        super().initStyleOption(option, index)
        decision_index = index.siblingAtColumn(self.data_column)
        if decision_index.isValid():
            data = decision_index.data(Qt.ItemDataRole.UserRole + 1)
            if isinstance(data, CPDLCMessage):
                if data.reply_type in [ReplyTag.WILCO_UNABLE,
                                       ReplyTag.AFFIRM_NEGATIVE,
                                       ReplyTag.ROGER]:
                    if data.has_replied:
                        option.backgroundBrush = QBrush(QColor(129, 212, 250))
                    else:
                        option.backgroundBrush = QBrush(QColor(129, 199, 132))


class MessageWindow(QWidget, Ui_MessageWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.reply_buttons = []
        self.model = QStandardItemModel()
        self.setupTable()
        self.message_details.hide()
        self.close_btn.clicked.connect(self.message_details.hide)
        self.delete_btn.setEnabled(False)
        self.delete_btn.clicked.connect(self.delete_message)
        self.delegate = RowColorDelegate(self.messages, 2)
        self.messages.setItemDelegate(self.delegate)
        self.sound = QSoundEffect()
        self.sound_playing = Semaphore(1)
        self.current_index: Optional[QModelIndex] = None
        self.sound.setSource(QUrl("qrc:/sound/notify"))
        self.sound.setVolume(1)
        self.setWindowTitle(app_title)
        cpdlc_manager.cpdlc.add_message_sender_callback(self.send_message)
        cpdlc_manager.cpdlc.add_message_receiver_callback(self.receive_message)

    def setupTable(self):
        self.model.setHorizontalHeaderLabels(["Dir", "Time", "Message"])
        self.messages.setModel(self.model)
        self.messages.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.messages.horizontalHeader().setStretchLastSection(True)
        self.messages.verticalHeader().setVisible(False)
        self.messages.setColumnWidth(0, 20)
        self.messages.setColumnWidth(1, 60)
        self.messages.setWordWrap(True)
        self.messages.clicked.connect(self.on_message_selected)
        self.messages.setStyleSheet("""
            QTableView {
                selection-background-color: #e6ee9c;
                selection-color: black;
            }
        """)

    def delete_message(self):
        if self.current_index is not None:
            self.model.removeRow(self.current_index.row())
        self.delete_btn.setEnabled(False)
        self.message_details.hide()

    def send_message(self, station: str, message: str):
        item = [QStandardItem("↑"), QStandardItem(datetime.now().strftime("%H:%M:%S")),
                MessageItem(AcarsMessage(station, PacketType.TELEX, message, MessageDirection.OUT))]
        item[0].setData(Qt.AlignmentFlag.AlignCenter, Qt.ItemDataRole.TextAlignmentRole)
        item[1].setData(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap,
                        Qt.ItemDataRole.TextAlignmentRole)
        self.model.insertRow(0, item)

    def receive_message(self, message: AcarsMessage):
        self.sound_playing.acquire()
        if not self.sound.isPlaying():
            self.sound.play()
        self.sound_playing.release()
        item = [QStandardItem("↓"), QStandardItem(message.timestamp.strftime("%H:%M:%S")), MessageItem(message)]
        item[0].setData(Qt.AlignmentFlag.AlignCenter, Qt.ItemDataRole.TextAlignmentRole)
        item[1].setData(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap,
                        Qt.ItemDataRole.TextAlignmentRole)
        self.model.insertRow(0, item)

    def on_message_selected(self, index: QModelIndex):
        data = index.data(Qt.ItemDataRole.UserRole + 1)
        if isinstance(data, AcarsMessage):
            self.current_index = None
            self.delete_btn.setEnabled(False)
            if data.direction == MessageDirection.IN:
                self.message_from.setText(data.target_station)
                self.to.setText(config.callsign)
            elif data.direction == MessageDirection.OUT:
                self.message_from.setText(config.callsign)
                self.to.setText(data.target_station)
            self.content.setText(data.message)
            if isinstance(data, CPDLCMessage):
                self.clear_reply_button()
                if data.request_for_reply and not data.has_replied:
                    match data.reply_type:
                        case ReplyTag.WILCO_UNABLE:
                            wilco_button = QPushButton("WILCO")
                            wilco_button.clicked.connect(lambda: self.reply_message(data, True))
                            self.buttons_layout.addWidget(wilco_button)
                            self.reply_buttons.append(wilco_button)
                            unable_button = QPushButton("UNABLE")
                            unable_button.clicked.connect(lambda: self.reply_message(data, False))
                            self.buttons_layout.addWidget(unable_button)
                            self.reply_buttons.append(unable_button)
                        case ReplyTag.AFFIRM_NEGATIVE:
                            affirm_button = QPushButton("AFFIRM")
                            affirm_button.clicked.connect(lambda: self.reply_message(data, True))
                            self.buttons_layout.addWidget(affirm_button)
                            self.reply_buttons.append(affirm_button)
                            negative_button = QPushButton("NEGATIVE")
                            negative_button.clicked.connect(lambda: self.reply_message(data, False))
                            self.buttons_layout.addWidget(negative_button)
                            self.reply_buttons.append(negative_button)
                        case ReplyTag.ROGER:
                            roger_button = QPushButton("ROGER")
                            roger_button.clicked.connect(lambda: self.reply_message(data, True))
                            self.buttons_layout.addWidget(roger_button)
                            self.reply_buttons.append(roger_button)
                        case _:
                            raise ValueError("Unknown replay type")
                else:
                    self.current_index = index
                    self.delete_btn.setEnabled(True)
            else:
                self.current_index = index
                self.delete_btn.setEnabled(True)
            self.message_details.show()
        else:
            self.message_details.hide()

    def clear_reply_button(self):
        for button in self.reply_buttons:
            self.buttons_layout.removeWidget(button)
            button.deleteLater()
        self.reply_buttons.clear()

    def reply_message(self, message: CPDLCMessage, status: bool):
        cpdlc_manager.cpdlc.reply_cpdlc_message(message, status)
        self.clear_reply_button()
        self.messages.clearSelection()
        self.message_details.hide()
