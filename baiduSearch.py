

import requests
import os
import re

import xlwt
import xlrd
from xlutils.copy import copy



# board_id	board_100_7003
# 目前借口只能拿到前100
def getSearchData(boardId, fileName):
    fileName = fileName + ".xls"
    if not os.path.exists(fileName):
        workbook = xlwt.Workbook()  # 使用xlwt新生成一个workbook
    else:
        workbook = copy(xlrd.open_workbook(fileName))

    sheet = workbook.add_sheet("百度游戏TOP100", True)
    row0 = ['排行', '游戏名','类型', '下载量(万)','下载地址','md5']  # 第一行内容

    for i in range(len(row0)):
        sheet.write(0, i, row0[i])  # write(行，列，值)

    for page in range(10):
        targetUrl = "https://appc.baidu.com/uiserver?country=CN&pu=cuid%40_ivHaja22igHP2i50i28a_88vug_8vib_82r8j87S86ouviJ0uvViguAvt_NuviW_P2lfqqHB%2Ccut%40rpEcRk57xIlTaviqgI-DI_hlvh_DuLYwNpxhjfOuA%2Cctv%401%2Ccua%40_a-qiyaOvigBNE6lI5me6NI0-I_UCvh4SGNqA%2Cosname%40baiduappsearch%2Ccfrom%401009556z&language=zh&gms=false&disp=MIUI10_Builds_by_HitoLiu&cen=cuid_cut_cua_uid&operator=&network=WF&uid=_ivHaja22igHP2i50i28a_88vug_8vib_82r8j87S8qjuHivgavkigOW2igqu2fD3dcjC&psize=4&bdgid=eal52-_es5DHbNHw8lfhHRE4oL3v6maYT6d9n3SHPZ3lg&province=qivtkjihetggRHi86iS3kliheug_MHf3odfqA&cct=qivtkjihetggRHi86iS3kliheug_MHf3odfqA&board_id=" + str(
            boardId) + "&action=ranklist&from=1009556z&apn=" + str(
            page) + "&ndid=fbAzNdAKBr90F1qk8iAek-kQ2J2CtDD82aO2emX9Fti6fj9zNkKt_FMYY&ver=16795814&cll=ga24N_auvi_POei00a2YN_aTv8eH32e5B&platform_version_id=26&abi=armeabi-v7a&usertype=0&board_name=%E7%83%AD%E6%90%9C%E6%A6%9C&pkname=com.baidu.appsearch&is_support_webp=true&name=game_v8&native_api=1&crid=1536481806040&native_api=1&pn=" + str(
            page) + "&f=recommend%24%24%24homepage%40fixedentry%40ranklist%40%E7%83%AD%E6%90%9C%E6%A6%9C&bannert=26%4027%4028%4029%4030%4032%4043&apk_ver=16795814&ptl=hps"
        print(targetUrl)
        r = requests.get(targetUrl)
        originItem = r.json()
        middleArray = originItem['result']['data']
        resltArray = []
        for ii in range(len(middleArray)):
            if ii % 2 == 0:
                resltArray.append(middleArray[ii])
        innerFun(row0, resltArray, sheet, page)

    workbook.save(fileName)  # 保存workbook为xls格式


#
def innerFun(row0, pageArray, sheet, page):
    for clounmIndex in range(len(row0)):
        for rowIndex in range(len(pageArray)):
            per = pageArray[rowIndex]['itemdata']
            if clounmIndex == 0:
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, page * len(pageArray) + rowIndex + 1)
            if clounmIndex == 1:
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, per['sname'])
            if clounmIndex == 2:
                #re.compile(r'[1-9]\d*').findall(per['all_download_ori'])
                download=0
                """if bool(re.search('[万]',per['usenum_ori'])):
                    download =re.compile(r'[1-9]\d*').findall(per['usenum_ori'])
                if bool(re.search('[亿]',per['usenum_ori'])):
                    str =re.compile(r'[1-9]\d*').findall(per['usenum_ori'])
                    num =[]
                    for s in str:
                        num.append(s)
                    download = num*10000
                
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, per['usenum_ori'])"""
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, per['catename'])
            if clounmIndex == 3:
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, per['usenum_ori'])
            if clounmIndex == 4:
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, per['download_url'])
            if clounmIndex == 5:
                sheet.write(page * len(pageArray) + rowIndex + 1, clounmIndex, per['md5'])