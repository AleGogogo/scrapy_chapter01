import pathlib

import requests
import os

import xlwt
import xlrd
from xlutils.copy import copy

def talkingdataSearch(fileName,data,n):
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))

    sheet = workbook.add_sheet("talkingDataTOP100", True)

    row0=['排名','名字'] # 第一行内容

    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)

    for index in range(n/40+1):# 大循环加载一页的内容(30）个
        url='http://mi.talkingdata.com/appstore/rank.json?date='+str(data)+'&cat=6014&tab=1&page='+str(index)+'&pagesize=30'
        print(index)
        res =requests.get(url)
        originItem=res.json()
        listArray= originItem['rows']
        writefile(listArray,index,row0,sheet)

    workbook.save(fileName)  # 保存workbook为xls格式

def writefile(listArray,page,row0,sheet):
    for clounmIndex in range(len(row0)):
        for rowIndex in range(len(listArray)):
            per = listArray[rowIndex]
            if clounmIndex == 0:
                sheet.write(len(listArray)*page+rowIndex+1,clounmIndex,per['rank'])
            if clounmIndex == 1:
                sheet.write(len(listArray) * page + rowIndex+1, clounmIndex, per['appinfo']['name'])
