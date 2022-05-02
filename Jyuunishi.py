#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime, timedelta


jyuunishis = '子丑寅卯辰巳午未申酉戌亥'

def _jyuunishi_number(yyyy):
    return (yyyy - 4) % 12

def jyuunishi(yyyy):
    number = _jyuunishi_number(yyyy)
    # print( jyuunishi[number] )
    return jyuunishis[number]
    
def eto_year(yyyy):
    return jyuunishi(yyyy)






def _jyuunishi_number_ofDate(date):
    dt1 = datetime(1900, 1, 3)
    
    y, m, d = date.split('-')
    dt2 = datetime(int(y), int(m), int(d))
    
    dt3 = dt2 - dt1
    days = dt3.days

    number = days % 12
    return number



def jyuunishi_ofDate(date):
    number = _jyuunishi_number_ofDate(date)
    return jyuunishis[number]





import pandas as pd

def dates_forJyuunishi_startDate_endDate(Jyuunishi, startDate, endDate):
    date_index = pd.date_range(start=startDate, end=endDate, freq="D")
    date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")
    
    dates = list()
    for date in date_ary:
        jyuunishi_name = jyuunishi_ofDate(date)
        # print(Jyuunishi,'\t', jyuunishi_name)
        if jyuunishi_name == Jyuunishi:
            dates.append(date)
            # print(date)

    return dates







if __name__ == '__main__':
    print('十二支（じゅうにし）：子丑寅卯辰巳午未申酉戌亥')
    
    print( '2022年の十二支は、', jyuunishi(2022) )
    print( '2022-05-02の十二支は、', jyuunishi_ofDate('2022-05-02') )
    dates = dates_forJyuunishi_startDate_endDate('子', '2022-05-1', '2022-06-30')
    print('2022-05-1 から 2022-06-30 までで子の日は、')
    for date in dates:
        print('\t', date)
    print()
    
    
    
    
    # jyuunishi(year)
    for year in range(2010, 2030):
        print(year, '\t', jyuunishi(year))
    print()


    
    # jyuunishi_ofDate(date)
    today = datetime.today()
    for delta in range(-10, 20):
        day = today + timedelta(days=delta)
        date = datetime.strftime(day, '%Y-%m-%d')
        print(date, '\t', jyuunishi_ofDate(date))
    print()
    


    # dates_forJyuunishi_startDate_endDate(eto, startDate, endDate)
    thisYear = str(today.year)
    thisMonth = str(today.month)
    startDate = '-'.join([thisYear, thisMonth, '1'])
    endDate = '-'.join([thisYear, thisMonth, '28'])
    
    for eto in jyuunishis:
        print(eto)
        dates = dates_forJyuunishi_startDate_endDate(eto, startDate, endDate)
        for date in dates:
            print('\t', date)
        print()
    print()



