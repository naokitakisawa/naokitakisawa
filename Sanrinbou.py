#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
三隣亡（さんりんぼう）
Sanrinbou.py

s = Snarinbou(2022)
_bool = s.is_sanrinbou(date)


こちらのページから計算方式と意味を頂きました。ありがとうございます。
掲載暦注とその説明　（その２）
http://koyomi8.com/sub/rekicyuu_doc02.htm
三隣亡とは、現在は建築に関しての忌日とされている暦注。
一・四・七・十月	亥（い）の日
二・五・八・十一月	寅（とら）の日
三・六・九・十二月	午（うま）の日
ただし古い暦注には三隣亡ではなく「三輪宝」と書いてあり、家を建てるにはよい日となっている。暦注の転記ミスから「吉日」が「凶日」に転じてしまったものでは無いかとも考えられる。
あまり気にしてもはじまらない。


こちらのページにあるカレンダーでチェックしました。ありがとうございます。
三隣亡とは？2022年はいつ？してはいけないことは？
https://nihon-nenchugyoji.com/sanrinbou/

@author: naokitakisawa
"""

import SolarTerms24
import Jyuunishi

class Sanrinbou:
    def __init__(self, year):
        self.dict_date_sanrinou = {}
        
        dates = []
        
        # 一・四・七・十月	亥（い）の日
        dates += SolarTerms24.dates_of('立春', year)
        dates += SolarTerms24.dates_of('雨水', year)
        
        dates += SolarTerms24.dates_of('立夏', year)
        dates += SolarTerms24.dates_of('小満', year)
        
        dates += SolarTerms24.dates_of('立秋', year)
        dates += SolarTerms24.dates_of('処暑', year)
        
        dates += SolarTerms24.dates_of('立冬', year)
        dates += SolarTerms24.dates_of('小雪', year)
        
        for date in dates:
            jyuunishi = Jyuunishi.jyuunishi_of_date( date )
            if jyuunishi == '亥':
                self.dict_date_sanrinou[ date ] = True
        
        
        
        # 二・五・八・十一月	寅（とら）の日
        dates = []
        dates += SolarTerms24.dates_of('啓蟄', year)
        dates += SolarTerms24.dates_of('春分', year)
        
        dates += SolarTerms24.dates_of('芒種', year)
        dates += SolarTerms24.dates_of('夏至', year)
        
        dates += SolarTerms24.dates_of('白露', year)
        dates += SolarTerms24.dates_of('秋分', year)
        
        dates += SolarTerms24.dates_of('大雪', year)
        dates += SolarTerms24.dates_of('冬至', year)
        
        for date in dates:
            jyuunishi = Jyuunishi.jyuunishi_of_date( date )
            if jyuunishi == '寅':
                self.dict_date_sanrinou[ date ] = True
        
        
        
        # 三・六・九・十二月	午（うま）の日
        dates = []
        dates += SolarTerms24.dates_of('清明', year)
        dates += SolarTerms24.dates_of('穀雨', year)
        
        dates += SolarTerms24.dates_of('小暑', year)
        dates += SolarTerms24.dates_of('大暑', year)
        
        dates += SolarTerms24.dates_of('寒露', year)
        dates += SolarTerms24.dates_of('霜降', year)
        
        dates += SolarTerms24.dates_of('小寒', year)
        dates += SolarTerms24.dates_of('大寒', year)
        
        
        for date in dates:
            jyuunishi = Jyuunishi.jyuunishi_of_date( date )
            if jyuunishi == '午':
                self.dict_date_sanrinou[ date ] = True
        



    def is_sanrinbou(self, date):
        return date in self.dict_date_sanrinou

        








if __name__ == '__main__':
    print('三隣亡(さんりんぼう)とは、現在は建築に関しての忌日とされている暦注。')
    print()
    
    # コンストラクタ
    import datetime
    thisYear = datetime.datetime.today().year
    s = Sanrinbou(thisYear)
    
    
    
    
    
    # is_sanrinbou(date)
    startDate = str(thisYear) + '-01-01'
    endDate = str(thisYear) + '-12-31'
    
    import pandas as pd
    date_index = pd.date_range(start=startDate, end=endDate, freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for date in date_ary.values:
        _bool = s.is_sanrinbou(date)
        if _bool:
            print( date, "\t三隣亡" )
        else:
            print( date )
        
        
        
        
        
        
        
        
        