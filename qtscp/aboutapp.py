# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.setEnabled(True)
        Dialog.resize(292, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(292, 130))
        Dialog.setMaximumSize(QtCore.QSize(292, 130))
        Dialog.setBaseSize(QtCore.QSize(337, 291))
        Dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app/img/App_OpenCubicPlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 0, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 90, 71, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 50, 171, 31))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 31, 171))
        self.widget.setStyleSheet("background:#B8B8B8")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About QtSCP"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:496; color:#41cd52;\">Qt</span><span style=\" font-size:24pt; font-weight:496;\">SCP </span>0.0.1b3</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/app/img/App_OpenCubicPlayer.png\"/><img src=\":/default/img/app/App_OpenCubicPlayer.png\"/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Noto Sans Display\'; font-size:9pt; color:#000000;\">Unoffical Qt client of SCP </span><span style=\" font-family:\'Noto Sans Display\'; font-size:9pt;\">Copyright (C) 2020</span><span style=\" font-family:\'Noto Sans Display\'; font-size:9pt; color:#000000;\"> @jDan735</span></p></body></html>"))
import images_rc