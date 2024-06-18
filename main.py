# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import webbrowser
from pydub import AudioSegment


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QWidget, QFileDialog

from data.db import create_bd,   add_result
from core import main_thread


class BellMenu(QWidget):
    def __init__(self, lesson):
        super(BellMenu, self).__init__()
        self.setFixedSize(640, 520)

        self.lesson = lesson

        self.ui = uic.loadUi("./gui/menu.ui", self)
        self.label.setText("Звонок для " + str(self.lesson) + " урока")
        self.start_ui()

        self.start_choose.clicked.connect(self.add_start_music)
        self.end_choose.clicked.connect(self.add_end_music)
        self.dop_choose.clicked.connect(self.add_dop_music)

    def add_start_music(self):
        start_music_file = QFileDialog.getOpenFileName(
            parent=self,
            caption="Выберите файл",
            directory=os.getcwd(),
            filter="*.mp3"
        )

        postfix = start_music_file[0].split(".")[-1]
        if postfix.lower() != "mp3":
            box = QMessageBox.information(self, "Ошибка", "Файл должен быть с расширеньем mp3",
                                          QMessageBox.Ok, QMessageBox.Ok)
            return box
        else:
            file_name = start_music_file[0].split("/")[-1]
            self.ui.start_name.setText(file_name)

            new_path = self.make_waw_file(start_music_file[0], file_name)
            time = self.beautiful_time(self.start.time().hour(), self.start.time().minute())

            add_result(lesson=int(self.lesson), ring_number=1, time=time, path=new_path)

    def add_end_music(self):
        start_music_file = QFileDialog.getOpenFileName(
            parent=self,
            caption="Выберите файл",
            directory=os.getcwd(),
            filter="*.mp3"
        )

        postfix = start_music_file[0].split(".")[-1]
        if postfix.lower() != "mp3":
            box = QMessageBox.information(self, "Ошибка", "Файл должен быть с расширеньем mp3",
                                          QMessageBox.Ok, QMessageBox.Ok)
            return box
        else:
            file_name = start_music_file[0].split("/")[-1]
            self.ui.start_name.setText(file_name)

            new_path = self.make_waw_file(start_music_file[0], file_name)
            time = self.beautiful_time(self.start.time().hour(), self.start.time().minute())

            add_result(lesson=int(self.lesson), ring_number=2, time=time, path=new_path)

    def add_dop_music(self):
        start_music_file = QFileDialog.getOpenFileName(
            parent=self,
            caption="Выберите файл",
            directory=os.getcwd(),
            filter="*.mp3"
        )

        postfix = start_music_file[0].split(".")[-1]
        if postfix.lower() != "mp3":
            box = QMessageBox.information(self, "Ошибка", "Файл должен быть с расширеньем mp3",
                                          QMessageBox.Ok, QMessageBox.Ok)
            return box
        else:
            file_name = start_music_file[0].split("/")[-1]
            self.ui.start_name.setText(file_name)

            new_path = self.make_waw_file(start_music_file[0], file_name)
            time = self.beautiful_time(self.start.time().hour(), self.start.time().minute())

            add_result(lesson=int(self.lesson), ring_number=3, time=time, path=new_path)

    def start_ui(self):
        self.ui.show()

    @staticmethod
    def beautiful_time(hour, minute):
        if hour < 10:
            if minute < 10:
                result = f"0{hour}:0{minute}"
            else:
                result = f"0{hour}:{minute}"
        else:
            if minute < 10:
                result = f"{hour}:0{minute}"
            else:
                result = f"{hour}:{minute}"
        return result

    @staticmethod
    def make_waw_file(path, filename):
        sound = AudioSegment.from_mp3(path)
        new_path = f"./music/{filename}.waw"
        sound.export(new_path, format="wav")
        return new_path


class SupportWin(QDialog):
    def __init__(self):
        super(SupportWin, self).__init__()
        self.setFixedSize(380, 280)
        self.ui = uic.loadUi("./gui/support.ui", self)
        self.start_ui()

    def start_ui(self):
        self.ui.show()


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setFixedSize(900, 570)
        self.ui = uic.loadUi("./gui/main.ui", self)
        self.start_ui()
        create_bd()
        main_thread()

        self.dock.clicked.connect(self.show_docks)
        self.support.clicked.connect(self.show_support)
        self.developer.clicked.connect(self.show_developer)

        self.les0.clicked.connect(lambda: BellMenu(0))
        self.les1.clicked.connect(lambda: BellMenu(1))
        self.les2.clicked.connect(lambda: BellMenu(2))
        self.les3.clicked.connect(lambda: BellMenu(3))
        self.les4.clicked.connect(lambda: BellMenu(4))
        self.les5.clicked.connect(lambda: BellMenu(5))
        self.les6.clicked.connect(lambda: BellMenu(6))
        self.les7.clicked.connect(lambda: BellMenu(7))
        self.les8.clicked.connect(lambda: BellMenu(8))
        self.les9.clicked.connect(lambda: BellMenu(9))

    def start_ui(self):
        self.ui.show()

    @staticmethod
    def show_support():
        supp = SupportWin()

    @staticmethod
    def show_docks():
        webbrowser.open(r"https://github.com/whoiam143/SchoolBell/blob/main/README.md")

    @staticmethod
    def show_developer():
        webbrowser.open(r"https://github.com/whoiam143")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWin()
    ex.show()
    sys.exit(app.exec())
