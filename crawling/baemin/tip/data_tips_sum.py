import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl import workbook, worksheet

file_list = os.listdir(r'C:\Users\SEC\Coding\VScode\crawling\baemin\files') # getting the name of files
empty = []

for index, name in enumerate(file_list):    # extracting the name from the files' name
    alt_name = name[21:-8]
    ele = [index, alt_name]
    empty.append(ele)

df_list = pd.DataFrame(empty)


df_list.rename(columns={0:'index', 1:'Name'}, inplace=True)
df_list['tips'] = ''

df_list['index'] = list(range(0, 398))
df_list.reset_index(inplace=True, drop=True)



for x in range(0,398):         # extracting tips from the files
    order = df_list['Name'][x]
    file_dir = r'C:\Users\SEC\Coding\VScode\crawling\baemin\files\배달의민족-2022년10월_정산명세서_{}사장님.xlsx'.format(order)
    wb = load_workbook(file_dir, data_only=True)
    ws = wb['상세']

    tip_sum = []
    
    for m in range(6, 200):    # adding the details
        col1 = ws.cell(row=m, column=7).value
        col2 = ws.cell(row=m, column=8).value
        if col1 or col2 != None:
            col3 = col1 + col2
        tip_sum.append(col3)

    
    tip_sum1 = list(filter(None, tip_sum))
    df_list['tips'][x] = sum(tip_sum1)

df_list.to_excel(r'tips.xlsx')