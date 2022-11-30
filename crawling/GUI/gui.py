### Setup Modules ###
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic


# label = QLabel("Hello")
# label.show()

# button = QPushButton('Hello, world!')
# button.show()


form_class = uic.loadUiType("design.ui")[0]  # An object to connect UI file with python file


class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__(self)
        self.setupUi(self)
        self.setGeometry(800, 250, 250, 350)
        self.setWindowTitle("Frankraft")
        self.setWindowIcon(QIcon(r'C:\Users\SEC\Coding\VScode\crawling\GUI\img\bike_red.png'))
    
    def menubar(self):
        menu_open = self.menuBar().addMenu("&File")
        
        exit_action = QAction(QMenuBar(self))
        exit_action.triggered.connect(self.click)
    
    def click(self):
        print('sucess')
        

    
    
    


    
    #self.comboBox.currentTextChanged.connect(self.showTable)
    
    
    
    #def showTable(self):
     
    
    # def showResult(self):
                
    #     df_store = pd.read_excel(r'C:\Users\SEC\Coding\VScode\crawling\result\baemin_review_20221117.xlsx')
    #     self.tableWidget.setRowCount(df_store.shape[0])
    #     self.tableWidget.setColumnCount(9)
        
    #     for i in range(len(df_store)):
    #         for j in range(0, 9):
    #             self.tableWidget.setItem(i, j, QTableWidgetItem(df_store.iloc[i][j]))
                
                
    # def showProgress(self, store_index):
    #     return self.progressBar.setValue(store_index)
    
        

def gui_main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

gui_main()