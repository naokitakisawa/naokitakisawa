#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
solarTerms(yyyy)  #yyyy年の二十四節気について、名前と日にちと配列で得る。 ===='
date_of(term_name, yyyy)  #yyyy年のterm_name節気に該当する、日にちを得る。 ====
dates_of(term_name,yyyy)  #yyyy年のterm_name節気の中にある日付のリストを返す。 ====
term_of_date(date)  # dateがどの節気に入っているのか返す。 ====



免責事項:このスクリプトで得られたデータについて、私、作者は責任を持ちません。
1年は春分の日から始めるそうですが、そうすると計算が面倒、いえ私の用途から外れるので対応していません。

このスクリプトで使用した計算式は、次のページから頂きました。ありがとうございます。
二十四節気の略算式
http://addinbox.sakura.ne.jp/sekki24_topic.htm
2099年まで有効だそうです。無効になるほど長生きしたいです。
'''

import datetime
from datetime import timedelta

data = [
        {'name':'小寒', 'month':1, 'd':6.3811, 'a':0.242778, 'deltaYear':-1}, 
        {'name':'大寒', 'month':1, 'd':21.1046, 'a':0.242765, 'deltaYear':-1}, 
        {'name':'立春', 'month':2, 'd':4.8693, 'a':0.242713, 'deltaYear':-1}, 
        {'name':'雨水', 'month':2, 'd':19.7062, 'a':0.242627, 'deltaYear':-1}, 
        {'name':'啓蟄', 'month':3, 'd':6.3968, 'a':0.242512, 'deltaYear':0}, 
        {'name':'春分', 'month':3, 'd':21.4471, 'a':0.242377, 'deltaYear':0}, 
        {'name':'清明', 'month':4, 'd':5.6280, 'a':0.242231, 'deltaYear':0}, 
        {'name':'穀雨', 'month':4, 'd':20.9375, 'a':0.242083, 'deltaYear':0}, 
        {'name':'立夏', 'month':5, 'd':6.3771 , 'a':0.241945, 'deltaYear':0}, 
        {'name':'小満', 'month':5, 'd':21.9300, 'a':0.241825, 'deltaYear':0}, 
        {'name':'芒種', 'month':6, 'd':6.5733, 'a':0.241731, 'deltaYear':0}, 
        {'name':'夏至', 'month':6, 'd':22.2747, 'a':0.241669, 'deltaYear':1}, 
        {'name':'小暑', 'month':7, 'd':8.0091, 'a':0.241642, 'deltaYear':0}, 
        {'name':'大暑', 'month':7, 'd':23.7317, 'a':0.241654, 'deltaYear':0}, 
        {'name':'立秋', 'month':8, 'd':8.4102, 'a':0.241703, 'deltaYear':0}, 
        {'name':'処暑', 'month':8, 'd':24.0125, 'a':0.241786, 'deltaYear':0}, 
        {'name':'白露', 'month':9, 'd':8.5186, 'a':0.241898, 'deltaYear':0}, 
        {'name':'秋分', 'month':9, 'd':23.8896, 'a':0.242032, 'deltaYear':0}, 
        {'name':'寒露', 'month':10, 'd':9.1414, 'a':0.242179 , 'deltaYear':0}, 
        {'name':'霜降', 'month':10, 'd':24.2487, 'a':0.242328, 'deltaYear':0}, 
        {'name':'立冬', 'month':11, 'd':8.2396, 'a':0.242469 , 'deltaYear':0}, 
        {'name':'小雪', 'month':11, 'd':23.1189, 'a':0.242592, 'deltaYear':0}, 
        {'name':'大雪', 'month':12, 'd':7.9152, 'a':0.242689, 'deltaYear':0}, 
        {'name':'冬至', 'month':12, 'd':22.6587, 'a':0.242752, 'deltaYear':0}, 
        ]




def _formatted_date(yyyy, mm, dd):
    return "{0:04d}-{1:02d}-{2:02d}".format(yyyy,mm,dd)





def solarTerm_and_date(yyyy, season):
    name = season['name']
    month = season['month']
    d = season['d']
    a = season['a']
    deltaYear = season['deltaYear']
    day = int(d + (a * (yyyy + deltaYear - 1900 )) - int((yyyy + deltaYear - 1900) / 4))
    formatted = _formatted_date(yyyy, month, day)
    return [name, formatted]





def solarTerms(yyyy):
    terms = []
    
    for datum in data:
        name = datum['name']
        month = datum['month']
        d = datum['d']
        a = datum['a']
        deltaYear = datum['deltaYear']
        
        day = int(d + (a * (yyyy + deltaYear - 1900 )) - int((yyyy + deltaYear - 1900) / 4))
        date = _formatted_date(yyyy, month, day)
        terms.append([name, date])
    
    return terms






def date_of(term_name, yyyy, ):
    if type(yyyy) is str:
        yyyy = int(yyyy)
    
    terms = solarTerms(yyyy)
    for term in terms:
        _name, _date = term
        if _name == term_name:
            return _date
    return 'ERROR_NO_DATE'





def _term_names():
    return [datum['name'] for datum in data] 




def dates_of(term_name, in_year):
    
    from_date = ''
    to_date = ''
    index = 0
    
    for i in range(len(data)):
        datum = data[i]
        a_name = datum['name']
        if a_name != term_name:
            continue
        
        index = i
        break
    
    datum = data[index]
    
    dates = []
    
    if index == 0:
        from_date = date_of(term_name, in_year)
        
        a_datum = data[index+1]
        to_date = date_of(a_datum['name'], in_year)
        
    elif index == 23:
        last_date = date_of('小寒', in_year)
        
        end = datetime.datetime.strptime(last_date, '%Y-%m-%d')
        start = datetime.datetime.strptime( str(in_year) + '-01-01', '%Y-%m-%d')

        for i in range((end - start).days):
            d = start + timedelta(i)
            date = d.strftime("%Y-%m-%d")
            dates.append(date)
        
        from_date = date_of(term_name, in_year)
        to_date = str(in_year) + '-12-31'
        
        
    else:
        from_date = date_of(term_name, in_year)
        to_date = '9999-01-23'
        
        a_datum = data[index+1]
        to_date = date_of(a_datum['name'], in_year)

    
    
    start = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    
    for i in range((end - start).days):
        d = start + timedelta(i)
        date = d.strftime("%Y-%m-%d")
        dates.append(date)
    
    
    if index == 23:
        from_date = ''
        to_date = ''
        index = 0
        
        for i in range(len(data)):
            datum = data[i]
            a_name = datum['name']
            if a_name != term_name:
                continue
            
            index = i
            break
        
        datum = data[index]
        
        
        dates.append(str(in_year) + '-12-31')
        
    
    return dates






date_term_dict = {}

def term_of_date(date):
    thisYear = date.split('-')[0]
    
    if len(date_term_dict) == 0:
        for a_term in _term_names():
            for a_date in dates_of(a_term,thisYear):
                date_term_dict[a_date] = a_term
    
    return date_term_dict[date]






if __name__ == '__main__':
    term_names = _term_names()

    print( '二十四節気：')
    print( term_names )
    print( len( term_names ), '節気' )
    print()
    
    
    
    today = datetime.date.today()
    thisYear = today.year
    
    
    
    print('solarTerms(yyyy)  #yyyy年の二十四節気について、名前と日にちと配列で得る。 ====') 
    terms = solarTerms(thisYear)
    for term in terms:
        name, date = term
        print(name, '\t', date)
    print()
        


    print('date_of(term_name, yyyy)  #yyyy年のname節気に該当する、日にちを得る。 ====')
    for name in _term_names():
        aDate = date_of(name, thisYear)
        print(name, '\t', aDate)
    print()
    
    
    
    print('dates_of(term_name,in_year)  #in_year年のname節気にある日付のリストを返す。 ====')
    for a_term in term_names:
        print( a_term )
        dates = dates_of(a_term,thisYear)
        for a_date in dates:
            print('\t', a_date)
        print()
    print()
    
    
    
    print('term_of_date(date)  # dateがどの節気に入っているのか返す。')
    import pandas as pd
    date_index = pd.date_range(start=str(thisYear) + '-01-01', end=str(thisYear) + '-12-31', freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    for a_date in date_ary.values:
        # print( a_date )
        a_term = term_of_date(a_date)
        print( a_date, '\t', a_term)
    print()
    