#import scrapy_top100
from src import _360marketTop100, baiduSearch, yiguanSearch, talkingdataSearch, tengxunSearch, rank_liuyuwei

# baiduSearch.getSearchData('board_100_7003' , '游戏top100')
# yiguanSearch.yiguanSearchData('游戏','100','100')
# talkingdataSearch.talkingdataSearch('游戏top100','2018-07-01',100)
# tengxunSearch.TengXsearch('游戏top100',100)
# _360marketTop100._360marketSearch('游戏top100', 100)

rank_liuyuwei.doRank('游戏top100')