# -*- coding:utf-8 -*-

# @Time    : 2021/8/12 12:13
# @Author  : Xutm
# @Language: python3.6.5
# @description: quit application(完结)

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()
        # 创建一个垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        # 将窗口布局设置为vbox布局
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)
        self.setLayout(vbox)
        self.setWindowTitle("一个QLabel测试")
        # 设置各个标签的功能
        label1.setText("<font color = yellow>这是label1，欢迎使用</font>")
        label1.setAlignment(Qt.AlignCenter)
        label1.setAutoFillBackground(True)
        label1.setPalette(palette)

        label2.setText("<a href='#'>这是一个滑动标签</a>")
        label2.setToolTip("啥用没有")

        label2.setAlignment(Qt.AlignCenter)
        label2.setAutoFillBackground(True)
        label2.setPalette(palette)

        label3.setPixmap(QPixmap('./china.ico'))
        label3.setAlignment(Qt.AlignCenter)

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://baidu.com'>百度一下，看看呗</a>")
        label4.linkActivated.connect(self.LabelClicked)
        label4.setAlignment(Qt.AlignRight)

        label2.linkHovered.connect(self.linkHovered)  # linkhovered事件触发必须是超链接的标签
    def linkHovered(self):
        print('鼠标滑过label2')


    def LabelClicked(self):
        print("鼠标点击label4")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLabelDemo()
    mainWin.show()
    sys.exit(app.exec_())




