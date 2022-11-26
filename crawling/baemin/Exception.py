import pandas as pd

### Exception ###
def errorProcess(store_index, log_info, kind):
    store_name = log_info.getStore(store_index)
    empty = []
    
    if kind == 'sale':
        empty.append([store_index, store_name, 'error', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = [['No.','store', 'baemin', 'baemin', ], ['', '', 'sales', 'quantity']])
    else:
        empty.append([store_index, store_name, 'error', '', '', '', ''])
        df_error = pd.DataFrame(empty, index=range(0, 1), columns = ['store', 'nick', 'rate', 'view', 'img url', 'img_no', 'img'])
        
    return df_error