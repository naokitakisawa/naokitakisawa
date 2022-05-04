#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
旧暦から新暦に変換するクラス。計算が複雑なので、人の手を借り力業で辞書を作成しています。

cvrt = Convert_kyureki_to_shinreki(2020, 10)
shinreki = cvrt.shinreki_from('2022-05-04')


Kyurekiクラスはこちらから拝借しました。ありがとうございます。
新暦、旧暦変換 qreki.py
Copyright (C) fgshun 2009, 2017
https://github.com/fgshun/qreki_py
http://d.hatena.ne.jp/fgshun/

@author: naokitakisawa
"""


myDict = {}

class Convert_kyureki_to_shinreki:
    def __init__(self, startYear, deltaYear):
        global myDict
        
        from qreki import Kyureki
        import pandas as pd
        import re
        
        date_index = pd.date_range(start=str(startYear) + '-01-01', end=str(startYear + deltaYear) + '-12-31', freq="D")
        date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
        
        for shinreki in date_ary.values:
            y, m, d = [int(a) for a in shinreki.split('-')]
    
            kyureki_obj = Kyureki.from_ymd(y, m, d)
            kyureki_kanji = str(kyureki_obj)
    
            ary = [int(a) for a in re.split('[年月日閏]', kyureki_kanji) if a != '']
            kyureki = '{:04d}-{:02d}-{:02d}'.format( ary[0], ary[1], ary[2] )
    
            myDict[kyureki] = shinreki
            
            
            

    def shinreki_from_kyuureki(self, kyuureki):
        return myDict[kyuureki]
    
    
if __name__ == '__main__':
    print('旧暦から新暦に変換するクラス')
    cvrt = Convert_kyureki_to_shinreki(2022, 0)
    shinreki = cvrt.shinreki_from_kyuureki('2022-05-04')
    print( shinreki )
    


