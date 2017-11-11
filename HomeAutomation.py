# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAutomation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 971, 551))

        self.tabWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(5,24, 77, 0), stop:1 rgba(5, 24, 77, 0.28));\n""")

        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gh = QtWidgets.QGroupBox(self.tab)
        self.gh.setGeometry(QtCore.QRect(60, 40, 381, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gh.setFont(font)
        self.gh.setFlat(False)
        self.gh.setCheckable(False)
        self.gh.setObjectName("gh")


        self.Level1_Pushbutton1 = "OFF"
        self.pushButton = QtWidgets.QPushButton(self.gh)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton.setObjectName("LIGHT ON")
        self.pushButton.clicked.connect(self.click_level1_pushbutton1)
        self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: gray;}')

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%%%%%%%%%%%% QDial    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        self.dial = QtWidgets.QDial(self.gh)
        self.dial.setGeometry(QtCore.QRect(210, 60, 111, 101))
        self.dial.setMinimum(20)
        self.dial.setMaximum(30)
        self.dial.setProperty("value", 25)
        self.dial.setInvertedAppearance(False)
        self.dial.setObjectName("dial")
        self.dial.setNotchesVisible(True)
        self.dial.setWrapping(True)
        self.dial.setStyleSheet('QDial {background-color: #717c7b; color: red;}')


        self.spinBox = QtWidgets.QSpinBox(self.gh)
        self.spinBox.setGeometry(QtCore.QRect(250, 160, 41, 21))
        self.spinBox.setMinimum(21)
        self.spinBox.setMaximum(29)
        self.spinBox.setValue(25)
        self.spinBox.setObjectName("spinBox")

        self.dial.valueChanged.connect(self.change_dial)
        self.spinBox.valueChanged.connect(self.change_spinbox)
        #self.dial.valueChanged.connect(self.spinBox.setValue)
        #self.spinBox.valueChanged.connect(self.dial.setValue)


        self.label = QtWidgets.QLabel(self.gh)
        self.label.setGeometry(QtCore.QRect(210, 20, 131, 16))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 260, 381, 201))
        self.groupBox_2.setObjectName("groupBox_2")

        self.Level1_Pushbutton2 = "OFF"
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.click_level1_pushbutton2)
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: gray;}')



        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 40, 381, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(490, 260, 381, 201))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gh_2 = QtWidgets.QGroupBox(self.tab_2)
        self.gh_2.setGeometry(QtCore.QRect(20, 30, 381, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gh_2.setFont(font)
        self.gh_2.setFlat(False)
        self.gh_2.setCheckable(False)
        self.gh_2.setObjectName("gh_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.gh_2)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.dial_2 = QtWidgets.QDial(self.gh_2)
        self.dial_2.setGeometry(QtCore.QRect(240, 30, 50, 64))
        self.dial_2.setMinimum(20)
        self.dial_2.setMaximum(30)
        self.dial_2.setProperty("value", 25)
        self.dial_2.setInvertedAppearance(False)
        self.dial_2.setObjectName("dial_2")
        self.label_2 = QtWidgets.QLabel(self.gh_2)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 131, 16))
        self.label_2.setObjectName("label_2")
        self.gh_3 = QtWidgets.QGroupBox(self.tab_2)
        self.gh_3.setGeometry(QtCore.QRect(20, 290, 381, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gh_3.setFont(font)
        self.gh_3.setFlat(False)
        self.gh_3.setCheckable(False)
        self.gh_3.setObjectName("gh_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.gh_3)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gh_4 = QtWidgets.QGroupBox(self.tab_2)
        self.gh_4.setGeometry(QtCore.QRect(500, 30, 381, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gh_4.setFont(font)
        self.gh_4.setFlat(False)
        self.gh_4.setCheckable(False)
        self.gh_4.setObjectName("gh_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.gh_4)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gh_5 = QtWidgets.QGroupBox(self.tab_2)
        self.gh_5.setGeometry(QtCore.QRect(500, 290, 381, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gh_5.setFont(font)
        self.gh_5.setFlat(False)
        self.gh_5.setCheckable(False)
        self.gh_5.setObjectName("gh_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.gh_5)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gh_6 = QtWidgets.QGroupBox(self.tab_3)
        self.gh_6.setGeometry(QtCore.QRect(260, 120, 381, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gh_6.setFont(font)
        self.gh_6.setFlat(False)
        self.gh_6.setCheckable(False)
        self.gh_6.setObjectName("gh_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.gh_6)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.dial_3 = QtWidgets.QDial(self.gh_6)
        self.dial_3.setGeometry(QtCore.QRect(240, 30, 50, 64))
        self.dial_3.setMinimum(20)
        self.dial_3.setMaximum(30)
        self.dial_3.setProperty("value", 25)
        self.dial_3.setInvertedAppearance(False)
        self.dial_3.setObjectName("dial_3")
        self.label_3 = QtWidgets.QLabel(self.gh_6)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 131, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click_level1_pushbutton1(self):

        print(self.Level1_Pushbutton1)
        if (self.Level1_Pushbutton1 == "ON"):
            self.Level1_Pushbutton1 = "OFF"
            self.pushButton.setText("O F F")
            self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: gray;}')


            
        else:
            self.Level1_Pushbutton1 = "ON"
            self.pushButton.setText("O N")
            self.pushButton.setStyleSheet('QPushButton {background-color: #457d2f; color: black;}')

    def click_level1_pushbutton2(self):

        print(self.Level1_Pushbutton2)
        if (self.Level1_Pushbutton2 == "ON"):
            self.Level1_Pushbutton2 = "OFF"
            self.pushButton_2.setText("O F F")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: gray;}')


        else:
            self.Level1_Pushbutton2 = "ON"
            self.pushButton_2.setText("O N")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: #457d2f; color: black;}')

    def change_dial(self):

            self.spinBox.setValue(self.dial.value())

    def change_spinbox(self):

            self.dial.setValue(self.spinBox.value())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HOME AUTOMATION SYSTEM"))


        #self.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: gray;}')

        self.gh.setTitle(_translate("MainWindow", "Living Room"))

        self.pushButton.setText(_translate("MainWindow", "O F F"))

        self.label.setText(_translate("MainWindow", "Temperature Control"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kitchen"))
        self.pushButton_2.setText(_translate("MainWindow", "O F F"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Garden"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.groupBox.setTitle(_translate("MainWindow", "Dining Room"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "GROUND FLOOR"))
        self.gh_2.setTitle(_translate("MainWindow", "MASTER BEDROOM"))
        self.pushButton_4.setText(_translate("MainWindow", "Light1 ON"))
        self.label_2.setText(_translate("MainWindow", "Temperature Control"))
        self.gh_3.setTitle(_translate("MainWindow", "BEDROOM 1"))
        self.pushButton_5.setText(_translate("MainWindow", "Light1 ON"))
        self.gh_4.setTitle(_translate("MainWindow", "HOME WORKSTATION"))
        self.pushButton_6.setText(_translate("MainWindow", "Light1 ON"))
        self.gh_5.setTitle(_translate("MainWindow", "TOILET"))
        self.pushButton_7.setText(_translate("MainWindow", "Light1 ON"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SECOND FLOOR"))
        self.gh_6.setTitle(_translate("MainWindow", "BEDROOM 2"))
        self.pushButton_8.setText(_translate("MainWindow", "Light1 ON"))
        self.label_3.setText(_translate("MainWindow", "Temperature Control"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ATTIC"))

if __name__ == "__main__":
    import sys

    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
