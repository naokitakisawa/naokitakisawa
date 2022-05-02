#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime, timedelta


jikkans = '甲乙丙丁戊己庚辛壬癸'



def jikkan_number(year):
    return (year - 4) % 10
    
    
def jikkan(year):
    number = jikkan_number(year) 
    return jikkans[number]





def jikkan_number_date(date):
    
    y, m, d = date.split('-')
    dt = datetime(int(y), int(m), int(d) )
    dt0 = datetime(1900, 1, 1)
    
    dt3 = dt - dt0
    days = dt3.days

    number = days % 10
    return number


def jikkan_date(date):
    number = jikkan_number_date(date)
    return jikkans[number]





if __name__ == '__main__':
    print('十干（じっかん） 甲乙丙丁戊己庚辛壬癸')
    print( '2022年の十干は、', jikkan(2022) )
    print( '2022-05-02 の十干は', jikkan_date('2022-05-02') )
    print()
    
    
    # jikkan(year)
    for year in range(2020, 2030):
        print(year, '\t', jikkan(year) )
    print()
    
    
    
    # jikkan_date(date
    today = datetime.today()
    
    for delta in range(-10, 20):
        day = today + timedelta(days=delta)
        date = datetime.strftime(day, '%Y-%m-%d')
        print(date, '\t', jikkan_date(date) )
    print()
    





