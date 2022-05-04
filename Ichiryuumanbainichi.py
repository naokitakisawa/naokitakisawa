#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
一粒万倍日（いちりゅうまんばいにち）にまつわる python 関数

dates = ichiryuumanbainichi(2022)  #一粒万倍日に該当するdate文字列が入った配列を返す
True_or_False = is_ichiryuumanbainichi('2022-05-03')  #与えられたdate文字列が一粒万倍日に当たるかの判定


importしている 十二支を計算するJyuunishi と 二十四節気のSolarTerms24 も私が作りました。GitHubの同じところに置いてあります。

一粒万倍日の計算式は次のページから得ました。ありがとうございました。
http://www.natubunko.net/charm/koyomi02.html

合っているかどうかは次のページのカレンダーで確認しました。ありがとうございました。
https://www.arachne.jp/onlinecalendar/taian/2022/
'''


import Jyuunishi
import SolarTerms24



def ichiryuumanbainichi(year):
    
    def _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2):
        dates = []
        
        for a_date in _dates:
            jyuunishi = Jyuunishi.jyuunishi_of_date(a_date)
            
            if jyuunishi == jyuunishi1 or jyuunishi == jyuunishi2:
                dates.append(a_date)
                
        return dates
        
    
    result = []

    _dates = SolarTerms24.dates_of('小寒', year) + SolarTerms24.dates_of('大寒', year)
    jyuunishi1 = '卯'
    jyuunishi2 = '子'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)
    

    _dates = SolarTerms24.dates_of('立春', year) + SolarTerms24.dates_of('雨水', year)
    jyuunishi1 = '丑'
    jyuunishi2 = '午'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)
            
            
    _dates = SolarTerms24.dates_of('啓蟄', year) + SolarTerms24.dates_of('春分', year)
    jyuunishi1 = '酉'
    jyuunishi2 = '寅'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2) 


    _dates = SolarTerms24.dates_of('清明', year) + SolarTerms24.dates_of('穀雨', year)
    jyuunishi1 = '子'
    jyuunishi2 = '卯'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('立夏', year) + SolarTerms24.dates_of('小満', year)
    jyuunishi1 = '卯'
    jyuunishi2 = '辰'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('芒種', year) + SolarTerms24.dates_of('夏至', year)
    jyuunishi1 = '巳'
    jyuunishi2 = '午'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('小暑', year) + SolarTerms24.dates_of('大暑', year)
    jyuunishi1 = '酉'
    jyuunishi2 = '午'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('立秋', year) + SolarTerms24.dates_of('処暑', year)
    jyuunishi1 = '子'
    jyuunishi2 = '未'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('白露', year) + SolarTerms24.dates_of('秋分', year)
    jyuunishi1 = '卯'
    jyuunishi2 = '申'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('寒露', year) + SolarTerms24.dates_of('霜降', year)
    jyuunishi1 = '酉'
    jyuunishi2 = '午'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('立冬', year) + SolarTerms24.dates_of('小雪', year)
    jyuunishi1 = '酉'
    jyuunishi2 = '戌'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)         
    
    
    
    _dates = SolarTerms24.dates_of('大雪', year) + SolarTerms24.dates_of('冬至', year)
    jyuunishi1 = '亥'
    jyuunishi2 = '子'
    result += _dates_jyuunishi1_jyuunishi2(_dates, jyuunishi1, jyuunishi2)  
    
    
    return result





is_ichiryuumanbainichi_dict = {}

def is_ichiryuumanbainichi(date):
    year = date.split('-')[0]
    
    if len(is_ichiryuumanbainichi_dict) == 0:
        a_dict = {date:True for date in ichiryuumanbainichi( year )}
    
    if date in a_dict:
        return True
    
    return False








if __name__ == '__main__':
    print( '一粒万倍日（いちりゅうまんばいにち）' )
    print()
    
    import datetime
    today = datetime.date.today()
    thisYear = today.year
    
    
    
    print( 'dates = ichiryuumanbainichi(', thisYear, ')  #一粒万倍日に該当するdate文字列が入った配列を返す' )
    
    for a_date in ichiryuumanbainichi( thisYear ):
        print( a_date )
    print()




    print( "True_or_False = is_chiryuumanbainichi('{}')  #与えられたdate文字列が一粒万倍日に当たるかの判定".format(today.strftime("%Y-%m-%d")) )
    import pandas as pd
    date_index = pd.date_range(start=str(thisYear) + '-01-01', end=str(thisYear) + '-12-31', freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for a_date in date_ary.values:
        true_or_false = is_ichiryuumanbainichi(a_date)
        print(a_date, '\t', true_or_false)
    print()