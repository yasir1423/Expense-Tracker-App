# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(786, 531)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.pushButton_2 = QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/images/account - Copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(40, 40))
        self.pushButton_2.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_2)
        self.pushButton = QPushButton(self.splitter_2)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/home (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 40))
        self.pushButton.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton)
        self.pushButton_3 = QPushButton(self.splitter_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/images/remove (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(40, 40))
        self.pushButton_3.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QPushButton(self.splitter_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon3 = QIcon()
        icon3.addFile(u":/images/remove (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(40, 40))
        self.pushButton_5.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QPushButton(self.splitter_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon4 = QIcon()
        icon4.addFile(u":/images/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(40, 40))
        self.pushButton_4.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_4)

        self.verticalLayout.addWidget(self.splitter_2)

        self.verticalSpacer = QSpacerItem(20, 151, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/images/user-logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(40, 40))
        self.pushButton_6.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_6)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(30, 30))
        self.pushButton_8.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QSize(30, 30))
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QSize(30, 30))
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.verticalSpacer_2 = QSpacerItem(20, 207, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(30, 30))
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_12)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addpage = QStackedWidget(self.widget_3)
        self.addpage.setObjectName(u"addpage")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.splitter_4 = QSplitter(self.page)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.tableWidget_home = QTableWidget(self.splitter_4)
        self.tableWidget_home.setObjectName(u"tableWidget_home")
        self.splitter_4.addWidget(self.tableWidget_home)
        self.btn_home_showall = QPushButton(self.splitter_4)
        self.btn_home_showall.setObjectName(u"btn_home_showall")
        self.btn_home_showall.setFont(font)
        self.btn_home_showall.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btn_home_showall.setCheckable(True)
        self.splitter_4.addWidget(self.btn_home_showall)

        self.verticalLayout_6.addWidget(self.splitter_4)

        self.addpage.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 140, 251, 91))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.label.setFont(font1)
        self.addpage.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.page_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.page_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.page_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.page_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.page_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.page_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_3.addWidget(self.lineEdit_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.page_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_2.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.page_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.btn_add_expense = QPushButton(self.page_4)
        self.btn_add_expense.setObjectName(u"btn_add_expense")
        self.btn_add_expense.setFont(font)
        self.btn_add_expense.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btn_add_expense.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_add_expense)

        self.addpage.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_4 = QVBoxLayout(self.page_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.page_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_14.addWidget(self.lineEdit_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.page_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_13.addWidget(self.lineEdit_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.page_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_12.addWidget(self.lineEdit_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.page_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.lineEdit_11 = QLineEdit(self.page_5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_11.addWidget(self.lineEdit_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.page_5)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_10.addWidget(self.lineEdit_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.page_5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.lineEdit_13 = QLineEdit(self.page_5)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_9.addWidget(self.lineEdit_13)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.lineEdit_14 = QLineEdit(self.page_5)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_8.addWidget(self.lineEdit_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.btn_update_edit = QPushButton(self.page_5)
        self.btn_update_edit.setObjectName(u"btn_update_edit")
        self.btn_update_edit.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btn_update_edit.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_update_edit)

        self.tableWidget = QTableWidget(self.page_5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_15 = QPushButton(self.page_5)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.pushButton_15.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.pushButton_15)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.btn_extract_edit = QPushButton(self.page_5)
        self.btn_extract_edit.setObjectName(u"btn_extract_edit")
        self.btn_extract_edit.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btn_extract_edit.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.btn_extract_edit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.addpage.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_5 = QVBoxLayout(self.page_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget_2 = QTableWidget(self.page_6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_5.addWidget(self.tableWidget_2)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_showall_remove = QPushButton(self.page_6)
        self.btn_showall_remove.setObjectName(u"btn_showall_remove")
        self.btn_showall_remove.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btn_showall_remove.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.btn_showall_remove)

        self.horizontalSpacer_2 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.btn_remove_remove = QPushButton(self.page_6)
        self.btn_remove_remove.setObjectName(u"btn_remove_remove")
        self.btn_remove_remove.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btn_remove_remove.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.btn_remove_remove)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.addpage.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.addpage.addWidget(self.page_2)

        self.gridLayout.addWidget(self.addpage, 0, 1, 1, 1)

        self.btn_setup = QPushButton(self.widget_3)
        self.btn_setup.setObjectName(u"btn_setup")
        icon6 = QIcon()
        icon6.addFile(u":/images/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_setup.setIcon(icon6)
        self.btn_setup.setIconSize(QSize(40, 40))
        self.btn_setup.setCheckable(True)

        self.gridLayout.addWidget(self.btn_setup, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_setup.toggled.connect(self.widget_2.setVisible)
        self.btn_setup.toggled.connect(self.widget.setHidden)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)
        self.pushButton_5.toggled.connect(self.pushButton_10.setChecked)
        self.pushButton_10.toggled.connect(self.pushButton_5.setChecked)
        self.pushButton_4.toggled.connect(self.pushButton_11.setChecked)
        self.pushButton_11.toggled.connect(self.pushButton_4.setChecked)
        self.pushButton_9.toggled.connect(self.pushButton_3.setChecked)
        self.pushButton_3.toggled.connect(self.pushButton_9.setChecked)
        self.pushButton_9.toggled.connect(self.pushButton_3.setChecked)
        self.pushButton_2.toggled.connect(self.pushButton_8.setChecked)
        self.pushButton_8.toggled.connect(self.pushButton_2.setChecked)
        self.pushButton.toggled.connect(self.pushButton_7.setChecked)
        self.pushButton_7.toggled.connect(self.pushButton.setChecked)

        self.addpage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.pushButton_6.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.btn_home_showall.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Upload Here", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Expense:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Remaining:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Review:", None))
        self.btn_add_expense.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Expense:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Remaining:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Review:", None))
        self.btn_update_edit.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.btn_extract_edit.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.btn_showall_remove.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.btn_remove_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btn_setup.setText("")
    # retranslateUi

