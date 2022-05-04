#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
天赦日（てんしゃにち）
@author: naokitakisawa

dates = tensyanichi(2022)  #天赦日に該当するdate文字列が入った配列を返す
True_or_False = is_tensyanichi('2022-05-03')  #与えられたdate文字列が天赦日に当たるかの判定


こちらのページから計算式と説明を引用しました。ありがとうございます。
http://www.natubunko.net/charm/koyomi01.html
暦注（れきちゅう／日本のこよみに注意書きされる事項）の一種。
「てんしゃび」「天しゃ」とも呼ぶ。

天の生気が万物を養い、すべてを赦す（ゆるす）最良の日。
すべての暦注に優先し、他の日取りが悪くても一切障りない大吉日。
特に結婚には大吉。
１年に４～６日ある。

天赦日かどうかのチェックは次のページでチェックしました。
https://www.arachne.jp/onlinecalendar/taian/2022/
"""

import datetime

import Jyuunishi
import Jikkan
import SolarTerms24



def tensyanichi(year):
    
    def _dates_of_dates_jikkan_jyuunichi(_dates, jikkan, jyuunishi):
        dates = []
        
        for _date in _dates:
            _jikkan = Jikkan.jikkan_date(_date)
            _jyuunishi = Jyuunishi.jyuunishi_of_date(_date )
            if _jikkan == jikkan and _jyuunishi == jyuunishi:
                dates.append(_date)
        
        return dates
    
    
    
    
    
    
    
    dates = []
    
    
    
    dates = []
    
    _dates = []
    _dates += SolarTerms24.dates_of('立春', year)
    _dates += SolarTerms24.dates_of('雨水', year)
    _dates += SolarTerms24.dates_of('啓蟄', year)
    _dates += SolarTerms24.dates_of('春分', year)
    _dates += SolarTerms24.dates_of('清明', year)
    _dates += SolarTerms24.dates_of('穀雨', year)
    
    dates += _dates_of_dates_jikkan_jyuunichi(_dates, '戊', '寅')
    
    
    
    _dates = []
    
    _dates += SolarTerms24.dates_of('立夏', year)
    _dates += SolarTerms24.dates_of('小満', year)
    _dates += SolarTerms24.dates_of('芒種', year)
    _dates += SolarTerms24.dates_of('夏至', year)
    _dates += SolarTerms24.dates_of('小暑', year)
    _dates += SolarTerms24.dates_of('大暑', year)
    
    dates += _dates_of_dates_jikkan_jyuunichi(_dates, '甲', '午')
    
    
    
    _dates = []
    
    _dates += SolarTerms24.dates_of('立秋', year)
    _dates += SolarTerms24.dates_of('処暑', year)
    _dates += SolarTerms24.dates_of('白露', year)
    _dates += SolarTerms24.dates_of('秋分', year)
    _dates += SolarTerms24.dates_of('寒露', year)
    _dates += SolarTerms24.dates_of('霜降', year)
    
    dates += _dates_of_dates_jikkan_jyuunichi(_dates, '戊', '申')
    
    
    
    _dates = []
    
    _dates += SolarTerms24.dates_of('立冬', year)
    _dates += SolarTerms24.dates_of('小雪', year)
    _dates += SolarTerms24.dates_of('大雪', year)
    _dates += SolarTerms24.dates_of('冬至', year)
    _dates += SolarTerms24.dates_of('小寒', year)
    _dates += SolarTerms24.dates_of('大寒', year)
    
    dates += _dates_of_dates_jikkan_jyuunichi(_dates, '甲', '子')
    
    
    _tensyanichi_dates = sorted(dates)
    return _tensyanichi_dates







def is_tensyanichi(date):
    year = date.split('-')[0]
    
    dates = tensyanichi(year)
    
    if date in dates:
        return True
    
    return False









if __name__ == '__main__':
    print('天赦日（てんしゃにち、てんしゃび、てんしゃ）')
    
    today = datetime.date.today()
    thisYear = today.year
    
    
    print( 'dates = tensyanichi(', thisYear, ')  #天赦日に該当するdate文字列が入った配列を返す' )
    dates = tensyanichi(thisYear)
    for date in dates:
        print(date)
    print()
    
    
    
    print( "True_or_False = is_tensyanichi('{}')  #与えられたdate文字列が天赦日に当たるかの判定".format(today))
    import pandas as pd
    date_index = pd.date_range(start=str(thisYear) + '-01-01', end=str(thisYear) + '-12-31', freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for a_date in date_ary.values:
        true_or_false = is_tensyanichi(a_date)
        
        if true_or_false:
            print(a_date, '\t', true_or_false)
        else:
            print(a_date, '\t\t', true_or_false)
    print()
    