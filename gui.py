# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
from random import randint
from random import sample
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

import time
import requests

from PyQt5.QtWidgets import QMessageBox

class MainWindow(object):
    def setupUi(self, MainWindow):
        self.jsonForApp = ''
        self.requestFromServer = requests.get('http://localhost:5000/')

        self.thread = threading.Thread(target=self.updateSpinBox, args=())
        self.thread.daemon = True
        self.thread.start()

        MainWindow.setObjectName("Quiz")
        MainWindow.resize(411, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonDodaj = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonDodaj.setObjectName("buttonDodaj")
        self.gridLayout_4.addWidget(self.buttonDodaj, 9, 2, 1, 1)
        self.odpowiedzC = QtWidgets.QLineEdit(self.groupBox_2)
        self.odpowiedzC.setObjectName("odpowiedzC")
        self.gridLayout_4.addWidget(self.odpowiedzC, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 7, 0, 1, 1)
        self.odpowiedzB = QtWidgets.QLineEdit(self.groupBox_2)
        self.odpowiedzB.setObjectName("odpowiedzB")
        self.gridLayout_4.addWidget(self.odpowiedzB, 3, 2, 1, 1)
        self.odpowiedzA = QtWidgets.QLineEdit(self.groupBox_2)
        self.odpowiedzA.setObjectName("odpowiedzA")
        self.gridLayout_4.addWidget(self.odpowiedzA, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.pytanie = QtWidgets.QLineEdit(self.groupBox_2)
        self.pytanie.setObjectName("pytanie")
        self.gridLayout_4.addWidget(self.pytanie, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)
        self.odpowiedzD = QtWidgets.QLineEdit(self.groupBox_2)
        self.odpowiedzD.setObjectName("odpowiedzD")
        self.gridLayout_4.addWidget(self.odpowiedzD, 7, 2, 1, 1)
        self.radioButtonA = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonA.setText("")
        self.radioButtonA.setObjectName("radioButtonA")
        self.gridLayout_4.addWidget(self.radioButtonA, 1, 1, 1, 1)
        self.radioButtonB = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonB.setText("")
        self.radioButtonB.setObjectName("radioButtonB")
        self.gridLayout_4.addWidget(self.radioButtonB, 3, 1, 1, 1)
        self.radioButtonC = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonC.setText("")
        self.radioButtonC.setObjectName("radioButtonC")
        self.gridLayout_4.addWidget(self.radioButtonC, 5, 1, 1, 1)
        self.radioButtonD = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonD.setText("")
        self.radioButtonD.setObjectName("radioButtonD")
        self.gridLayout_4.addWidget(self.radioButtonD, 7, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMinimum(1)

        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.buttonStart = QtWidgets.QPushButton(self.groupBox)
        self.buttonStart.setObjectName("buttonStart")
        self.gridLayout_3.addWidget(self.buttonStart, 4, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.buttonStart)
        MainWindow.setTabOrder(self.buttonStart, self.pytanie)
        MainWindow.setTabOrder(self.pytanie, self.odpowiedzA)
        MainWindow.setTabOrder(self.odpowiedzA, self.odpowiedzB)
        MainWindow.setTabOrder(self.odpowiedzB, self.odpowiedzC)
        MainWindow.setTabOrder(self.odpowiedzC, self.odpowiedzD)
        MainWindow.setTabOrder(self.odpowiedzD, self.radioButtonA)
        MainWindow.setTabOrder(self.radioButtonA, self.radioButtonB)
        MainWindow.setTabOrder(self.radioButtonB, self.radioButtonC)
        MainWindow.setTabOrder(self.radioButtonC, self.radioButtonD)
        MainWindow.setTabOrder(self.radioButtonD, self.buttonDodaj)

        self.buttonDodaj.clicked.connect(self.quizDodaj)
        self.buttonStart.clicked.connect(self.quizStart)

    def updateSpinBox(self):
        while True:
            self.jsonForApp = requests.get('http://localhost:5000').json()
            self.spinBox.setMaximum(len(self.jsonForApp))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dodawanie"))
        self.buttonDodaj.setText(_translate("MainWindow", "Dodaj"))
        self.label_4.setText(_translate("MainWindow", "B"))
        self.label_6.setText(_translate("MainWindow", "D"))
        self.label_2.setText(_translate("MainWindow", "Pytanie"))
        self.label_3.setText(_translate("MainWindow", "A"))
        self.label_5.setText(_translate("MainWindow", "C"))
        self.groupBox.setTitle(_translate("MainWindow", "Quiz"))
        self.label.setText(_translate("MainWindow", "Ilość pytań"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))

    def quizDodaj(self):
        self.server_ip = 'http://localhost:5000/add'

        if self.odpowiedzA.text():
            if self.odpowiedzB.text():
                if self.odpowiedzC.text():
                    if self.odpowiedzD.text():
                        if self.pytanie.text():
                            if self.radioButtonA.isChecked():
                                self.event_data = {'a': self.odpowiedzA.text(), 'b': self.odpowiedzB.text(),
                                                   'c': self.odpowiedzC.text(), 'd': self.odpowiedzD.text(),
                                                   'poprawna': self.odpowiedzA.text(), 'pytanie': self.pytanie.text()}
                                requests.post(self.server_ip, json=self.event_data)
                            elif self.radioButtonB.isChecked():
                                self.event_data = {'a': self.odpowiedzA.text(), 'b': self.odpowiedzB.text(),
                                                   'c': self.odpowiedzC.text(), 'd': self.odpowiedzD.text(),
                                                   'poprawna': self.odpowiedzB.text(), 'pytanie': self.pytanie.text()}
                                requests.post(self.server_ip, json=self.event_data)
                            elif self.radioButtonC.isChecked():
                                self.event_data = {'a': self.odpowiedzA.text(), 'b': self.odpowiedzB.text(),
                                                   'c': self.odpowiedzC.text(), 'd': self.odpowiedzD.text(),
                                                   'poprawna': self.odpowiedzC.text(), 'pytanie': self.pytanie.text()}
                                requests.post(self.server_ip, json=self.event_data)
                            elif self.radioButtonD.isChecked():
                                self.event_data = {'a': self.odpowiedzA.text(), 'b': self.odpowiedzB.text(),
                                                   'c': self.odpowiedzC.text(), 'd': self.odpowiedzD.text(),
                                                   'poprawna': self.odpowiedzD.text(), 'pytanie': self.pytanie.text()}
                                requests.post(self.server_ip, json=self.event_data)

    def quizStart(self):
        self.howManyQuestions = int(self.spinBox.text())

        self.dialog = QtWidgets.QMainWindow()
        self.ui = QuizWid()
        self.ui.setupUi(self.dialog, self.howManyQuestions, self.jsonForApp)
        self.dialog.show()




class QuizWid(object):
    def getRandomArray(self, howManyQuestions, howManyQuestionsYouWant):
        self.resultFromRandom = set()
        while len(self.resultFromRandom) < howManyQuestionsYouWant:
            self.resultFromRandom.add(randint(1, howManyQuestions))
        self.tab = [i for i in self.resultFromRandom]

        return sample(self.tab, len(self.tab))

    def setupUi(self, MainWindow, howManyQuestions, jsonFromRequest):
        self.jsonFromRequest = jsonFromRequest
        self.idQuestions = self.getRandomArray(len(jsonFromRequest), howManyQuestions)
        print(self.idQuestions)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dalejButton = QtWidgets.QPushButton(self.frame)
        self.dalejButton.setObjectName("dalejButton")
        self.gridLayout_2.addWidget(self.dalejButton, 9, 0, 1, 1)
        self.radioButtonB = QtWidgets.QRadioButton(self.frame)
        self.radioButtonB.setObjectName("radioButtonB")
        self.gridLayout_2.addWidget(self.radioButtonB, 6, 0, 1, 1)
        self.radioButtonA = QtWidgets.QRadioButton(self.frame)
        self.radioButtonA.setObjectName("radioButtonA")
        self.gridLayout_2.addWidget(self.radioButtonA, 3, 0, 1, 1)
        self.radioButtonC = QtWidgets.QRadioButton(self.frame)
        self.radioButtonC.setObjectName("radioButtonC")
        self.gridLayout_2.addWidget(self.radioButtonC, 7, 0, 1, 1)
        self.radioButtonD = QtWidgets.QRadioButton(self.frame)
        self.radioButtonD.setObjectName("radioButtonD")
        self.gridLayout_2.addWidget(self.radioButtonD, 8, 0, 1, 1)
        self.labelPytanie = QtWidgets.QLabel(self.frame)
        self.labelPytanie.setObjectName("labelPytanie")
        self.gridLayout_2.addWidget(self.labelPytanie, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.labelTytul = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTytul.setFont(font)
        self.labelTytul.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTytul.setObjectName("labelTytul")
        self.gridLayout_2.addWidget(self.labelTytul, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dalejButton.clicked.connect(self.quiz)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.translate(self.idQuestions[0], jsonFromRequest)
        self.correct = 0

    def quiz(self):
        if self.idQuestions:
            if self.radioButtonA.isChecked():
                if self.checkCorrectAnswer('a', self.idQuestions[0]):
                    self.correct += 1
            elif self.radioButtonB.isChecked():
                if self.checkCorrectAnswer('b', self.idQuestions[0]):
                    self.correct += 1
            elif self.radioButtonC.isChecked():
                if self.checkCorrectAnswer('c', self.idQuestions[0]):
                    self.correct += 1
            elif self.radioButtonD.isChecked():
                if self.checkCorrectAnswer('d', self.idQuestions[0]):
                    self.correct += 1
            self.idQuestions.pop(0)
            if self.idQuestions:
                self.translate(self.idQuestions[0], self.jsonFromRequest)
            else:
                print(self.correct)
                #info = QMessageBox(self, 'Wynik:', str(self.correct))
                #info.exec_()


    def checkCorrectAnswer(self, answer, id):
        a = self.jsonFromRequest[id-1][answer]
        b = self.jsonFromRequest[id-1]['poprawna']
        if a in b:
            return True

        else:
            return False



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "quuuuiz"))
        self.dalejButton.setText(_translate("MainWindow", "Dalej"))
        self.labelTytul.setText(_translate("MainWindow", "QUIZOWANIE"))

    def translate(self, number, json):
        self.radioButtonA.setText(json[number-1]['a'])
        self.radioButtonB.setText(json[number-1]['b'])
        self.radioButtonC.setText(json[number-1]['c'])
        self.radioButtonD.setText(json[number-1]['d'])
        self.labelPytanie.setText(json[number-1]['pytanie'])

