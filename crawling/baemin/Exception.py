import pandas as pd
from common.Log_info import LogInfo

### Exception ###
def errorProcess(store_index, log_info, kind):
    log_info = LogInfo()
    store_name = log_info.getStore(store_index)
    empty = []
    
    if kind == 'sale':
        empty.append([store_index, store_name, 'error', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = [['No.','store', 'baemin', 'baemin', ], ['', '', 'sales', 'quantity']])
    else:
        empty.append([store_index, store_name, 'error', '', '', '', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = ['store', 'nick', 'rate', 'view', 'img url', 'img_no', 'img'])
        
    return df_error