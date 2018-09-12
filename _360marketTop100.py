import requests
import json
import os
import xlwt
import xlrd
from xlutils.copy import copy

def _360marketSearch(fileName,n):
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))

    sheet = workbook.add_sheet("360市场TOP100", True)  # 增加一个名称为sheet1的sheet

    row0 = ['排行', '游戏名','下载量(万)','类别']  # 第一行内容
    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)

    url='http://openbox.mobilem.360.cn/app/rank?from=game&type=good_sale&prepage=recommend_ranking&curpage=recommend_ranking_%E6%B8%B8%E6%88%8F%E7%83%AD%E6%A6%9C_%E5%85%A8%E9%83%A8&page=1&os=27&os_version=8.1.0&vc=300070142&v=7.1.42&md=MI+8&sn=4.953045095286574&cpu=qualcomm+technologies%2C+inc+sdm845&ca1=armeabi-v7a&ca2=armeabi&m=3b3ae7a8818fc1d8c4a2448d2bd371e7&m2=e549abfd93d86a5687afd1cbe04e9481&ch=8968329&ppi=1080_2118&startCount=1&pvc=172&pvn=1.7.2&re=1&tid=0&cpc=1&snt=-1&nt=1&gender=1&age=29&newuser=1&theme=2&rm=V10_8.8.31&br=Xiaomi&carrier_id=-1&s_3pk=1&webp=1'
    res = requests.get(url)
    array = res.json()['data']
    for clounmIndex in range(len(row0)):
        for rowIndex in range(len(array)):
            per = array[rowIndex]
            if clounmIndex == 0:
                sheet.write(rowIndex + 1, clounmIndex, rowIndex + 1)
            if clounmIndex == 1:
                sheet.write(rowIndex + 1, clounmIndex, per['name'])
            if clounmIndex == 2:
                download_times = int(per['download_times'])/10000
                sheet.write(rowIndex + 1, clounmIndex, download_times)
            if clounmIndex == 3:
                sheet.write(rowIndex + 1, clounmIndex, per['category_name'])

    workbook.save(fileName)  # 保存workbook为xls格式