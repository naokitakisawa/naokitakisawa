#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
甲子（かっし,かし,こうし,きのえね）かどうか判定する python 関数

import Kasshi
_bool = Kasshi.is_kasshi(date)


掲載暦注とその説明　（その２）
http://koyomi8.com/sub/rekicyuu_doc02.htm
六十干支の最初。五行説でも「木水」の組み合わせで相生。このため目出度い日とされ、この日に祭り（甲子祭）をするなどの風習があった


こちらのカレンダーでチェックしました。
https://www.taian-calendar.com/year-kinoenenohi/kinoenenohi-2022.html


@author: naokitakisawa
"""

import Jikkan
import Jyuunishi

def is_kasshi(date):
    jika = Jikkan.jikkan_date(date)
    jyuu = Jyuunishi.jyuunishi_of_date(date)
    kanshi = jika + jyuu
    
    return kanshi == '甲子'



if __name__ == '__main__':
    print('甲子（かっし,かし,こうし,きのえね）六十干支の最初。五行説でも「木水」の組み合わせで相生。このため目出度い日とされ、この日に祭り（甲子祭）をするなどの風習があった。')
    print()
    
    
    # is_hassen(date)
    import datetime
    thisYear = datetime.datetime.today().year
    startDate = str(thisYear) + '-01-01'
    endDate = str(thisYear) + '-12-31'
    
    import pandas as pd
    date_index = pd.date_range(start=startDate, end=endDate, freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for date in date_ary.values:
        _bool = is_kasshi(date)
        if _bool:
            print( date, '\t甲子')
        else:
            print( date )