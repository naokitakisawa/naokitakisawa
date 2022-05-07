#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
八専（はっせん）

import Hassen
_bool = is_hassen(date)


八専（はっせん）とは、選日の一つ。
Wikipedia
https://ja.wikipedia.org/wiki/八専
八専のうち間日を除く8日間は同気が重なる（比和）ことから吉はますます吉となり、凶はますます凶となるとされた。


八専とは？2022年はいつ？してはいけないことは？
https://nihon-nenchugyoji.com/hassen/
同気が重なると、物事が片寄る「凶日」であることから、以下のようなことをしてはいけない、見合わせたほうが良いとされています。

昔は軍事上の忌日でしたが、針灸や柱を建てることも不吉となりました。

法事（仏事や供養など）
破壊的な仕事の着手（ビルの取り壊しなど）
婚礼（入籍・結婚式など）
針灸
柱を建てる（土木関係）


計算結果のチェックはこちらのページと照らし合わせました。ありがとうございます。
2022年八専一覧（月別カレンダー）
https://nihon-nenchugyoji.com/hassen/


@author: naokitakisawa
"""

import Jikkan
import Jyuunishi


def is_hassen(date):
    HASSEN = [
        '壬子',  
        '甲寅', 
        '乙卯', 
        '丁巳', 
        '己未', 
        '庚申', 
        '辛酉', 
        '癸亥', ]
    
    jika = Jikkan.jikkan_date(date)
    jyuu = Jyuunishi.jyuunishi_of_date(date)
    kanshi = jika + jyuu
    
    return kanshi in HASSEN




if __name__ == '__main__':
    print('八専（はっせん）。八専のうち間日を除く8日間は同気が重なる（比和）ことから吉はますます吉となり、凶はますます凶となるとされた。')
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
        _bool = is_hassen(date)
        if _bool:
            print( date, "\t八専" )
        else:
            print( date )
    