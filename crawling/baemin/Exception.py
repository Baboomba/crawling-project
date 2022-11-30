import pandas as pd

import sys
sys.path.append(r'.\crawling')

from common.Log_info import LogInfo

### Exception ###

class ErrorProcess(LogInfo):
    def __init__(self, app):
        super().__init__(self)
        
    
    def sales_error(self, store_index):
        empty = []
        empty.append([store_index, self.getStore(store_index), 'error', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = self.sales_columns)
        return df_error
    
    
    def review_error(self, store_index):
        empty = []
        empty.append([store_index, self.getStore(store_index), 'error', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = self.review_columns)
        return df_error