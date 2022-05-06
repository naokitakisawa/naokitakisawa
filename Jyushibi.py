#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
受死日にまつわる計算をするクラス。

import Jyushibi
cls = Jyushibi(2022)
dates = cls.dates
true_or_false = cls.is_jyushibi(’2022−05−06’)

ここで使用している関数は、GitHub の同じところに置いてあるはず。
import Jyuunishi
import SolarTerms24



受死日（じゅしび、じゅしにち）
受死日の意味や由来と読み方！2022年はいつ？
https://sk-imedia.com/27430

この受死日は「病を患えば必ず死ぬ最悪の大凶日」という扱いを受けており、一説には他の暦注を一切無視して凶日にしてしまうほどの力があると言われております。
この受死日は日の干支によってきまりますが、そのルールは正月（立春と雨水）だと戌の日、2月（啓蟄と春分、以下同じ法則）だと辰の日、3月だと亥の日、4月だと巳の日、5月だと子の日、6月だと午の日、7月だと丑の日、8月だと未の日、9月だと寅の日、10月だと申の日、11月だと卯の日、12月だと酉の日となっております。

@author: naokitakisawa
"""


import Jyuunishi
import SolarTerms24

class Jyushibi:
    def __init__(self, year):
        self._dates = []
        
        _eto = ['', '戌', '辰', '亥', '巳', '子', '午', '丑', '未', '寅', '申', '卯', '酉']
        
        #十二支と二十四節気を受け取り、該当する日を self._dates配列に格納する。
        def set_dates(eto_number, term_name):
            eto = _eto[eto_number]
            dates = SolarTerms24.dates_of(term_name, year)
            for date in dates:
                myEto = Jyuunishi.jyuunishi_of_date(date)
                if eto == myEto:
                    self._dates.append(date)

        set_dates(1, '立春')
        set_dates(1, '雨水')
        set_dates(2, '啓蟄')
        set_dates(2, '春分')
        set_dates(3, '清明')
        set_dates(3, '穀雨')
        set_dates(4, '立夏')
        set_dates(4, '小満')
        set_dates(5, '芒種')
        set_dates(5, '夏至')
        set_dates(6, '小暑')
        set_dates(6, '大暑')
        set_dates(7, '立秋')
        set_dates(7, '処暑')
        set_dates(8, '白露')
        set_dates(8, '秋分')
        set_dates(9, '寒露')
        set_dates(9, '霜降')
        set_dates(10, '立冬')
        set_dates(10, '小雪')
        set_dates(11, '大雪')
        set_dates(11, '冬至')
        set_dates(12, '小寒')
        set_dates(12, '大寒')
        
        self._dates.sort()


    
    def dates(self):
        return self._dates
    

    
    def is_jyushibi(self, date):
        return date in self._dates



if __name__ == '__main__':
    print('受死日（じゅしび、じゅしにち）を計算するクラス: cls = Jyushibi()')
    import datetime
    today = datetime.date.today()
    thisYear = today.year
    
    #コンストラクタ
    jyu = Jyushibi(thisYear)
    print()    
    
    
    
    # cls.dates() # 受死日配列を返す
    dates = jyu.dates()
    for date in dates:
        print(date)
    print()
    
    
    
    # true_or_false = cls.is_jyushibi(date) #dateが受死日に当たるとTrueで返す
    startDate = str(thisYear) + '-01-01'
    endDate = str(thisYear) + '-12-31'
    
    import pandas as pd
    date_index = pd.date_range(start=startDate, end=endDate, freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for a_date in date_ary.values:
        if jyu.is_jyushibi(a_date):
            print(a_date, '\t', '受死日')
        else:
            print('\t', a_date)
    
