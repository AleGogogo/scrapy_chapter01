import requests
from  bs4 import BeautifulSoup
import re
import os

import xlwt
import xlrd
from xlutils.copy import copy

def TengXsearch(fileName,n):
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))
    sheet = workbook.add_sheet("应用宝TOP100", True)
    row0 = ['排名', '名字', '下载量']  # 第一行内容
    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)

    for page in range(3):  # 大循环加载一页的内容(30）个
        url = 'http://sj.qq.com/myapp/category.htm?orgame=2'
        res =requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        datas = soup.find_all('div',class_="app-info-desc")
        downloads = soup.find_all('span', class_="download")
        for clounmIndex in range(len(row0)):
            for rowIndex in range(len(datas)):
                name = datas[rowIndex].a.string
                download = re.findall(r'下载(.*?)次',downloads[rowIndex].string)
                if clounmIndex == 0:
                    sheet.write(len(datas)*page+rowIndex+1,clounmIndex,len(datas)*page+rowIndex+1)
                if clounmIndex == 1:
                    sheet.write(len(datas)*page+rowIndex + 1, clounmIndex, name)
                if clounmIndex == 2:
                    sheet.write(len(datas)*page+rowIndex + 1, clounmIndex, download)

    workbook.save(fileName)