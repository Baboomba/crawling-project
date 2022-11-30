import datetime
import pandas as pd

from openpyxl.drawing.image import Image
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment

import sys
sys.path.append(r'.\crawling')

from common.Log_info import LogInfo


class SaveData(LogInfo):
    def __init__(self, app, kind):
        super().__init__(app)
        yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
        day = yesterday.strftime('%Y%m%d')
        self.data_dir_day = r'.\crawling\result\{}_{}_{}.xlsx'.format(app, kind, day)
        self.data_dir_month = r'.\crawling\result\{}_{}.xlsx'.format(app, kind)
    
    
    def sales_day(self, store_index, df_result):
        global df_sales
        
        if store_index == 0:
            df_sales = self.frame_sales
        
        df_sales = pd.concat([df_sales, df_result])
        df_sales.to_excel(self.data_dir_day)
        return df_sales
    
    
    def sales_month(self, store_index, df_result):
        global df_month
        
        if store_index == 0:
            df_month = self.frame_sales
        
        df_month = pd.concat([df_month, df_result])
        df_month.to_excel(self.data_dir_month)
        return df_month
    
    
    def review_BM(self, store_index, df_result):
        global df_review
        
        if store_index == 0:
            df_review = self.frame_review
                    
        df_review = pd.concat([df_review, df_result])
        df_review.fillna('', inplace=True)
        df_review.to_excel(self.data_dir)
        return df_review
    
    
    def process_data(self):
        wb = load_workbook(self.data_dir)
        ws = wb.active
        ws.column_dimensions[get_column_letter(1)].width = 3.5
        ws.column_dimensions[get_column_letter(2)].width = 11.5
        ws.column_dimensions[get_column_letter(3)].width = 11.5
        ws.column_dimensions[get_column_letter(4)].width = 4
        ws.column_dimensions[get_column_letter(5)].width = 60
        ws.column_dimensions[get_column_letter(6)].width = 11.5
        ws.column_dimensions[get_column_letter(7)].width = 4.5
        ws.column_dimensions[get_column_letter(8)].width = 30
        
        for row in range(2, ws.max_row + 1):
            ws.row_dimensions[row].height = 150
        
        for order in range(0, ws.max_column):
            ws[row][order].alignment = Alignment(horizontal = 'center', vertical='center', wrap_text=True)
    
        for image_rows in range(2, ws.max_row + 1):
            img_no = ws[image_rows][6].value
            try:
                review_img = Image(r'.\crawling\download\baemin_img\{}.jpg'.format(img_no))
                review_img.height = 200
                review_img.width = 200
                ws.add_image(review_img, 'H{}'.format(image_rows))
            except:
                continue
        
        wb.save(self.data_dir)


    def set_index(self):
        df_sales.set_index('No.', drop=True, inplace=True)
        df_sales.fillna("", inplace=True)
        df_sales.to_excel(self.data_dir)
    
            
        



def dataDir(app, kind):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    day = yesterday.strftime('%Y%m%d')
    data_dir = r'.\crawling\result\{}_{}_{}.xlsx'.format(app, kind, day)
    return data_dir


### Save data ###
def saveSales(store_index, df_result, app, kind):
    data_dir = dataDir(app, kind)
    global df_sales
        
    if store_index == 0:
        columns = [['No.', 'store', 'baemin', 'baemin', 'yogiyo', 'yogiyo', 'coupang', 'coupang'],
            ['', '', 'sales', 'quantity', 'sales', 'quantity', 'sales', 'quantity']
            ]
        df_sales = pd.DataFrame(index=range(0, 1), columns=columns)
        
    df_sales = pd.concat([df_sales, df_result])
    df_sales.to_excel(data_dir)
    
    return df_sales


def saveSales_month(store_index, df_result):
    data_dir = f'.\crawling\result\baemin_month.xlsx'
    global df_month
        
    if store_index == 0:
        columns = [['No.', 'store', 'baemin', 'baemin', 'yogiyo', 'yogiyo', 'coupang', 'coupang'],
            ['', '', 'sales', 'quantity', 'sales', 'quantity', 'sales', 'quantity']
            ]
        df_month = pd.DataFrame(index=range(0, 1), columns=columns)
        
    df_month = pd.concat([df_month, df_result])
    df_month.to_excel(data_dir)
    
    return df_month


def saveReview(store_index, df_result, app, kind):
    global df_review
    data_dir = dataDir(app, kind)
    
    if store_index == 0:
        df_review = pd.DataFrame(index=range(0, 1), columns=['store', 'nick', 'rate', 'view', 'img url', 'img_no', 'img'])
    else:
        pass
        
    df_review = pd.concat([df_review, df_result])
    df_review.fillna('', inplace=True)
    df_review.to_excel(data_dir)
    
    return df_review
    


### Processing Review data in Excel ###
def processData(app, kind):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    day = yesterday.strftime('%Y%m%d')
    data_dir = dataDir(app, kind)
    wb = load_workbook(data_dir)
    ws = wb.active

    ws.column_dimensions[get_column_letter(1)].width = 3.5
    ws.column_dimensions[get_column_letter(2)].width = 11.5
    ws.column_dimensions[get_column_letter(3)].width = 11.5
    ws.column_dimensions[get_column_letter(4)].width = 4
    ws.column_dimensions[get_column_letter(5)].width = 60
    ws.column_dimensions[get_column_letter(6)].width = 11.5
    ws.column_dimensions[get_column_letter(7)].width = 4.5
    ws.column_dimensions[get_column_letter(8)].width = 30
    
    for row in range(2, ws.max_row + 1):
        ws.row_dimensions[row].height = 150
        for order in range(0, ws.max_column):
            ws[row][order].alignment = Alignment(horizontal = 'center', vertical='center', wrap_text=True)
    
    for image_rows in range(2, ws.max_row + 1):
        img_no = ws[image_rows][6].value
        try:
            review_img = Image(r'.\crawling\download\baemin_img\{}.jpg'.format(img_no))
            review_img.height = 200
            review_img.width = 200
            ws.add_image(review_img, 'H{}'.format(image_rows))
        except:
            continue

    wb.save(r'.\crawling\result\{}_{}_{}.xlsx'.format(app, kind, day))
    
    return print('complete')