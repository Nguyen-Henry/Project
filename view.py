# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rock_button = QtWidgets.QPushButton(self.centralwidget)
        self.rock_button.setGeometry(QtCore.QRect(940, 490, 151, 81))
        self.rock_button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.rock_button.setObjectName("rock_button")
        self.paper_button = QtWidgets.QPushButton(self.centralwidget)
        self.paper_button.setGeometry(QtCore.QRect(510, 490, 151, 81))
        self.paper_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.paper_button.setObjectName("paper_button")
        self.scissors_button = QtWidgets.QPushButton(self.centralwidget)
        self.scissors_button.setGeometry(QtCore.QRect(50, 490, 151, 81))
        self.scissors_button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.scissors_button.setObjectName("scissors_button")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(450, 20, 418, 31))
        self.title.setMinimumSize(QtCore.QSize(418, 31))
        self.title.setMaximumSize(QtCore.QSize(418, 31))
        self.title.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.title.setObjectName("title")
        self.basic_text = QtWidgets.QLabel(self.centralwidget)
        self.basic_text.setGeometry(QtCore.QRect(450, 220, 271, 51))
        self.basic_text.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.basic_text.setObjectName("basic_text")
        self.player_wins = QtWidgets.QLabel(self.centralwidget)
        self.player_wins.setGeometry(QtCore.QRect(10, 400, 201, 41))
        self.player_wins.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.player_wins.setObjectName("player_wins")
        self.computer_wins = QtWidgets.QLabel(self.centralwidget)
        self.computer_wins.setGeometry(QtCore.QRect(810, 400, 231, 41))
        self.computer_wins.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.computer_wins.setObjectName("computer_wins")
        self.player_choice = QtWidgets.QLabel(self.centralwidget)
        self.player_choice.setGeometry(QtCore.QRect(10, 440, 271, 51))
        self.player_choice.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 127);")
        self.player_choice.setObjectName("player_choice")
        self.computer_choice = QtWidgets.QLabel(self.centralwidget)
        self.computer_choice.setGeometry(QtCore.QRect(810, 440, 331, 51))
        self.computer_choice.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.computer_choice.setObjectName("computer_choice")
        self.outcome = QtWidgets.QLabel(self.centralwidget)
        self.outcome.setGeometry(QtCore.QRect(460, 450, 341, 41))
        self.outcome.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 255);")
        self.outcome.setObjectName("outcome")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(950, 20, 151, 81))
        self.reset_button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.reset_button.setObjectName("reset_button")
        self.player_picture = QtWidgets.QLabel(self.centralwidget)
        self.player_picture.setGeometry(QtCore.QRect(50, 160, 261, 181))
        self.player_picture.setText("")
        self.player_picture.setPixmap(QtGui.QPixmap("RPS.png"))
        self.player_picture.setScaledContents(True)
        self.player_picture.setObjectName("player_picture")
        self.computer_picture = QtWidgets.QLabel(self.centralwidget)
        self.computer_picture.setGeometry(QtCore.QRect(830, 160, 261, 181))
        self.computer_picture.setText("")
        self.computer_picture.setPixmap(QtGui.QPixmap("RPS.png"))
        self.computer_picture.setScaledContents(True)
        self.computer_picture.setObjectName("computer_picture")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors "))
        self.rock_button.setText(_translate("MainWindow", "Rock"))
        self.paper_button.setText(_translate("MainWindow", "Paper"))
        self.scissors_button.setText(_translate("MainWindow", "Scissors"))
        self.title.setText(_translate("MainWindow", "Rock Paper Scissors"))
        self.basic_text.setText(_translate("MainWindow", "Please select an option"))
        self.player_wins.setText(_translate("MainWindow", "Player Wins:"))
        self.computer_wins.setText(_translate("MainWindow", "Computer Wins:"))
        self.player_choice.setText(_translate("MainWindow", "Player Choice: "))
        self.computer_choice.setText(_translate("MainWindow", "Computer Choice:"))
        self.outcome.setText(_translate("MainWindow", "Outcome:"))
        self.reset_button.setText(_translate("MainWindow", "RESET"))
