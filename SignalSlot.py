# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignalSlot.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(713, 565)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(140, 150, 91, 19))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 270, 111, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 190, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(140, 310, 104, 87))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        self.checkBox.toggled['bool'].connect(self.lineEdit.setVisible)
        self.checkBox_2.toggled['bool'].connect(self.textEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "关闭窗口"))
        self.checkBox.setText(_translate("Form", "显示/隐藏"))
        self.checkBox_2.setText(_translate("Form", "可用/不可用"))
