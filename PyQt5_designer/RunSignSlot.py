# -*- coding:utf-8 -*-

# @Time    : 2021/8/4 17:13
# @Author  : Xutm
# @Language: python3.6.5
# @description:

import SignalSlot
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    ui = SignalSlot.Ui_Form()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())