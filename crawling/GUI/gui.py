### Main Modules ###
import os, sys
sys.path.append(r'./')

from GUI.design import Ui_MainWindow
from PySide6 import QtWidgets, QtGui

### Additional Modules ###
import pandas as pd
import threading
import win32com.client

### My Modueles ###
from common.DriverSet import DriverSet
from common.Log_info import LogInfo
from baemin.LogBM import LogProcess_BM
from baemin.path import FindPath
from baemin.getSale import ScrapeSales
from baemin.Exception import ErrorProcess
from common.Save import SaveData
from common.Database import DataProcess




class ScraperGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ScraperGUI, self).__init__()
        self.setupUi(self)
        self.btn_run.clicked.connect(self.run_clicked)
        self.pushButton.clicked.connect(self.list_clicked)
    
    
    def list_clicked(self):
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = True
        path = os.path.abspath(r'./common/store_list.xlsx')
        wb = excel.Workbooks.Open(path)
        return wb


    def run_clicked(self):
        check_A = self.radioButton_day.isChecked() or self.radioButton_month.isChecked()
        check_B = self.radioButton_off.isChecked() or self.radioButton_on.isChecked()
                
        if check_A and check_B:
            fname = QtWidgets.QFileDialog.getSaveFileName(filter='xlsx')
            global save_dir
            save_dir = f'{fname[0]}.{fname[1]}'
            
            if save_dir != '.':
                self.groupBox_menu.setEnabled(False)
                thread = threading.Thread(target=self.scrapeBM_min_path)
                thread.daemon = True
                thread.start()
            else:
                pass
            
        else:
            self.alert_option_check()


    def alert_option_check(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Alert")
        msg.setText("<p align='center'>선택하지 않은 옵션이 있습니다.</p>")
        msg.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
        return msg.show()


    def type_condition(self):
        if self.radioButton_day.isChecked():
            day = 'yesterday'
            return day
        else:
            month = 'month'
            return month
        

    def browser_condition(self):
        if self.radioButton_on.isChecked():
            return False
        else:
            return True
        
        
    def return_conditions(self):
        period = self.type_condition()
        headless = self.browser_condition()
        values = [period, headless]
        return values


    def progress_status(self, progress):
        info = LogInfo()
        size = info.store_size()
        ratio = (progress)/size
        percent = int(ratio*100)
        
        self.label_percent.setText(f'{percent}%')
        self.frame_bar.setStyleSheet("border-radius:100px;"
                             f"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90,\
                                 stop:{1-ratio} rgba(0,0,0,0),\
                                     stop:{1.0001-ratio} rgba(157, 162, 250, 255))"
                             )
    
    
    def complete_message(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Complete")
        msg.setText("<p align='center'>수집 완료</p>")
        msg.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
        return msg.show()

        

    def scrapeBM_min_path(self):
        info = LogInfo()
        login = LogProcess_BM()
        path = FindPath()
        scrape = ScrapeSales()
        error = ErrorProcess(kind='sales')
        save = SaveData()
        data = DataProcess(kind='sales')
        Driver = DriverSet()
        
        URL = r'https://ceo.baemin.com/'
        
        headless = self.browser_condition()
        time = self.type_condition()
        driver = Driver.driver_run(headless)
        driver.get(URL)
        size = info.store_size()
        global result_sales
        global save_dir
        result_sales = data.make_frame(kind='sales')
        
        
        for store_index in range(0, size):
            self.progress_status(progress=store_index)
            try:
                login.main_page(driver)
                login.login(driver, store_index)
                login.pass_change(driver)
                login.biz_uni(driver)
                if login.log_check(driver) == True:
                    pass
                else:
                    driver.get(URL)
                    continue
                path.simple_path(driver)
                
                if time == 'yesterday':
                    scrape.calandar_click(driver)
                    scrape.select_yesterday(driver)
                    scraped = scrape.list_sales(driver, store_index)
                    result_sales = data.result_process(result_sales, scraped)
                    result_sales.to_excel(save_dir)
                    login.logout_another(driver)
                else:
                    scrape.calandar_click(driver)
                    scrape.select_month(driver)
                    scraped = scrape.list_sales(driver, store_index)
                    result_sales = data.result_process(result_sales, scraped)
                    result_sales.to_excel(save_dir)
                    login.logout_another(driver)
                
            except:
                print(f'error in {store_index}th store')
                scraped_error = error.sales_error(store_index)
                result_sales = data.result_process(result_sales, scraped_error)
                result_sales.to_excel(save_dir)
                driver.quit()
                driver = Driver.driver_run(headless)
                driver.get(URL)
        
        result_sales = save.set_index(result_sales)
        result_sales.to_excel(save_dir)
        
        driver.quit()
        self.label_percent.setText('100%')
        self.frame_bar.setStyleSheet("border-radius:100px;"
                             f"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90,\
                                 stop:0 rgba(0,0,0,0),\
                                     stop:0.0001 rgba(157, 162, 250, 255))"
                             )




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ScraperGUI()
    window.show()
    app.exec_()