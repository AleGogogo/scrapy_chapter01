import requests
from  bs4 import BeautifulSoup
import re
import os

import xlwt
import xlrd
from xlutils.copy import copy



def TengXsearch(fileName,n):
    totileCount = 0
    pageIndex = 1
    dictSet = {}
    resultArray = []
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))
    sheet = workbook.add_sheet("应用宝TOP100", True)
    row0 = ['排名', '名字', '下载量' , '公司']  # 第一行内容
    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)

    while totileCount <= n and pageIndex <= 100:
        url = 'http://android.myapp.com/myapp/cate/appList.htm?orgame=2&categoryId=0&pageSize=20&pageContext=' + str(
            pageIndex)
        pageIndex += 1
        res = requests.get(url)
        originIterm = res.json()
        listArray = originIterm['obj']
        if listArray is None:
            continue
        for row in range(len(listArray)):
            rowItem = listArray[row]
            appId = rowItem['appId']
            name = rowItem['appName']
            if dictSet.get(str(appId)) is None:
                dictSet[str(appId)] = name
                resultArray.append(rowItem)

        totileCount = len(resultArray)


    writefile(resultArray , 0 , row0 , sheet)

    workbook.save(fileName)


def writefile(listArray, page, row0, sheet):
    for clounmIndex in range(len(row0)):
        for rowIndex in range(len(listArray)):
            per = listArray[rowIndex]
            if clounmIndex == 1:
                sheet.write(len(listArray) * page + rowIndex + 1, clounmIndex, per['appName'])
            if clounmIndex == 2:
                sheet.write(len(listArray) * page + rowIndex + 1, clounmIndex, per['appDownCount'])
            if clounmIndex == 3:
                sheet.write(len(listArray) * page + rowIndex + 1, clounmIndex, per['authorName'])
