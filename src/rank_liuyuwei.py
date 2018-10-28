import os

import xlrd
import xlwt
from src.cons.constant import ValueName


class Game:
    name = ''
    downloadUrl = ''
    downloadCount = -1
    file_md5 = ''

    def __init__(self, name, downloadUrl, downloadCount , file_md5) -> None:
        self.name = name
        self.downloadCount = downloadCount
        self.downloadUrl = downloadUrl
        self.file_md5 = file_md5

def doRank(filename ):
    fullName = filename + ".xls"
    if os.path.exists(fullName):
        workbook = xlrd.open_workbook(fullName)
        for sheetName in workbook.sheet_names():
            xl_sheet = workbook.sheet_by_name(sheetName)
            handleSheetData(xl_sheet)

def handleSheetData(xl_sheet):
    cloumName = []
    for index in range(xl_sheet.nrows):
        if index == 0:
            continue
        rowData = xl_sheet.row_values(index)
        cloumIndex = getCloumnIndex(ValueName.name, xl_sheet)


def getCloumnIndex(colomnName , xl_sheet):
    cloumnRow = xl_sheet.row(0)
    for index in range(len(cloumnRow)):
        if colomnName == cloumnRow[index].value:
            return index

