import requests
from  bs4 import BeautifulSoup
import re
import os
import json

import xlwt
import xlrd
from xlutils.copy import copy





def TengXsearch(fileName, n):
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))
    sheet = workbook.add_sheet("应用宝TOP100", True)
    row0 = ['排名', '名字', '公司','下载量(万)']  # 第一行内容
    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)
    page=0
    for index in range(5):  # 大循环加载一页的内容(30）个
        if index ==0:
            page=0
        if index ==1:
            page = index+20
        elif index>1:
            page = 21+27*(index-1)
        print('page is'+str(page))
        url = 'http://android.myapp.com/myapp/cate/appList.htm?orgame=2&categoryId=0&pageSize=20&pageContext='+str(page)
        res =requests.get(url)
        originIterm = res.json()
        listArray=originIterm['obj']
        print('len is' +str(len(listArray)))
        writefile(listArray, 0, row0, sheet)
    workbook.save(fileName)

def writefile(listArray, page, row0, sheet):
    if len(listArray) == 0:
        return
    for clounmIndex in range(len(row0)):
        for rowIndex in range(len(listArray)):
            per = listArray[rowIndex]
            if clounmIndex == 0:
                sheet.write(len(listArray) * page + rowIndex + 1, clounmIndex, len(listArray) * page+1+rowIndex)
            if clounmIndex == 1:
                sheet.write(len(listArray) * page + rowIndex + 1,clounmIndex,per['appName'])
            if clounmIndex == 2:
                sheet.write(len(listArray) * page + rowIndex + 1, clounmIndex, per['authorName'])
            if clounmIndex == 3:
                sheet.write(len(listArray) * page + rowIndex + 1, clounmIndex, per['appRatingInfo']['ratingCount'])
