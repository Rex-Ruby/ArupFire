from sys import exit, argv
from PyQt5.QtWidgets import QApplication
from ui_DCM import Ui_MainWindow
from  PyQt5.QtWidgets import QMainWindow

if __name__ == '__main__':
        app = QApplication(argv)
        mainWindow = QMainWindow()
        ui = Ui_MainWindow()
        mainWindow.show()
        ui.setupUi(mainWindow)
        # ui.retranslateUi(mainWindow)
        # retranslateUi()函数在setupUi()函数中已被调用，不再重复调用
        # ui.show()
        exit(app.exec_())