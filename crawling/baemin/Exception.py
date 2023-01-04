import pandas as pd

import sys
sys.path.append(r'./')

from common.Log_info import LogInfo
from common.Database import DataProcess

### Exception ###

class ErrorProcess(LogInfo, DataProcess):
    def __init__(self, kind:str):
        LogInfo.__init__(self)
        DataProcess.__init__(self, kind)
        
    
    def sales_error(self, store_index):
        scraped = [store_index, self.getStore(store_index), 'error', '']
        return scraped
    
    
    def tip_error(self, store_index):
        scraped = [store_index, self.getStore(store_index), 'error', '']
        return scraped
    
    
    def review_error(self, store_index):
        empty = []
        empty.append([store_index, self.getStore(store_index), 'error', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = self.columns)
        return df_error