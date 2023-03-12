import sys
from PyQt5.QtWidgets import *

from PyQt5 import QtGui, QtWidgets
import cv2
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 500

        # 设置软件图标（可省略）
        self.setWindowIcon(QtGui.QIcon("zzp.ico"))
        # 设置主界面标题
        self.setWindowTitle("张子庞2101010340")
        # 设置固定尺寸
        self.setFixedSize(self.width, self.height)
        # 设置主界面背景色
        self.setStyleSheet("background-color:rgb(255,255,255)")

        self.init_widget()

    def init_widget(self):
        self.button = QtWidgets.QPushButton('点击我', self)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print('你点击了按钮')
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileNames(self, "选择图片", "./",
                                                                    "Image Files (*.png *.jpg *.bmp *.ico)")
        print(fileName)

        imageList = []
        for i in fileName:
            imageList.append(cv2.imread(i))

        self.showImage(imageList)

    def showImage(self, imageList):
        fig = plt.gcf()
        fig.set_size_inches(20, 20)
        idx = 0
        for i in range(0, len(imageList)):
            ax = plt.subplot(1, len(imageList), 1 + i)
            ax.imshow(imageList[idx], cmap='gray')
            ax.set_xticks([])
            ax.set_yticks([])
            idx += 1
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
