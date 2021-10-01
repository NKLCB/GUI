import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("first_screen.ui")[0]

class TestWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

    def file_select(self):
        #self.statusBar().showMessage('Push file select Button')
        pass

    def folder_select(self):
        #self.statusBar().showMessage('Push folder select Button')
        pass


if __name__=="__main__":
    # Program start Class
    app = QApplication(sys.argv)

    # TestWindow Class's instance create
    testWindow = TestWindow()

    # Show Program screen 
    testWindow.show()

    # EventLoop 
    app.exec_()
