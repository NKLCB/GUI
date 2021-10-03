import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, QBasicTimer
from PyQt5 import uic

first_screen = uic.loadUiType("first_screen.ui")[0]
second_screen = uic.loadUiType("second_screen.ui")[0]


class TestWindow(QMainWindow, first_screen):

    def __init__(self):
        super().__init__()

        self.second_w = None

        self.setupUi(self)
        self.setGeometry(300,300,400,140)
        # Window's size fix width = 400, height  = 140
        self.setFixedSize(400, 140)
        self.start_test()

        # Button to code
        self.checkVersionButton.clicked.connect(self.check_version)
        self.fileSelectButton.clicked.connect(self.file_select)
        self.folderSelectButton.clicked.connect(self.folder_select)

    def start_test(self):
        # Status_bar Show Messages test
        self.statusBar().showMessage('Program Ready')

    def check_version(self):
        #self.statusBar().showMessage('Push Check Version Button')
        pass

    def file_select(self, checked):
        #self.statusBar().showMessage('Push file select Button')
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                print(f.name)
                #filename = os.path.basename(f.name)
                filename = f.name

        if self.second_w is None:
            self.second_w = SecondWindow(filename)
        self.second_w.show()

    def folder_select(self):
        #self.statusBar().showMessage('Push folder select Button')
        pass


class SecondWindow(QMainWindow, second_screen):

    filename = None

    def __init__(self, filename):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(350,350,400,140)
        self.setFixedSize(400,140)
        self.label = QLabel("% s" % filename, self)
        self.cancelButton.clicked.connect(QCoreApplication.instance().quit)
        self.scanButton.clicked.connect(self.test_status)

    def test_status(self):
        self.statusBar().showMessage('Push Start Scan Button')


class ThirdWindow(object): #QMainWindoW?, progress

    def __init__(self):
        self.setupUi()

    def setupUi(self, third_screen):
        third_screen.setObjectName("third_screen")
        third_screen.resize(400, 140)
        self.setWindowTitle("NeKaBe")



#class FinalWindow(object): #Result


if __name__=="__main__":
    # Program start Class
    app = QApplication(sys.argv)

    # TestWindow Class's instance create
    testWindow = TestWindow()

    # Show Program screen 
    testWindow.show()

    # EventLoop 
    app.exec_()
