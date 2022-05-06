#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
十二直（じゅうにちょく）、別名中段（ちゅうだん）を計算するクラス　（メソッド一つしかないのでほぼ関数かな）
Jyuunityoku.py

import Jyuunityoku
j = Jyuunityoku()
十二直 = j.jyuunityoku('2022-05-06')

建（たつ）
除（のぞく）
満（みつ）
平（たいら）
定（さだん）
執（とる）
破（やぶる）
危（あやぶ）
成（なる）
納（おさん）
開（ひらく）
閉（とづ）
たのみたさと、やあ、なおひと。

宝くじ的に
縁起が良いのは、満、成
縁起が悪いのは、執、危
のようです。


計算は力業で行っています。数式で計算するよりメンテしやすいかなと思って。


計算方法はこちらのページから拝借しました。
http://koyomi.vis.ne.jp/sub/rekicyuu_doc01.htm


あとこちらのページにあるスクリプトを参考にさせて頂きました。ありがとうございます。
Rubyで暦注（六曜,九星,干支,中段,宿）を出力
https://bias.hateblo.jp/entry/20090906


正しく計算できているか確認するのに、次のサイトを利用させて頂きました。ありがとうございます。
https://koyomishokunin.com/12choku_2022/
https://shinto-bukkyo.net/koyomi/十二直/


@author: naokitakisawa
"""

import SolarTerms24
import Jyuunishi

DEBUG_MODE = False


class Jyuunityoku:
    def __init__(self, year):
        JYUUNITYOKU = [
            '建',
            '除',
            '満',
            '平',
            '定',
            '執',
            '破',
            '危',
            '成',
            '納',
            '開',
            '閉',
            ]
        
        
        self._dict = dict()

        current_jyuunityoku_number = 99
        
        
        
        dates = SolarTerms24.dates_of('大雪', year - 1)
        for date in dates:
            
            eto = Jyuunishi.jyuunishi_of_date(date)
            if eto == '子':
                if DEBUG_MODE: print('子 found\t', date, '\t===============')
                current_jyuunityoku_number = 0
            if current_jyuunityoku_number == 99:
                continue
            
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = current_jyuunityoku_number % 12 + 1
        


        
        dates = SolarTerms24.dates_of('冬至', year - 1)
        for date in dates:
                
            #1月分はスキップ
            month = date.split('-')[1]
            if month == "01":
                continue
            
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12


        
        dates = SolarTerms24.dates_of('冬至', year)
        for date in dates:
                
            #12月分はスキップ
            month = date.split('-')[1]
            if month == "12":
                continue
            
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
        
        
        
        
  
        
  
    
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('小寒', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 


        dates = SolarTerms24.dates_of('大寒', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
    
 
    
 
    
 
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立春', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
        dates = SolarTerms24.dates_of('雨水', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
    
 
    
 
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('啓蟄', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            

        dates = SolarTerms24.dates_of('春分', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12 
    
 
    
 
    
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('清明', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
        dates = SolarTerms24.dates_of('穀雨', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12 
    
    
    
    
    
 
    
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立夏', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('小満', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12     
 






        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('芒種', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('夏至', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    








        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('小暑', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('大暑', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    







        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立秋', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('処暑', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    




        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('白露', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('秋分', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    




        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('寒露', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
        
        dates = SolarTerms24.dates_of('霜降', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    





        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立冬', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('小雪', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    





        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('大雪', year)
        for date in dates:
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('冬至', year)
        for date in dates:
            #1月分はスキップ
            month = date.split('-')[1]
            if month == "01":
                continue
            
            self._dict[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12   






    def jyuunityoku(self, date):
        return self._dict[date]







if __name__ == '__main__':
    # コンストラクタ
    import datetime
    thisYear = datetime.date.today().year
    j = Jyuunityoku(thisYear)
    
    
    # jyuunityoku(date) # 十二直を得る
    startDate = str(thisYear) + '-01-01'
    endDate = str(thisYear) + '-12-31'
    
    import pandas as pd
    date_index = pd.date_range(start=startDate, end=endDate, freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for date in date_ary.values:
        jyuuni = j.jyuunityoku(date)
        print(date, '\t', jyuuni)
    
    
    