# -*- coding:utf-8 -*-

# @Time    : 2021/8/12 12:13
# @Author  : Xutm
# @Language: python3.6.5
# @description: quit application(完结)

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication,\
    QPushButton, QHBoxLayout, QFormLayout


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,300)
        self.move(300,300)

        self.button1 = QPushButton('退出程序')
        self.button1.clicked.connect(self.on_clickedButton)
        mainFrame = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


    def on_clickedButton(self):
        sender = self.sender()
        print(sender.text()+' 按钮被按下！')
        app1 = QApplication.instance()
        app1.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QuitApplication()
    mainWin.show()
    sys.exit(app.exec_())




