#-*- coding: utf-8 -*-

import pandas as pd

import sys
sys.path.append(r'.\crawling')

def storeList(raw_num, col_num):
    wb = pd.read_excel(r'.\crawling\common\store_list.xls')
    df_storelist = pd.DataFrame(wb)
    df_storelist.fillna("", inplace=True)
    df_storelist.set_index('store')
    store_list = df_storelist.iloc[raw_num][col_num]
    return store_list


def storeSize():
    wb = pd.read_excel(r'.\crawling\common\store_list.xls')
    df_storelist = pd.DataFrame(wb)
    size = df_storelist.shape[0]
    return size

    

class LogInfo:
    def __init__(self, app):
        self.sales_columns = [['No.','store', app, app, ], ['', '', 'sales', 'quantity']]
        self.review_columns = ['store', 'nick', 'rate', 'view', 'img url', 'img_no', 'img']
        self.frame_sales = pd.DataFrame(
            index=range(0, 1),
            columns= [
                ['No.', 'store', 'baemin', 'baemin', 'yogiyo', 'yogiyo', 'coupang', 'coupang'],
                ['', '', 'sales', 'quantity', 'sales', 'quantity', 'sales', 'quantity']
            ])
        self.frame_review = pd.DataFrame(
            index=range(0, 1),
            columns= self.review_columns
        )

           
    def getStore(self, i):
        store = storeList(i, 1)
        return store
        
    def getBmid(self, i):
        bmid = storeList(i, 2)
        return bmid
    
    def getBmpw(self, i):
        bmpw = storeList(i, 3)
        return bmpw
    
    def getYgyid(self, i):
        ygyid = storeList(i, 4)
        return ygyid
    
    def getYgypw(self, i):
        ygypw = storeList(i, 5)
        return ygypw
    
    def getCpid(self, i):
        cpid = storeList(i, 6)
        return cpid
    
    def getCppw(self, i):
        cppw = storeList(i, 7)
        return cppw