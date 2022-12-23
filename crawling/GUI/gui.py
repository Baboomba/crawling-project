### Setup Modules ###
import os, sys
sys.path.append(r'./crawling')

import pyautogui
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtCore, QtWidgets, QtGui

from baemin.Run_minimum import scrapeBM_min_path
from GUI.design import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.run_btn.clicked.connect(self.click_run)
        self.stop_btn.clicked.connect(self.click_stop)
        self.progressBar.setValue(0)
        self.dateStart.connect()

        
    
    
    def click_run(self):
        import time
        for x in range(101):
            self.progressBar.setValue(x)
            time.sleep(0.1)
            
    def click_stop(self):
        terminal_command = "exit()"
        os.system(terminal_command)
    
    
    def show_browser(self):
        if self.radioButton.clicked():
            return True
        elif self.radioButton_2.clicked():
            return False
    
    
    def run_program(self):
        headless = self.show_browser()
        if headless != None:
            self.pushButton.clicked.connected(scrapeBM_min_path(headless))
        
        
    def progress_status(self):
        self.progressBar.setValue(100)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()



############################################################################################
# ui 파일을 직접 사용할 때 사용하는 코드
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     ui_file_name = r".\crawling\GUI\design.ui"
#     ui_file = QFile(ui_file_name)
#     if not ui_file.open(QIODevice.ReadOnly):
#         print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
#         sys.exit(-1)
#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     ui_file.close()
#     if not window:
#         print(loader.errorString())
#         sys.exit(-1)
#     window.show()
#
#     sys.exit(app.exec())
############################################################################################