# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

import sys
sys.path.append(r'./')      # inserted for images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 350)
        MainWindow.setMinimumSize(QSize(400, 350))
        MainWindow.setMaximumSize(QSize(400, 350))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515 ExtraBold"])
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"GUI/img/bike.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_bg = QFrame(self.centralwidget)
        self.frame_bg.setObjectName(u"frame_bg")
        self.frame_bg.setGeometry(QRect(158, 60, 220, 220))
        self.frame_bg.setFrameShape(QFrame.StyledPanel)
        self.frame_bg.setFrameShadow(QFrame.Raised)
        self.frame_bar = QFrame(self.frame_bg)
        self.frame_bar.setObjectName(u"frame_bar")
        self.frame_bar.setGeometry(QRect(10, 10, 200, 200))
        self.frame_bar.setStyleSheet(u"QFrame {\n"
"	border-radius:100px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(0,0,0,0), stop:0.0001 rgba(157, 162, 250, 255));\n"
"}\n"
"\n"
"")
        self.frame_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_bar.setFrameShadow(QFrame.Raised)
        self.frame_cover = QFrame(self.frame_bar)
        self.frame_cover.setObjectName(u"frame_cover")
        self.frame_cover.setGeometry(QRect(10, 10, 180, 180))
        self.frame_cover.setStyleSheet(u"QFrame {\n"
"	border-radius: 90px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(0,0,0,0), stop:0 rgba(62, 62, 62, 255));\n"
"}\n"
"")
        self.frame_cover.setFrameShape(QFrame.StyledPanel)
        self.frame_cover.setFrameShadow(QFrame.Raised)
        self.label_status = QLabel(self.frame_cover)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(50, 47, 81, 41))
        self.label_status.setLayoutDirection(Qt.LeftToRight)
        self.label_status.setStyleSheet(u"font: 12pt \"Microsoft Tai Le\";\n"
"color: rgb(235, 235, 235);")
        self.label_status.setTextFormat(Qt.PlainText)
        self.label_status.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_percent = QLabel(self.frame_cover)
        self.label_percent.setObjectName(u"label_percent")
        self.label_percent.setGeometry(QRect(63, 82, 61, 41))
        self.label_percent.setStyleSheet(u"color: rgb(235, 235, 235);\n"
"font: 20pt \"Microsoft Tai Le\";")
        self.groupBox_menu = QGroupBox(self.centralwidget)
        self.groupBox_menu.setObjectName(u"groupBox_menu")
        self.groupBox_menu.setGeometry(QRect(18, 15, 120, 311))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Tai Le"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.groupBox_menu.setFont(font1)
        self.groupBox_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_menu.setStyleSheet(u"font: 12pt \"Microsoft Tai Le\";\n"
"color: rgb(235, 235, 235);")
        self.groupBox_menu.setAlignment(Qt.AlignCenter)
        self.groupBox_menu.setFlat(False)
        self.groupBox_menu.setCheckable(False)
        self.btn_run = QPushButton(self.groupBox_menu)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(35, 250, 50, 50))
        self.btn_run.setStyleSheet(u"QPushButton {\n"
"	border-radius:25;\n"
"	color : rgb(62, 62, 62);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(99, 99, 99, 255), stop:1 rgba(189, 189, 189, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 189, 189, 255), stop:1 rgba(99, 99, 99, 255));\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"GUI/img/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_run.setIcon(icon1)
        self.btn_run.setIconSize(QSize(35, 30))
        self.btn_run.setAutoDefault(False)
        self.groupBox_period = QGroupBox(self.groupBox_menu)
        self.groupBox_period.setObjectName(u"groupBox_period")
        self.groupBox_period.setGeometry(QRect(10, 90, 101, 71))
        self.groupBox_period.setStyleSheet(u"font: 10pt \"Microsoft Tai Le\";\n"
"color: rgb(235, 235, 235);")
        self.groupBox_period.setAlignment(Qt.AlignCenter)
        self.radioButton_day = QRadioButton(self.groupBox_period)
        self.radioButton_day.setObjectName(u"radioButton_day")
        self.radioButton_day.setGeometry(QRect(10, 20, 88, 20))
        font2 = QFont()
        font2.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.radioButton_day.setFont(font2)
        self.radioButton_day.setStyleSheet(u"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.radioButton_month = QRadioButton(self.groupBox_period)
        self.radioButton_month.setObjectName(u"radioButton_month")
        self.radioButton_month.setGeometry(QRect(10, 40, 88, 20))
        self.radioButton_month.setStyleSheet(u"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.groupBox_browser = QGroupBox(self.groupBox_menu)
        self.groupBox_browser.setObjectName(u"groupBox_browser")
        self.groupBox_browser.setGeometry(QRect(10, 170, 101, 71))
        self.groupBox_browser.setStyleSheet(u"font: 10pt \"Microsoft Tai Le\";\n"
"color: rgb(235, 235, 235);")
        self.groupBox_browser.setAlignment(Qt.AlignCenter)
        self.radioButton_on = QRadioButton(self.groupBox_browser)
        self.radioButton_on.setObjectName(u"radioButton_on")
        self.radioButton_on.setGeometry(QRect(10, 20, 88, 20))
        self.radioButton_on.setStyleSheet(u"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.radioButton_off = QRadioButton(self.groupBox_browser)
        self.radioButton_off.setObjectName(u"radioButton_off")
        self.radioButton_off.setGeometry(QRect(10, 40, 88, 20))
        self.radioButton_off.setStyleSheet(u"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.groupBox = QGroupBox(self.groupBox_menu)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 30, 101, 51))
        self.groupBox.setStyleSheet(u"font: 10pt \"Microsoft Tai Le\";\n"
"color: rgb(235, 235, 235);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 19, 41, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border-radius:6;\n"
"	color : rgb(62, 62, 62);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(99, 99, 99, 255), stop:1 rgba(189, 189, 189, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 189, 189, 255), stop:1 rgba(99, 99, 99, 255));\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"GUI/img/icons8-list-view-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(23, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        self.statusbar.setWindowIcon(icon)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scraper", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"PROGRESS", None))
        self.label_percent.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.groupBox_menu.setTitle(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_run.setText("")
        self.groupBox_period.setTitle(QCoreApplication.translate("MainWindow", u"TYPE", None))
        self.radioButton_day.setText(QCoreApplication.translate("MainWindow", u"DAY", None))
        self.radioButton_month.setText(QCoreApplication.translate("MainWindow", u"MONTH", None))
        self.groupBox_browser.setTitle(QCoreApplication.translate("MainWindow", u"BROWSER", None))
        self.radioButton_on.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.radioButton_off.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"LIST", None))
        self.pushButton.setText("")
        self.statusbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scraper", None))
    # retranslateUi

