# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAutomation5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setWindowOpacity(5.0)

        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setEnabled(True)
        self.frame_main.setGeometry(QtCore.QRect(0, -10, 1031, 611))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame_main.setFont(font)
        self.frame_main.setAutoFillBackground(False)
        self.frame_main.setStyleSheet("QFrame {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QStackedWidget\n"
"{\n"
"background-color: rgb(249, 249, 249);\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 130, 781, 351))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.attic = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.attic.setGeometry(QtCore.QRect(380, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.attic.setFont(font)
        self.attic.setStyleSheet("color: rgb(29, 176, 29);\n"
"background-color: rgb(104, 104, 104);\n"
"font: 75 15pt \"Agency FB\";\n"
"border-color: rgb(217, 217, 217);")
        self.attic.setAutoDefault(False)
        self.attic.setDefault(False)
        self.attic.setObjectName("attic")
        self.second_floor = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.second_floor.setGeometry(QtCore.QRect(210, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.second_floor.setFont(font)
        self.second_floor.setStyleSheet("color: rgb(29, 176, 29);\n"
"background-color: rgb(104, 104, 104);\n"
"font: 75 15pt \"Agency FB\";\n"
"border-color: rgb(217, 217, 217);")
        self.second_floor.setAutoDefault(False)
        self.second_floor.setDefault(False)
        self.second_floor.setObjectName("second_floor")
        self.ground_floor = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.ground_floor.setGeometry(QtCore.QRect(20, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ground_floor.setFont(font)
        self.ground_floor.setStyleSheet("background-color: rgb(104, 104, 104);\n"
"font: 75 15pt \"Agency FB\";\n"
"color: rgb(29, 176, 29);\n"
"border-color: rgb(217, 217, 217);")
        self.ground_floor.setAutoDefault(False)
        self.ground_floor.setDefault(False)
        self.ground_floor.setObjectName("ground_floor")
        self.pushButton_L1_1 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_L1_1.setGeometry(QtCore.QRect(80, 180, 61, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_L1_1.sizePolicy().hasHeightForWidth())
        self.pushButton_L1_1.setSizePolicy(sizePolicy)
        self.pushButton_L1_1.setStyleSheet("")
        self.pushButton_L1_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_new/lightOff.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_L1_1.setIcon(icon)
        self.pushButton_L1_1.setIconSize(QtCore.QSize(250, 80))
        self.pushButton_L1_1.setFlat(False)
        self.pushButton_L1_1.setObjectName("pushButton_L1_1")
        self.toolButton = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.toolButton.setGeometry(QtCore.QRect(180, 200, 41, 71))
        self.toolButton.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images_new/lightOff.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label.setGeometry(QtCore.QRect(100, 280, 31, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.afloor_all = QtWidgets.QCheckBox(self.stackedWidgetPage1)
        self.afloor_all.setGeometry(QtCore.QRect(20, 80, 181, 16))
        self.afloor_all.setObjectName("afloor_all")
        self.sfloor_all = QtWidgets.QCheckBox(self.stackedWidgetPage1)
        self.sfloor_all.setGeometry(QtCore.QRect(210, 70, 181, 31))
        self.sfloor_all.setObjectName("sfloor_all")
        self.gfloor_all = QtWidgets.QCheckBox(self.stackedWidgetPage1)
        self.gfloor_all.setGeometry(QtCore.QRect(390, 70, 181, 31))
        self.gfloor_all.setObjectName("gfloor_all")
        self.ground_floor_2 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.ground_floor_2.setGeometry(QtCore.QRect(570, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ground_floor_2.setFont(font)
        self.ground_floor_2.setStyleSheet("background-color: rgb(104, 104, 104);\n"
"font: 75 15pt \"Agency FB\";\n"
"color: rgb(29, 176, 29);\n"
"border-color: rgb(217, 217, 217);")
        self.ground_floor_2.setAutoDefault(False)
        self.ground_floor_2.setDefault(False)
        self.ground_floor_2.setObjectName("ground_floor_2")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.pushButton_L2_1 = QtWidgets.QPushButton(self.stackedWidgetPage2)
        self.pushButton_L2_1.setGeometry(QtCore.QRect(40, 20, 61, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_L2_1.sizePolicy().hasHeightForWidth())
        self.pushButton_L2_1.setSizePolicy(sizePolicy)
        self.pushButton_L2_1.setStyleSheet("")
        self.pushButton_L2_1.setText("")
        self.pushButton_L2_1.setIcon(icon)
        self.pushButton_L2_1.setIconSize(QtCore.QSize(250, 80))
        self.pushButton_L2_1.setFlat(False)
        self.pushButton_L2_1.setObjectName("pushButton_L2_1")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QtWidgets.QWidget()
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.stackedWidget.addWidget(self.stackedWidgetPage3)
        self.frame_2 = QtWidgets.QFrame(self.frame_main)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 771, 111))
        self.frame_2.setStyleSheet("QFrame {\n"
"background-color: rgb(249, 249, 249);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 801, 111))
        self.frame.setStyleSheet("QFrame \n"
"{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(120, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("QToolButton\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: transparent;\n"
"border: none;\n"
"\n"
"}\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images_new/home2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setAutoRaise(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(230, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images_new/groundfloor.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setAutoRaise(False)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        self.toolButton_5.setGeometry(QtCore.QRect(340, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images_new/settings.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setAutoRaise(False)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.frame)
        self.toolButton_6.setGeometry(QtCore.QRect(390, 110, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        self.toolButton_6.setIcon(icon4)
        self.toolButton_6.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setAutoRaise(False)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.frame)
        self.toolButton_7.setGeometry(QtCore.QRect(440, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images_new/tips.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon5)
        self.toolButton_7.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_7.setAutoRaise(False)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_8 = QtWidgets.QToolButton(self.frame)
        self.toolButton_8.setGeometry(QtCore.QRect(570, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_8.sizePolicy().hasHeightForWidth())
        self.toolButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_8.setFont(font)
        self.toolButton_8.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images_new/stocks.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon6)
        self.toolButton_8.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_8.setAutoRaise(False)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.frame)
        self.toolButton_9.setGeometry(QtCore.QRect(10, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_9.sizePolicy().hasHeightForWidth())
        self.toolButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_9.setFont(font)
        self.toolButton_9.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images_new/lock.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon7)
        self.toolButton_9.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_9.setAutoRaise(False)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(680, 10, 81, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"font: 75 12pt \"Agency FB\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    background-color:transparent;\n"
"border:none;\n"
"\n"
"}\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177)\n"
"}\n"
"QToolButton:hover {\n"
"background-color(224,232,246)\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images_new/weather.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon8)
        self.toolButton_3.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setAutoRaise(False)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_2.raise_()
        self.toolButton_4.raise_()
        self.toolButton_5.raise_()
        self.toolButton_6.raise_()
        self.stackedWidget.raise_()
        self.toolButton_7.raise_()
        self.toolButton_8.raise_()
        self.toolButton_9.raise_()
        self.toolButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HOME AUTOMATION Powered by RASPBERRY PI (Python) + FPGA (VHDL)"))
        self.attic.setText(_translate("MainWindow", "ATTIC"))
        self.second_floor.setText(_translate("MainWindow", "SECOND FLOOR"))
        self.ground_floor.setText(_translate("MainWindow", "GROUND FLOOR"))
        self.toolButton.setText(_translate("MainWindow", "light"))
        self.label.setText(_translate("MainWindow", "Light 1"))
        self.afloor_all.setText(_translate("MainWindow", "ATTIC ALL LIGHTS"))
        self.sfloor_all.setText(_translate("MainWindow", "SECOND FLOOR ALL LIGHTS"))
        self.gfloor_all.setText(_translate("MainWindow", "GROUND FLOOR ALL LIGHTS"))
        self.ground_floor_2.setText(_translate("MainWindow", "GARAGE + GARDEN"))
        self.toolButton_2.setText(_translate("MainWindow", "HOME"))
        self.toolButton_4.setText(_translate("MainWindow", "CONTROLS"))
        self.toolButton_5.setText(_translate("MainWindow", "SETTINGS"))
        self.toolButton_6.setText(_translate("MainWindow", "SETTINGS"))
        self.toolButton_7.setText(_translate("MainWindow", "TIPS"))
        self.toolButton_8.setText(_translate("MainWindow", "STOCKS"))
        self.toolButton_9.setText(_translate("MainWindow", "LOGIN"))
        self.toolButton_3.setText(_translate("MainWindow", "WEATHER"))

#import try_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

