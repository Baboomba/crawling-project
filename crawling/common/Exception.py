import pandas as pd

import sys
sys.path.append(r'.\crawling')

from common.Database import DataProcess
from common.Log_info import LogInfo

### Exception ###

class ErrorProcess(DataProcess, LogInfo):
    def __init__(self, kind):
        LogInfo.__init__(self)
        DataProcess.__init__(self, kind)
        
    
    def error_list(self, store_index, kind:str):
        name = self.getStore(store_index)
        if (kind == 'sales') or (kind == 'tips'):
            error = [store_index, name, 'error', '']
        elif kind == 'review':
            error = [
                name, 'error', '', '', '', ''
            ]
        return error
    
    
    def data_error(self, store_index, kind:str):
        empty = []
        error = self.error_list(store_index, kind)
        empty.append(error)
        result = pd.DataFrame(empty, columns = self.columns)
        return result