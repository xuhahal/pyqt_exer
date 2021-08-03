# -*- coding:utf-8 -*-

# @Time    : 2021/8/3 21:44
# @Author  : Xutm
# @Language: python3.6.5

import sys
# 主要的两个类
from PyQt5.QtWidgets import QApplication,QWidget

# 创建一个app实例
app = QApplication(sys.argv)
# 创建一个窗口
w = QWidget()

# 设置窗口尺寸
w.resize(500,500)
# 移动到相应的位置
w.move(300,300)
# 设置窗口标题
w.setWindowTitle("第一个窗口程序")
# 显示窗口
w.show()
# 安全退出程序
sys.exit(app.exec_())
