import datetime
import pandas as pd

from openpyxl.drawing.image import Image
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment





def dataDir(app, kind):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    day = yesterday.strftime('%Y%m%d')
    data_dir = r'C:\Users\SEC\Coding\VScode\crawling\result\{}_{}_{}.xlsx'.format(app, kind, day)
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
            review_img = Image(r'C:\Users\SEC\Coding\VScode\crawling\download\baemin_img\{}.jpg'.format(img_no))
            review_img.height = 200
            review_img.width = 200
            ws.add_image(review_img, 'H{}'.format(image_rows))
        except:
            continue

    wb.save(r'C:\Users\SEC\Coding\VScode\crawling\result\{}_{}_{}.xlsx'.format(app, kind, day))
    
    return print('complete')