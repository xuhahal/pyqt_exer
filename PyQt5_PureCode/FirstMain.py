# -*- coding:utf-8 -*-

# @Time    : 2021/8/8 17:32
# @Author  : Xutm
# @Language: python3.6.5
# @description: 第一个python代码的窗口程序

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        self.resize(600,400)

        self.setWindowTitle("第一个主窗口程序")

        self.status = self.statusBar()
        self.status.showMessage("停留5s", 5000)
        # self.center()
    def center(self):
        size = self.geometry()

        screen = QDesktopWidget().screenGeometry()

        newLeft = (screen.width()-size.width()) / 2
        newTop = (screen.height()-size.height()) / 2

        self.move(newLeft, newTop)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./china.ico'))
    firstMain = FirstMainWin()

    firstMain.show()
    sys.exit(app.exec_())