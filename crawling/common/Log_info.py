#-*- coding: utf-8 -*-

import pandas as pd

import sys
sys.path.append(r'./')

    

class LogInfo:
    def __init__(self):
        self.wb_read = pd.read_excel(r'./common/store_list.xlsx')
        self.df_storelist = pd.DataFrame(self.wb_read)
    
    
    def store_list(self, raw_num, col_num):
        self.df_storelist.fillna("", inplace=True)
        self.df_storelist.set_index('store')
        store_list = self.df_storelist.iloc[raw_num][col_num]
        return store_list
        
    
    def store_size(self):
        size = self.df_storelist.shape[0]
        return size
    
           
    def getStore(self, i):
        store = self.store_list(i, 1)
        return store
        
        
    def getBmid(self, i):
        bmid = self.store_list(i, 2)
        return bmid
    
    
    def getBmpw(self, i):
        bmpw = self.store_list(i, 3)
        return bmpw
    
    
    def getYgyid(self, i):
        ygyid = self.store_list(i, 4)
        return ygyid
    
    
    def getYgypw(self, i):
        ygypw = self.store_list(i, 5)
        return ygypw
    
    
    def getCpid(self, i):
        cpid = self.store_list(i, 6)
        return cpid
    
    
    def getCppw(self, i):
        cppw = self.store_list(i, 7)
        return cppw
    
if __name__ == '__main__':
    info = LogInfo()
    size = info.store_size()
    print(size)
    print(type(size))