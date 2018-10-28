import pathlib

import requests
import json
import os

import xlwt
import xlrd
from xlutils.copy import copy
from src.cons.constant import ValueName


def yiguanSearchData(keyword, topCount, fileName):
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))

    sheet = workbook.add_sheet("易观游戏TOP100" , True)  # 增加一个名称为sheet1的sheet

    row0 = [ValueName.rank, ValueName.name, ValueName.download_count, ValueName.download_count_day,ValueName.company]  # 第一行内容

    r = requests.post("http://zhishu.analysys.cn/public/qianfan/appSearch/searchData",
                      data={'words': keyword, 'pageType': 'all', 'page': '1', 'pageSize': topCount})
    listArray = r.json()['datas']['list']

    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)

    for clounmIndex in range(len(row0)):
        for rowIndex in range(len(listArray)):
            per = listArray[rowIndex]
            if clounmIndex == 0:
                sheet.write(rowIndex + 1, clounmIndex, rowIndex + 1)
            if clounmIndex == 1:
                sheet.write(rowIndex + 1, clounmIndex, per['appName'])
            if clounmIndex == 2:
                sheet.write(rowIndex + 1, clounmIndex, per['monthActiveNums'])
            if clounmIndex == 3:
                sheet.write(rowIndex + 1, clounmIndex, per['dayActiveNums'])
            if clounmIndex == 4:
                sheet.write(rowIndex + 1, clounmIndex, per['developCompanyFullName'])
    workbook.save(fileName)  # 保存workbook为xls格式

    return
