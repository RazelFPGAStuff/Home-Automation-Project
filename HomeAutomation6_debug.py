# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAutomation5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import RPi.GPIO as GPIO
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 450)
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
        self.stackedWidget.setGeometry(QtCore.QRect(0, 120, 781, 351))
        self.stackedWidget.setStyleSheet("QStackedWidget\n"
                                         "\n"
                                         "{\n"
                                         "\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "\n"
                                         "}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.stackedWidget1 = QtWidgets.QStackedWidget(self.stackedWidgetPage1)
        self.stackedWidget1.setGeometry(QtCore.QRect(10, 120, 781, 231))
        self.stackedWidget1.setStyleSheet("QFrame\n"
                                          "{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "}")
        self.stackedWidget1.setObjectName("stackedWidget1")
        self.stackedWidgetPage1_2 = QtWidgets.QWidget()
        self.stackedWidgetPage1_2.setObjectName("stackedWidgetPage1_2")
        self.groupBox = QtWidgets.QGroupBox(self.stackedWidgetPage1_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 301, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolButton_21 = QtWidgets.QToolButton(self.verticalLayoutWidget_5)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_21.setFont(font)
        self.toolButton_21.setStyleSheet("QToolButton\n"



                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_21.setIcon(icon)
        self.toolButton_21.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_21.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_21.setObjectName("toolButton_21")
        self.verticalLayout_5.addWidget(self.toolButton_21)

        # --------------added by ry
        self.value_toolButton_21 = "ON"
        #set_RPi()
        self.click_toolbutton_21()
        self.toolButton_21.clicked.connect(self.click_toolbutton_21)
        ### ---end

        self.toolButton_22 = QtWidgets.QToolButton(self.verticalLayoutWidget_5)
        self.toolButton_22.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 60 7pt \"Agency FB\";\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_22.setIcon(icon1)
        self.toolButton_22.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_22.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_22.setObjectName("toolButton_22")
        self.verticalLayout_5.addWidget(self.toolButton_22)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(110, 20, 81, 202))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # --------------added by ry
        self.value_toolButton_22 = "ON"
        self.click_toolbutton_22()
        self.toolButton_22.clicked.connect(self.click_toolbutton_22)
        ### ---end


        self.toolButton_23 = QtWidgets.QToolButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_23.setFont(font)
        self.toolButton_23.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_23.setIcon(icon)
        self.toolButton_23.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_23.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_23.setObjectName("toolButton_23")
        self.verticalLayout_6.addWidget(self.toolButton_23)

        # --------------added by ry
        self.value_toolButton_23 = "ON"
        self.click_toolbutton_23()
        self.toolButton_23.clicked.connect(self.click_toolbutton_23)
        ### ---end


        self.toolButton_24 = QtWidgets.QToolButton(self.verticalLayoutWidget_6)
        self.toolButton_24.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_24.setIcon(icon1)
        self.toolButton_24.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_24.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_24.setObjectName("toolButton_24")
        self.verticalLayout_6.addWidget(self.toolButton_24)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(210, 20, 81, 202))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # --------------added by ry
        self.value_toolButton_24 = "ON"
        self.click_toolbutton_24()
        self.toolButton_24.clicked.connect(self.click_toolbutton_24)
        ### ---end

        self.toolButton_25 = QtWidgets.QToolButton(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_25.setFont(font)
        self.toolButton_25.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_25.setIcon(icon)
        self.toolButton_25.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_25.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_25.setObjectName("toolButton_25")
        self.verticalLayout_7.addWidget(self.toolButton_25)

        # --------------added by ry
        self.value_toolButton_25 = "ON"
        self.click_toolbutton_25()
        self.toolButton_25.clicked.connect(self.click_toolbutton_25)
        ### ---end

        self.toolButton_26 = QtWidgets.QToolButton(self.verticalLayoutWidget_7)
        self.toolButton_26.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_26.setIcon(icon1)
        self.toolButton_26.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_26.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_26.setObjectName("toolButton_26")
        self.verticalLayout_7.addWidget(self.toolButton_26)

        # --------------added by ry
        self.value_toolButton_26 = "ON"
        self.click_toolbutton_26()
        self.toolButton_26.clicked.connect(self.click_toolbutton_26)
        ### ---end


        self.groupBox_2 = QtWidgets.QGroupBox(self.stackedWidgetPage1_2)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 0, 201, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.toolButton_33 = QtWidgets.QToolButton(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_33.setFont(font)
        self.toolButton_33.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_33.setIcon(icon1)
        self.toolButton_33.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_33.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_33.setObjectName("toolButton_33")
        self.verticalLayout_11.addWidget(self.toolButton_33)
        self.toolButton_34 = QtWidgets.QToolButton(self.verticalLayoutWidget_11)
        self.toolButton_34.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_34.setIcon(icon1)
        self.toolButton_34.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_34.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_34.setObjectName("toolButton_34")
        self.verticalLayout_11.addWidget(self.toolButton_34)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(110, 20, 81, 202))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.toolButton_35 = QtWidgets.QToolButton(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_35.setFont(font)
        self.toolButton_35.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_35.setIcon(icon1)
        self.toolButton_35.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_35.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_35.setObjectName("toolButton_35")
        self.verticalLayout_12.addWidget(self.toolButton_35)
        self.toolButton_36 = QtWidgets.QToolButton(self.verticalLayoutWidget_12)
        self.toolButton_36.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_36.setIcon(icon1)
        self.toolButton_36.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_36.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_36.setObjectName("toolButton_36")
        self.verticalLayout_12.addWidget(self.toolButton_36)
        self.groupBox_3 = QtWidgets.QGroupBox(self.stackedWidgetPage1_2)
        self.groupBox_3.setGeometry(QtCore.QRect(530, 0, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.toolButton_37 = QtWidgets.QToolButton(self.verticalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_37.setFont(font)
        self.toolButton_37.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_37.setIcon(icon1)
        self.toolButton_37.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_37.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_37.setObjectName("toolButton_37")
        self.verticalLayout_13.addWidget(self.toolButton_37)
        self.toolButton_38 = QtWidgets.QToolButton(self.verticalLayoutWidget_13)
        self.toolButton_38.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_38.setIcon(icon1)
        self.toolButton_38.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_38.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_38.setObjectName("toolButton_38")
        self.verticalLayout_13.addWidget(self.toolButton_38)
        self.groupBox_11 = QtWidgets.QGroupBox(self.stackedWidgetPage1_2)
        self.groupBox_11.setGeometry(QtCore.QRect(640, 0, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayoutWidget_23 = QtWidgets.QWidget(self.groupBox_11)
        self.verticalLayoutWidget_23.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_23.setObjectName("verticalLayoutWidget_23")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_23)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.toolButton_57 = QtWidgets.QToolButton(self.verticalLayoutWidget_23)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_57.setFont(font)
        self.toolButton_57.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_57.setIcon(icon1)
        self.toolButton_57.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_57.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_57.setObjectName("toolButton_57")
        self.verticalLayout_23.addWidget(self.toolButton_57)
        self.toolButton_58 = QtWidgets.QToolButton(self.verticalLayoutWidget_23)
        self.toolButton_58.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_58.setIcon(icon1)
        self.toolButton_58.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_58.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_58.setObjectName("toolButton_58")
        self.verticalLayout_23.addWidget(self.toolButton_58)
        self.stackedWidget1.addWidget(self.stackedWidgetPage1_2)
        self.stackedWidgetPage2_2 = QtWidgets.QWidget()
        self.stackedWidgetPage2_2.setObjectName("stackedWidgetPage2_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.stackedWidgetPage2_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 201, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.toolButton_41 = QtWidgets.QToolButton(self.verticalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_41.setFont(font)
        self.toolButton_41.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_41.setIcon(icon)
        self.toolButton_41.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_41.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_41.setObjectName("toolButton_41")
        self.verticalLayout_15.addWidget(self.toolButton_41)
        self.toolButton_42 = QtWidgets.QToolButton(self.verticalLayoutWidget_15)
        self.toolButton_42.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_42.setIcon(icon1)
        self.toolButton_42.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_42.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_42.setObjectName("toolButton_42")
        self.verticalLayout_15.addWidget(self.toolButton_42)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(110, 20, 81, 202))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.toolButton_43 = QtWidgets.QToolButton(self.verticalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_43.setFont(font)
        self.toolButton_43.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_43.setIcon(icon)
        self.toolButton_43.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_43.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_43.setObjectName("toolButton_43")
        self.verticalLayout_16.addWidget(self.toolButton_43)
        self.toolButton_44 = QtWidgets.QToolButton(self.verticalLayoutWidget_16)
        self.toolButton_44.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_44.setIcon(icon1)
        self.toolButton_44.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_44.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_44.setObjectName("toolButton_44")
        self.verticalLayout_16.addWidget(self.toolButton_44)
        self.groupBox_6 = QtWidgets.QGroupBox(self.stackedWidgetPage2_2)
        self.groupBox_6.setGeometry(QtCore.QRect(300, 0, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.toolButton_45 = QtWidgets.QToolButton(self.verticalLayoutWidget_17)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_45.setFont(font)
        self.toolButton_45.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_45.setIcon(icon)
        self.toolButton_45.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_45.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_45.setObjectName("toolButton_45")
        self.verticalLayout_17.addWidget(self.toolButton_45)
        self.toolButton_46 = QtWidgets.QToolButton(self.verticalLayoutWidget_17)
        self.toolButton_46.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_46.setIcon(icon1)
        self.toolButton_46.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_46.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_46.setObjectName("toolButton_46")
        self.verticalLayout_17.addWidget(self.toolButton_46)
        self.groupBox_7 = QtWidgets.QGroupBox(self.stackedWidgetPage2_2)
        self.groupBox_7.setGeometry(QtCore.QRect(490, 0, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(self.groupBox_7)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.toolButton_47 = QtWidgets.QToolButton(self.verticalLayoutWidget_18)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_47.setFont(font)
        self.toolButton_47.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_47.setIcon(icon)
        self.toolButton_47.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_47.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_47.setObjectName("toolButton_47")
        self.verticalLayout_18.addWidget(self.toolButton_47)
        self.toolButton_48 = QtWidgets.QToolButton(self.verticalLayoutWidget_18)
        self.toolButton_48.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_48.setIcon(icon1)
        self.toolButton_48.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_48.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_48.setObjectName("toolButton_48")
        self.verticalLayout_18.addWidget(self.toolButton_48)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_8.setGeometry(QtCore.QRect(100, 40, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayoutWidget_20 = QtWidgets.QWidget(self.groupBox_8)
        self.verticalLayoutWidget_20.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_20.setObjectName("verticalLayoutWidget_20")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.toolButton_51 = QtWidgets.QToolButton(self.verticalLayoutWidget_20)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_51.setFont(font)
        self.toolButton_51.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_51.setIcon(icon)
        self.toolButton_51.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_51.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_51.setObjectName("toolButton_51")
        self.verticalLayout_20.addWidget(self.toolButton_51)
        self.toolButton_52 = QtWidgets.QToolButton(self.verticalLayoutWidget_20)
        self.toolButton_52.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_52.setIcon(icon1)
        self.toolButton_52.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_52.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_52.setObjectName("toolButton_52")
        self.verticalLayout_20.addWidget(self.toolButton_52)
        self.groupBox_9 = QtWidgets.QGroupBox(self.stackedWidgetPage2_2)
        self.groupBox_9.setGeometry(QtCore.QRect(640, 0, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayoutWidget_21 = QtWidgets.QWidget(self.groupBox_9)
        self.verticalLayoutWidget_21.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_21.setObjectName("verticalLayoutWidget_21")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_21)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.toolButton_53 = QtWidgets.QToolButton(self.verticalLayoutWidget_21)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_53.setFont(font)
        self.toolButton_53.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_53.setIcon(icon)
        self.toolButton_53.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_53.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_53.setObjectName("toolButton_53")
        self.verticalLayout_21.addWidget(self.toolButton_53)
        self.toolButton_54 = QtWidgets.QToolButton(self.verticalLayoutWidget_21)
        self.toolButton_54.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_54.setIcon(icon1)
        self.toolButton_54.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_54.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_54.setObjectName("toolButton_54")
        self.verticalLayout_21.addWidget(self.toolButton_54)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_10.setGeometry(QtCore.QRect(100, 40, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayoutWidget_22 = QtWidgets.QWidget(self.groupBox_10)
        self.verticalLayoutWidget_22.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_22.setObjectName("verticalLayoutWidget_22")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_22)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.toolButton_55 = QtWidgets.QToolButton(self.verticalLayoutWidget_22)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_55.setFont(font)
        self.toolButton_55.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_55.setIcon(icon)
        self.toolButton_55.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_55.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_55.setObjectName("toolButton_55")
        self.verticalLayout_22.addWidget(self.toolButton_55)
        self.toolButton_56 = QtWidgets.QToolButton(self.verticalLayoutWidget_22)
        self.toolButton_56.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_56.setIcon(icon1)
        self.toolButton_56.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_56.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_56.setObjectName("toolButton_56")
        self.verticalLayout_22.addWidget(self.toolButton_56)
        self.stackedWidget1.addWidget(self.stackedWidgetPage2_2)
        self.stackedWidgetPage3_2 = QtWidgets.QWidget()
        self.stackedWidgetPage3_2.setObjectName("stackedWidgetPage3_2")
        self.groupBox_12 = QtWidgets.QGroupBox(self.stackedWidgetPage3_2)
        self.groupBox_12.setGeometry(QtCore.QRect(300, 0, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayoutWidget_24 = QtWidgets.QWidget(self.groupBox_12)
        self.verticalLayoutWidget_24.setGeometry(QtCore.QRect(10, 20, 81, 202))
        self.verticalLayoutWidget_24.setObjectName("verticalLayoutWidget_24")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_24)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.toolButton_59 = QtWidgets.QToolButton(self.verticalLayoutWidget_24)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        self.toolButton_59.setFont(font)
        self.toolButton_59.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 65 10pt \"Agency FB\";\n"
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
        self.toolButton_59.setIcon(icon)
        self.toolButton_59.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_59.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_59.setObjectName("toolButton_59")
        self.verticalLayout_24.addWidget(self.toolButton_59)
        self.toolButton_60 = QtWidgets.QToolButton(self.verticalLayoutWidget_24)
        self.toolButton_60.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        self.toolButton_60.setIcon(icon1)
        self.toolButton_60.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_60.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_60.setObjectName("toolButton_60")
        self.verticalLayout_24.addWidget(self.toolButton_60)
        self.stackedWidget1.addWidget(self.stackedWidgetPage3_2)
        self.stackedWidgetPage4 = QtWidgets.QWidget()
        self.stackedWidgetPage4.setObjectName("stackedWidgetPage4")
        self.stackedWidget1.addWidget(self.stackedWidgetPage4)
        self.toolButton = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.toolButton.setGeometry(QtCore.QRect(30, 10, 101, 91))
        self.toolButton.setStyleSheet("QToolButton\n"
                                      "\n"
                                      "{\n"
                                      "font: 75 7pt \"Agency FB\";\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images_new/level1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(80, 100))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_10 = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.toolButton_10.setGeometry(QtCore.QRect(220, 10, 101, 91))
        self.toolButton_10.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images_new/level2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon3)
        self.toolButton_10.setIconSize(QtCore.QSize(80, 100))
        self.toolButton_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.toolButton_11.setGeometry(QtCore.QRect(410, 10, 101, 91))
        self.toolButton_11.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 75 7pt \"Agency FB\";\n"
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
        icon4.addPixmap(QtGui.QPixmap("images_new/level3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon4)
        self.toolButton_11.setIconSize(QtCore.QSize(80, 100))
        self.toolButton_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.toolButton_12.setGeometry(QtCore.QRect(590, 10, 101, 91))
        self.toolButton_12.setStyleSheet("QToolButton\n"
                                         "\n"
                                         "{\n"
                                         "font: 60 7pt \"Agency FB\";\n"
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
        icon5.addPixmap(QtGui.QPixmap("images_new/garage.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon5)
        self.toolButton_12.setIconSize(QtCore.QSize(80, 100))
        self.toolButton_12.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_12.setObjectName("toolButton_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.stackedWidgetPage1)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 731, 101))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.raise_()
        self.stackedWidget.raise_()
        self.toolButton.raise_()
        self.toolButton_10.raise_()
        self.toolButton_11.raise_()
        self.toolButton_12.raise_()
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QtWidgets.QWidget()
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.label = QtWidgets.QLabel(self.stackedWidgetPage3)
        self.label.setGeometry(QtCore.QRect(60, 60, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.stackedWidgetPage3)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(181, 181, 181);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.stackedWidgetPage3)
        self.label_4.setGeometry(QtCore.QRect(500, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(181, 181, 181);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.stackedWidgetPage3)
        self.label_3.setGeometry(QtCore.QRect(560, 50, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox_13 = QtWidgets.QGroupBox(self.stackedWidgetPage3)
        self.groupBox_13.setGeometry(QtCore.QRect(20, 130, 391, 211))
        self.groupBox_13.setObjectName("groupBox_13")
        self.dial = QtWidgets.QDial(self.groupBox_13)
        self.dial.setGeometry(QtCore.QRect(10, 30, 271, 171))
        self.dial.setMinimum(15)
        self.dial.setMaximum(30)
        self.dial.setInvertedAppearance(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_13)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 120, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("intValue", 18)
        self.lcdNumber.setObjectName("lcdNumber")
        self.groupBox_14 = QtWidgets.QGroupBox(self.stackedWidgetPage3)
        self.groupBox_14.setGeometry(QtCore.QRect(460, 130, 311, 211))
        self.groupBox_14.setObjectName("groupBox_14")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_14)
        self.lcdNumber_2.setGeometry(QtCore.QRect(70, 90, 81, 101))
        self.lcdNumber_2.setStyleSheet("color: rgb(138, 138, 138);")
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("intValue", 12)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox_14)
        self.lcdNumber_3.setGeometry(QtCore.QRect(180, 90, 81, 101))
        self.lcdNumber_3.setStyleSheet("color: rgb(138, 138, 138);")
        self.lcdNumber_3.setDigitCount(2)
        self.lcdNumber_3.setProperty("intValue", 59)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_14)
        self.label_5.setGeometry(QtCore.QRect(160, 100, 21, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(138, 138, 138);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_14)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images_new/home2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon6)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images_new/groundfloor.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon7)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images_new/settings.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon8)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        self.toolButton_6.setIcon(icon8)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images_new/tips.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon9)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images_new/stocks.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon10)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images_new/lock.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon11)
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
                                        "font: 75 10pt \"Agency FB\";\n"
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images_new/weather.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon12)
        self.toolButton_3.setIconSize(QtCore.QSize(70, 100))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setAutoRaise(False)
        self.toolButton_3.setObjectName("toolButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click_toolbutton_21(self):

        icon2 = QtGui.QIcon()
        self.toolButton_21.setIconSize(QtCore.QSize(70, 70))

        if (self.value_toolButton_21 == "ON"):
            self.value_toolButton_21 = "OFF"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_21.setIcon(icon2)
            set_RPi()
            SW1_OFF()


        else:
            self.value_toolButton_21 = "ON"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_21.setIcon(icon2)

            set_RPi()
            SW1_ON()

        print(self.value_toolButton_21)

    def click_toolbutton_22(self):

        icon2 = QtGui.QIcon()
        self.toolButton_22.setIconSize(QtCore.QSize(70, 70))
        if (self.value_toolButton_22 == "ON"):
            self.value_toolButton_22 = "OFF"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_22.setIcon(icon2)
        else:
            self.value_toolButton_22 = "ON"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_22.setIcon(icon2)
        print(self.value_toolButton_22)

    def click_toolbutton_23(self):

        icon2 = QtGui.QIcon()
        self.toolButton_23.setIconSize(QtCore.QSize(70, 70))
        if (self.value_toolButton_23 == "ON"):
            self.value_toolButton_23 = "OFF"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_23.setIcon(icon2)
        else:
            self.value_toolButton_23 = "ON"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_23.setIcon(icon2)
        print(self.value_toolButton_23)

    def click_toolbutton_24(self):

        icon2 = QtGui.QIcon()
        self.toolButton_24.setIconSize(QtCore.QSize(70, 70))
        if (self.value_toolButton_24 == "ON"):
            self.value_toolButton_24 = "OFF"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_24.setIcon(icon2)
        else:
            self.value_toolButton_24 = "ON"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_24.setIcon(icon2)
        print(self.value_toolButton_24)

    def click_toolbutton_25(self):

        icon2 = QtGui.QIcon()
        self.toolButton_25.setIconSize(QtCore.QSize(70, 70))
        if (self.value_toolButton_25 == "ON"):
            self.value_toolButton_25 = "OFF"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_25.setIcon(icon2)
        else:
            self.value_toolButton_25 = "ON"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_25.setIcon(icon2)
        print(self.value_toolButton_25)

    def click_toolbutton_26(self):

        icon2 = QtGui.QIcon()
        self.toolButton_26.setIconSize(QtCore.QSize(70, 70))
        if (self.value_toolButton_26 == "ON"):
            self.value_toolButton_26 = "OFF"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_26.setIcon(icon2)
        else:
            self.value_toolButton_26 = "ON"
            icon2.addPixmap(QtGui.QPixmap("images_new/bulb_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_26.setIcon(icon2)
        print(self.value_toolButton_26)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "HOME AUTOMATION Powered by RASPBERRY PI (Python) + FPGA (VHDL)"))
        self.groupBox.setTitle(_translate("MainWindow", "LIVING ROOM"))
        self.toolButton_21.setText(_translate("MainWindow", "Light 1"))
        self.toolButton_22.setText(_translate("MainWindow", "Light 4"))
        self.toolButton_23.setText(_translate("MainWindow", "Light 2"))
        self.toolButton_24.setText(_translate("MainWindow", "Light 5"))
        self.toolButton_25.setText(_translate("MainWindow", "Light 3"))
        self.toolButton_26.setText(_translate("MainWindow", "Light 6"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DINING ROOM"))
        self.toolButton_33.setText(_translate("MainWindow", "Light 7"))
        self.toolButton_34.setText(_translate("MainWindow", "Light 9"))
        self.toolButton_35.setText(_translate("MainWindow", "Light 8"))
        self.toolButton_36.setText(_translate("MainWindow", "Light 10"))
        self.groupBox_3.setTitle(_translate("MainWindow", "KITCHEN"))
        self.toolButton_37.setText(_translate("MainWindow", "Light 11"))
        self.toolButton_38.setText(_translate("MainWindow", "Light 12"))
        self.groupBox_11.setTitle(_translate("MainWindow", "T and B"))
        self.toolButton_57.setText(_translate("MainWindow", "Light 13"))
        self.toolButton_58.setText(_translate("MainWindow", "Light 14"))
        self.groupBox_5.setTitle(_translate("MainWindow", " MASTER BEDROOM "))
        self.toolButton_41.setText(_translate("MainWindow", "Light 1"))
        self.toolButton_42.setText(_translate("MainWindow", "Light 2"))
        self.toolButton_43.setText(_translate("MainWindow", "Light 3"))
        self.toolButton_44.setText(_translate("MainWindow", "Light 4"))
        self.groupBox_6.setTitle(_translate("MainWindow", "BEDROOM 1"))
        self.toolButton_45.setText(_translate("MainWindow", "Light 5"))
        self.toolButton_46.setText(_translate("MainWindow", "Light 6"))
        self.groupBox_7.setTitle(_translate("MainWindow", "HOBBY ROOM"))
        self.toolButton_47.setText(_translate("MainWindow", "Light 7"))
        self.toolButton_48.setText(_translate("MainWindow", "Light 8"))
        self.groupBox_8.setTitle(_translate("MainWindow", "HOBBY ROOM"))
        self.toolButton_51.setText(_translate("MainWindow", "Light 7"))
        self.toolButton_52.setText(_translate("MainWindow", "Light 8"))
        self.groupBox_9.setTitle(_translate("MainWindow", " T and B"))
        self.toolButton_53.setText(_translate("MainWindow", "Light 9"))
        self.toolButton_54.setText(_translate("MainWindow", "Light 10"))
        self.groupBox_10.setTitle(_translate("MainWindow", "HOBBY ROOM"))
        self.toolButton_55.setText(_translate("MainWindow", "Light 7"))
        self.toolButton_56.setText(_translate("MainWindow", "Light 8"))
        self.groupBox_12.setTitle(_translate("MainWindow", "BEDROOM 2"))
        self.toolButton_59.setText(_translate("MainWindow", "Light 1"))
        self.toolButton_60.setText(_translate("MainWindow", "Light 2"))
        self.toolButton.setText(_translate("MainWindow", "GROUND FLOOR"))
        self.toolButton_10.setText(_translate("MainWindow", "SECOND FLOOR"))
        self.toolButton_11.setText(_translate("MainWindow", "ATTIC"))
        self.toolButton_12.setText(_translate("MainWindow", "GARAGE/GARDEN"))
        self.label.setText(_translate("MainWindow", "30.0 °C"))
        self.label_2.setText(_translate("MainWindow", "  OUTSIDE TEMPERATURE"))
        self.label_4.setText(_translate("MainWindow", "  INSIDE TEMPERATURE"))
        self.label_3.setText(_translate("MainWindow", "20.5 °C"))
        self.groupBox_13.setTitle(_translate("MainWindow", "CLIMATE CONTROL"))
        self.groupBox_14.setTitle(_translate("MainWindow", "TODAY IS"))
        self.label_5.setText(_translate("MainWindow", ":"))
        self.label_6.setText(_translate("MainWindow", "FRIDAY   Nov 24, 2017"))
        self.toolButton_2.setText(_translate("MainWindow", "HOME"))
        self.toolButton_4.setText(_translate("MainWindow", "CONTROLS"))
        self.toolButton_5.setText(_translate("MainWindow", "SETTINGS"))
        self.toolButton_6.setText(_translate("MainWindow", "SETTINGS"))
        self.toolButton_7.setText(_translate("MainWindow", "TIPS"))
        self.toolButton_8.setText(_translate("MainWindow", "STOCKS"))
        self.toolButton_9.setText(_translate("MainWindow", "LOGIN"))
        self.toolButton_3.setText(_translate("MainWindow", "WEATHER"))

def set_RPi():

    # rpi code

    # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output(22, False)

    # Set the modulator to ASK for On Off Keying
    # by setting MODSEL pin lo
    GPIO.output(18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(13, False)

    time.sleep(0.1)

    # print("sending code 1111 socket 1 on")
    # GPIO.output(11, True)
    # GPIO.output(15, True)
    # GPIO.output(16, True)
    # GPIO.output(13, False)
    # # let it settle, encoder requires this
    # time.sleep(0.1)
    # # Enable the modulator
    # GPIO.output(22, True)
    # # keep enabled for a period
    # time.sleep(0.25)
    # # Disable the modulator
    # GPIO.output(22, False)

def SW1_ON():
    print('--------------SOCKET1 ON--------------')

    GPIO.output (11, True)
    GPIO.output (15, True)
    GPIO.output (16, True)
    GPIO.output (13, True)
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)

    GPIO.cleanup()


def SW1_OFF():
    print('--------------SOCKET1 OFF--------------')

    GPIO.output (11, True)
    GPIO.output (15, True)
    GPIO.output (16, True)
    GPIO.output (13, False)
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)

    GPIO.cleanup()


# import try_rc

if __name__ == "__main__":
    import sys

    set_RPi()

    # --end rpi code

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

