
import pickle

from PyQt5.QtWidgets import QMessageBox, QErrorMessage

import NoteMachine_Class

from PyQt5 import QtCore, QtGui, QtWidgets



class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def closeEvent(self, event):
        with open("Notes.pkl", "wb") as file:
            pickle.dump(NoteMachine_Class.tasks, file)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 740)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_Button.setGeometry(QtCore.QRect(0, 209, 900, 101))
        self.add_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                      "font: 40pt \"Calibri\";")
        self.add_Button.setObjectName("add_Button")
        self.Msg_Input = QtWidgets.QTextEdit(self.centralwidget)
        self.Msg_Input.setGeometry(QtCore.QRect(209, 140, 691, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Msg_Input.setFont(font)
        self.Msg_Input.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                     "font: 12pt \"Calibri\";")
        self.Msg_Input.setObjectName("Msg_Input")
        self.Msg_Lable = QtWidgets.QLabel(self.centralwidget)
        self.Msg_Lable.setGeometry(QtCore.QRect(0, 140, 211, 75))
        self.Msg_Lable.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                     "font: 32pt \"Calibri\";")
        self.Msg_Lable.setObjectName("Msg_Lable")
        self.Notes_Label = QtWidgets.QLabel(self.centralwidget)
        self.Notes_Label.setGeometry(QtCore.QRect(0, 70, 211, 75))
        self.Notes_Label.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                       "font: 32pt \"Calibri\";")
        self.Notes_Label.setObjectName("Notes_Label")
        self.Time_Lable = QtWidgets.QLabel(self.centralwidget)
        self.Time_Lable.setGeometry(QtCore.QRect(0, 0, 211, 75))
        self.Time_Lable.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                      "font: 32pt \"Calibri\";")
        self.Time_Lable.setObjectName("Time_Lable")
        self.Time_Table = QtWidgets.QLabel(self.centralwidget)
        self.Time_Table.setGeometry(QtCore.QRect(0, 310, 191, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Time_Table.setFont(font)
        self.Time_Table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Time_Table.setObjectName("Time_Table")
        self.Notes_Table = QtWidgets.QLabel(self.centralwidget)
        self.Notes_Table.setGeometry(QtCore.QRect(189, 310, 321, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Notes_Table.setFont(font)
        self.Notes_Table.setStyleSheet("\n"
                                       "background-color: rgb(255, 255, 255);")
        self.Notes_Table.setTextFormat(QtCore.Qt.AutoText)
        self.Notes_Table.setScaledContents(True)
        self.Notes_Table.setObjectName("Notes_Table")
        self.Msg_Table = QtWidgets.QLabel(self.centralwidget)
        self.Msg_Table.setGeometry(QtCore.QRect(509, 310, 391, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Msg_Table.setFont(font)
        self.Msg_Table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Table.setObjectName("Msg_Table")
        self.Time_1 = QtWidgets.QLabel(self.centralwidget)
        self.Time_1.setGeometry(QtCore.QRect(0, 410, 191, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.Time_1.setFont(font)
        self.Time_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Time_1.setObjectName("Time_1")
        self.Notes_1 = QtWidgets.QLabel(self.centralwidget)
        self.Notes_1.setGeometry(QtCore.QRect(190, 410, 321, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Notes_1.setFont(font)
        self.Notes_1.setStyleSheet("\n"
                                   "border-color: rgb(255, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.Notes_1.setText("")
        self.Notes_1.setObjectName("Notes_1")
        self.Msg_1 = QtWidgets.QLabel(self.centralwidget)
        self.Msg_1.setGeometry(QtCore.QRect(509, 410, 291, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Msg_1.setFont(font)
        self.Msg_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_1.setText("")
        self.Msg_1.setObjectName("Msg_1")
        self.Notes_2 = QtWidgets.QLabel(self.centralwidget)
        self.Notes_2.setGeometry(QtCore.QRect(190, 510, 321, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Notes_2.setFont(font)
        self.Notes_2.setStyleSheet("\n"
                                   "background-color: rgb(255, 255, 255);")
        self.Notes_2.setText("")
        self.Notes_2.setObjectName("Notes_2")
        self.Time_2 = QtWidgets.QLabel(self.centralwidget)
        self.Time_2.setGeometry(QtCore.QRect(0, 510, 191, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.Time_2.setFont(font)
        self.Time_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Time_2.setObjectName("Time_2")
        self.Msg_2 = QtWidgets.QLabel(self.centralwidget)
        self.Msg_2.setGeometry(QtCore.QRect(509, 510, 291, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Msg_2.setFont(font)
        self.Msg_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_2.setText("")
        self.Msg_2.setObjectName("Msg_2")
        self.Notes_3 = QtWidgets.QLabel(self.centralwidget)
        self.Notes_3.setGeometry(QtCore.QRect(190, 610, 321, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Notes_3.setFont(font)
        self.Notes_3.setStyleSheet("\n"
                                   "background-color: rgb(255, 255, 255);")
        self.Notes_3.setText("")
        self.Notes_3.setObjectName("Notes_3")
        self.Time_3 = QtWidgets.QLabel(self.centralwidget)
        self.Time_3.setGeometry(QtCore.QRect(0, 610, 191, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.Time_3.setFont(font)
        self.Time_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Time_3.setObjectName("Time_3")
        self.Msg_3 = QtWidgets.QLabel(self.centralwidget)
        self.Msg_3.setGeometry(QtCore.QRect(509, 610, 291, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Msg_3.setFont(font)
        self.Msg_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_3.setText("")
        self.Msg_3.setObjectName("Msg_3")
        self.del_Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.del_Button1.setGeometry(QtCore.QRect(800, 410, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.del_Button1.setFont(font)
        self.del_Button1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.del_Button1.setObjectName("del_Button1")
        self.del_Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.del_Button2.setGeometry(QtCore.QRect(800, 510, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.del_Button2.setFont(font)
        self.del_Button2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.del_Button2.setObjectName("del_Button2")
        self.del_Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.del_Button3.setGeometry(QtCore.QRect(800, 610, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.del_Button3.setFont(font)
        self.del_Button3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.del_Button3.setObjectName("del_Button3")
        self.Notes_Input_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Notes_Input_2.setGeometry(QtCore.QRect(209, 70, 691, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Notes_Input_2.setFont(font)
        self.Notes_Input_2.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                         "font: 32pt \"Calibri\";")
        self.Notes_Input_2.setObjectName("Notes_Input_2")
        self.Time_Input = QtWidgets.QTextEdit(self.centralwidget)
        self.Time_Input.setGeometry(QtCore.QRect(209, 0, 691, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time_Input.setFont(font)
        self.Time_Input.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                      "font: 32pt \"Calibri\";")
        self.Time_Input.setObjectName("Time_Input")
        self.Time_Lable.raise_()
        self.Msg_Lable.raise_()
        self.Notes_Label.raise_()
        self.Time_Input.raise_()
        self.Notes_Input_2.raise_()
        self.add_Button.raise_()
        self.Msg_Input.raise_()
        self.Time_Table.raise_()
        self.Notes_Table.raise_()
        self.Msg_Table.raise_()
        self.Time_1.raise_()
        self.Notes_1.raise_()
        self.Msg_1.raise_()
        self.Notes_2.raise_()
        self.Time_2.raise_()
        self.Msg_2.raise_()
        self.Notes_3.raise_()
        self.Time_3.raise_()
        self.Msg_3.raise_()
        self.del_Button1.raise_()
        self.del_Button2.raise_()
        self.del_Button3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.note_count = 0
        try:
            with open("Notes.pkl", "rb") as file:
                NoteMachine_Class.tasks = pickle.load(file)
                for i in range(0, 3):
                    if i in NoteMachine_Class.tasks:
                        a = NoteMachine_Class.tasks[i]
                        if i == 0 :
                            self.Time_1.setText(a.time)
                            self.Notes_1.setText(a.notes)
                            self.Msg_1.setText(a.msg)
                        elif i == 1:
                            self.Time_2.setText(a.time)
                            self.Notes_2.setText(a.notes)
                            self.Msg_2.setText(a.msg)
                        elif i == 2:
                            self.Time_3.setText(a.time)
                            self.Notes_3.setText(a.notes)
                            self.Msg_3.setText(a.msg)
                        else:
                            error = QMessageBox()
                            error.setWindowTitle("Error")
                            error.setText("Very more tasks, delete some one")
                            error.exec_()
                        self.note_count += 1
        except:
            pass
        self.add_function()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_Button.setText(_translate("MainWindow", "+"))
        self.Msg_Lable.setText(_translate("MainWindow", "Message:"))
        self.Notes_Label.setText(_translate("MainWindow", "Notes:"))
        self.Time_Lable.setText(_translate("MainWindow", "Time:"))
        self.Time_Table.setText(_translate("MainWindow", "Time"))
        self.Notes_Table.setText(_translate("MainWindow", "   Notes"))
        self.Msg_Table.setText(_translate("MainWindow", "Message"))
        self.Time_1.setText(_translate("MainWindow", "XX:XX"))
        self.Time_2.setText(_translate("MainWindow", "XX:XX"))
        self.Time_3.setText(_translate("MainWindow", "XX:XX"))
        self.del_Button1.setText(_translate("MainWindow", "×"))
        self.del_Button2.setText(_translate("MainWindow", "×"))
        self.del_Button3.setText(_translate("MainWindow", "×"))



    def add_function(self):
        self.add_Button.clicked.connect(lambda: self.add_note(self.note_count))
        self.del_Button1.clicked.connect(lambda: self.delete(0))
        self.del_Button2.clicked.connect(lambda: self.delete(1))
        self.del_Button3.clicked.connect(lambda: self.delete(2))

    def add_note(self, note_count):
        try:
            time = self.Time_Input.toPlainText().strip()
            note = self.Notes_Input_2.toPlainText().strip()
            msg = self.Msg_Input.toPlainText().strip()
            NoteMachine_Class.tasks[self.note_count] = NoteMachine_Class.Note(time, note, msg)
            if time and note and msg:
                if self.Time_1.text() == "XX:XX":
                    self.Time_1.setText(time)
                    self.Notes_1.setText(note)
                    self.Msg_1.setText(msg)
                elif self.Time_2.text() == "XX:XX":
                    self.Time_2.setText(time)
                    self.Notes_2.setText(note)
                    self.Msg_2.setText(msg)
                elif self.Time_3.text() == "XX:XX":
                    self.Time_3.setText(time)
                    self.Notes_3.setText(note)
                    self.Msg_3.setText(msg)
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Error")
                    error.setText("Very more tasks, delete some one")
                    error.exec_()
                self.note_count += 1
                self.Time_Input.clear()
                self.Notes_Input_2.clear()
                self.Msg_Input.clear()
            else:
                error = QMessageBox()
                error.setWindowTitle("Error")
                error.setText("Isn't enougth data")
                error.exec_()

        except NoteMachine_Class.ScheduleValueError:
            self.Time_Input.clear()
            self.Notes_Input_2.clear()
            self.Msg_Input.clear()
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Unconrect time")
            error.exec_()

    def delete(self, note_number):
        if  note_number in NoteMachine_Class.tasks:
            task_obj = NoteMachine_Class.tasks[note_number]
            task_obj.task_cancel()
            del NoteMachine_Class.tasks[note_number]
            match note_number:
                case 0:
                    self.Time_1.setText("XX:XX")
                    self.Notes_1.setText("")
                    self.Msg_1.setText("")
                    self.note_count = 0
                case 1:
                    self.Time_2.setText("XX:XX")
                    self.Notes_2.setText("")
                    self.Msg_2.setText("")
                    self.note_count = 1
                case 2:
                    self.Time_3.setText("XX:XX")
                    self.Notes_3.setText("")
                    self.Msg_3.setText("")
                    self.note_count = 2
                case _:
                    print("Неверный номер заметки")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = AppWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
