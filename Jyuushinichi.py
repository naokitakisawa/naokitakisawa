#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
十死日（じゅうしにち、じゅうしび）かどうかを返す関数。
Jyuushinichi.py
bool = is_jyuushinichi('2022-05-07')


計算方法はこちらのページから頂きました。ありがとうございます。
掲載暦注とその説明　（その３）・・・下段について
十死、十死一生日、天殺日などとも言う。受死日に次ぐ大悪日。何事にも悪い日とされ、葬式にも凶。選日法は、節月と日の十二支による。
正月・四月・七月・十月は、	酉の日
二月・五月・八月・十一月、　巳の日
三月・六月・九月・十二月、　丑の日
（正月は立春から始まる）
http://koyomi8.com/sub/rekicyuu_doc03.htm


https://sk-imedia.com/27438
十死日（じゅうしにち）は昔のカレンダーに「十し」と記載されていた、凶日です。受死日に次いでの凶日という扱いをされており「十死一生日という大悪日」という意味があります。
この計算方法は間違いのようだ→十死日は1月だと戌の日、2月だと辰の日、3月だと亥の日、4月だと巳の日、5月だと子の日、6月だと午の日、7月だと丑の日、8月だと未の日、9月だと寅の日、10月だと申の日、11月だと卯の日、12月だと酉の日が該当するのです。


正しく計算できているが、次のページのカレンダーで答え合わせしました。
https://2996.info/kaiun/360/
http://koyomi8.com/directjp.cgi?http://koyomi8.com/sub/rekicyuu.htm
http://koyomi8.com/sub/rekicyuu.htm?20150327
https://jpnculture.net/jushinichi-juushinichi/

@author: naokitakisawa
"""





import SolarTerms24
import Jyuunishi




def is_jyuushinichi(date):
    term_name = SolarTerms24.term_of_date(date)
    jyuunishi = Jyuunishi.jyuunishi_of_date(date)
    
    
        
    if term_name == '小寒' or term_name == '大寒':
        wrong_jyuunishi = '丑'
        if jyuunishi == wrong_jyuunishi: return True
    
    
    elif term_name == '立春' or term_name == '雨水':
        wrong_jyuunishi = '酉'
        if jyuunishi == wrong_jyuunishi: return True
    
    elif term_name == '啓蟄' or term_name == '春分':
        wrong_jyuunishi = '巳'
        if jyuunishi == wrong_jyuunishi: return True
    
    
    elif term_name == '清明' or term_name == '穀雨':
        wrong_jyuunishi = '丑'
        if jyuunishi == wrong_jyuunishi: return True
    
    
    elif term_name == '立夏' or term_name == '小満':
        wrong_jyuunishi = '酉'
        if jyuunishi == wrong_jyuunishi: return True
        
    
    elif term_name == '芒種' or term_name == '夏至':
        wrong_jyuunishi = '巳'
        if jyuunishi == wrong_jyuunishi: return True
        
    
    elif term_name == '小暑' or term_name == '大暑':
        wrong_jyuunishi = '丑'
        if jyuunishi == wrong_jyuunishi: return True
    
    
    elif term_name == '立秋' or term_name == '処暑':
        wrong_jyuunishi = '酉'
        if jyuunishi == wrong_jyuunishi: return True
    
    
    elif term_name == '白露' or term_name == '秋分':
        wrong_jyuunishi = '巳'
        if jyuunishi == wrong_jyuunishi: return True
        
    
    elif term_name == '寒露' or term_name == '霜降':
        wrong_jyuunishi = '丑'
        if jyuunishi == wrong_jyuunishi: return True
        
    
    elif term_name == '立冬' or term_name == '小雪':
        wrong_jyuunishi = '酉'
        if jyuunishi == wrong_jyuunishi: return True
    
    
    elif term_name == '大雪' or term_name == '冬至':
        wrong_jyuunishi = '巳'
        if jyuunishi == wrong_jyuunishi: return True
    
    

    return False
        
    

if __name__ == '__main__':
    print('十死日（じゅうしにち）かどうかを返す関数。')
    print( "_bool = is_jyuushinichi('2022-05-07')")
    print()
    
    import datetime
    
    thisYear = datetime.datetime.today().year
    # thisYear = 2021
    
    startDate = str(thisYear) + '-01-01'
    endDate = str(thisYear) + '-12-31'
    import pandas as pd
    date_index = pd.date_range(start=startDate, end=endDate, freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    for date in date_ary.values:
        jyu = is_jyuushinichi(date)
        if jyu:
            print( date, "\t十死日")
        else:
            print( date)
    
    
    
    