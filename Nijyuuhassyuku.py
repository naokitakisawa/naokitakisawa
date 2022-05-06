#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二十八宿（にじゅうはっしゅく）を返す関数: jyu = nijyuuhassyukubi(date)

import nijyuuhassyukubi from Nijyuuhassyuku
jyu = nijyuuhassyukubi(date)



http://www.takarakuji-get.com/koyomi.html
二十八宿は月が２７～２８日で全天をを一周する恒星月に基づくもので
古くはこれによって天体の位置を示した。
日本では当初二十七宿（牛宿を除く）を用いていましたが
貞享暦(１６８４年)以後は中国流の二十八宿が採用されるようになりました。

https://www.calc-site.com/calendars/twenty_eight_mansion
検算用のカレンダーはここから頂きました。ありがとうございます。


https://meigen.keiziban-jp.com/manabi/okane/sikyuku/
鬼宿日の2022年版のカレンダー



@author: naokitakisawa
"""

from datetime import datetime
import pandas as pd

def nijyuuhassyuku_number(date):
    dt1 = datetime(1902, 1, 23) #角の日、計算の起点
    
    y, m, d = [int(a) for a in date.split('-')]
    dt2 = datetime(y, m, d)
    
    dt3 = dt2 - dt1
    days = dt3.days

    number = days % 28
    return number


def nijyuuhassyukubi(date):
    nijyuu = [
        '角',
        '亢',
        '氏',
        '房',
        '心',
        '尾 ',
        '箕',
        '斗',
        '牛',
        '女',
        '虚',
        '危',
        '室',
        '壁',
        '奎',
        '婁',
        '胃',
        '昴',
        '畢',
        '觜',
        '参',
        '井',
        '鬼',
        '柳',
        '星',
        '張',
        '翼',
        '軫',
        ]
    
    number = nijyuuhassyuku_number(date)
    return nijyuu[number]



    # def is_kisyukubi(date):
    #     _bool = True
    #     return _bool


if __name__ == '__main__':
    print('二十八宿（にじゅうはっしゅく）を返す関数: jyu = nijyuuhassyukubi(date)')
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")
    jyu = nijyuuhassyukubi(date)
    print( today )
    print( jyu )
    print()
    
    
    print('今年の二十八宿カレンダー' ) 
    date_index = pd.date_range(start=str(today.year) + '-01-01', end=str(today.year) + '-12-31', freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for _date in date_ary.values:
        # print( type(_date) )
        jyu = nijyuuhassyukubi(_date)
        print( _date, '\t', jyu)
    print()
    
    year = today.year
    
    
