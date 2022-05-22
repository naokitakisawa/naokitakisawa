#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
各種暦注を返すdatetime.dateオブジェクトの子クラス

from rekityuu import rekityuu


初期化(datetime.dateオブジェクトから継承）
obj = rekityuu(2022, 5, 8)
obj = rekityuu.fromisoformat('2022-05-08')
obj = rekityuu.fromordinal(100000)
obj = rekityuu.today()


プロパティ
string = obj.曜日     # youbi
string = obj.六曜     # rokuyou
string = obj.旧暦     # kyuureki
string = obj.十干     # jikkan
string = obj.十二支   # jyuunishi
string = obj.十二直        # jyuunichoku
string = obj.二十八宿       # nijyuuhassyuku
string = obj.二十四節気     # sekki


メソッド
new_obj = obj.advance()   #一日進んだ date オブジェクトを返す
new_obj = obj.back()   #一日戻った date オブジェクトを返す

true_or_false = obj.不成就日ですか()      # is_fujyoujyunichi()
rue_or_false = obj.受死日ですか()        # is_jyushibi()
rue_or_false = obj.十死日ですか()         # is_jyuushinichi()
true_or_false = obj.三隣亡ですか()       # is_sanrinbou()
true_or_false = obj.八専ですか()         # is_hassen()
true_or_false = obj.十方暮ですか()        # is_jippoukure()
true_or_false = obj.一粒万倍日ですか()    # is_ichiryuumandainichi()
true_or_false = obj.天赦日ですか ()       # is_tenshanichi()
true_or_false = obj.寅の日ですか()        # is_toranohi()
true_or_false = obj.己の日ですか()        # is_minohi()
true_or_false = obj.己巳の日ですか()      # is_tuchinotominohi()
true_or_false = obj.大明日ですか()       # is_daimyouichi()
true_or_false = obj.甲子ですか()         # is_kasshi()
true_or_false = obj.節分ですか()         # is_setsubun()
true_or_false = obj.彼岸ですか()         # is_higan()
true_or_false = obj.土用ですか()         # is_doyou()
true_or_false = obj.社日ですか()         # is_syanichi()
true_or_false = obj.八十八夜ですか()     # is_hachijyuuhachiya()
true_or_false = obj.二百十日ですか()     # is_nihyakutouka()
true_or_false = obj.二百二十日ですか()    # is_nihyakuhatsuka()
true_or_false = obj.大土ですか()         # is_ooduti()
true_or_false = obj.小土ですか()         # is_koduti()
true_or_false = obj.三伏ですか()         # is_sanpuku()
true_or_false = obj.庚申ですか()         # is_koushin()
true_or_false = obj.臘日ですか()         # is_roujitsu()


ユーティリティ
dates_string_list = obj.dates_in_year(year)   #オブジェクトの日にちを含む年に含まれる日にち文字列を返すユーティリティ
dates_string_list = obj.dates_in_month(month, year)   #オブジェクトの日にちを含む月に含まれる日にち文字列を返す
shinreki_string = obj.convert_kyuureki_to_shinreki(kyuureki_string) #旧暦から新暦を得る




@author: naokitakisawa
"""

import datetime
import re
from qreki import Kyureki # https://github.com/fgshun/qreki_py
import SolarTerms24   # このコードと同じとこに置いてあると思います。



class rekityuu(datetime.date):
    @classmethod
    def __init__(self, year,month,day):
        self.__dates_in_the_month = []
        self.__dates_in_the_year = []
        self.__jyuunichoku_from_date = {}
        self.__kyuureki = ''

 
    
    # a = k.advance()   一日進んだ date オブジェクトを返す
    def advance(self):
        delta = datetime.timedelta(days=1)
        new = self + delta
        return new

    
    # a = k.back()   一日戻った date オブジェクトを返す
    def back(self):
        delta = datetime.timedelta(days=1)
        new = self - delta
        return new









    # オブジェクトの日にちを含む年に含まれる日にち文字列を返すユーティリティ
    def dates_in_year(year):
        dates = []
        
        # if year is str:
        #     year = int(year)
        
        # print( type(year) )
        # print( year )
        
        startDate = rekityuu( 2022, 1, 1)
        i = 0
        
        while True:
            delta = datetime.timedelta(days=i)
            nowDate = startDate + delta

            if nowDate.year != year:
                break

            dates.append( str(nowDate) )            
            i += 1

#### TODO: ここ書き換えられる

        return dates

    


    # オブジェクトの日にちを含む月に含まれる日にち文字列を返すユーティリティ
    def dates_in_month(month, year):
        dates = []
        
        if year is str:
            month, year = [int(a) for a in (month, year)]
        
        startDate = datetime.date(year, month, 1)
        i = 0
        
        while True:
            delta = datetime.timedelta(days=i)
            nowDate = startDate + delta

            if nowDate.month != month:
                break

            dates.append( str(nowDate) )            
            i += 1

        return dates
















    
    # 曜日
    @property
    def 曜日(self):
        return self.youbi

    @property
    def youbi(self):
        YOUBI = '月火水木金土日'
        return YOUBI[self.weekday()]



    # 六曜
    @property
    def 六曜(self):
        return self.rokuyou
    
    @property
    def rokuyou(self):
        kyureki_obj = Kyureki.from_ymd(self.year, self.month, self.day)
        return kyureki_obj.rokuyou
        
        



    # 旧暦から新暦へ変換
    @classmethod
    def convert_kyuureki_to_shinreki(self, kyuureki_date_string):
        kyuureki_obj = rekityuu.fromisoformat(kyuureki_date_string)
        # print( kyuureki_obj )
        
        d = rekityuu(kyuureki_obj.year, 1,25)
        end_date = rekityuu(kyuureki_obj.year + 1, 2,20)
        
        kyuureki_to_shinreki = {}
        
        # print("旧暦\t\t新暦")
        while True:
            # print(d)
            
            k = Kyureki.from_ymd(d.year, d.month, d.day)
            k_kanji = str(k)
            
            kyureki = ''
            if '閏' not in k_kanji:
                ary = [int(a) for a in re.split('[年月日]', k_kanji) if a != '']
                kyureki = '{:04d}-{:02d}-{:02d}'.format( ary[0], ary[1], ary[2] )
            else :
                ary = [a for a in re.split('[年月日閏]', k_kanji) if a != '']
                kyureki = '{:04d}-閏{:02s}-{:02d}'.format( ary[0], ary[1], ary[2] )
            
            # print( kyureki )
            
            # print("{}\t{}".format(kyureki, d))
            
            kyuureki_to_shinreki[kyureki] = str(d)
            
            if d == end_date:
                break
            d = d.advance()
        
        
        return kyuureki_to_shinreki[kyuureki_date_string]




    # 旧暦文字列
    @property
    def 旧暦(self):
        return self.kyuureki
    
    @property
    def kyuureki(self):
        if self.__kyuureki:
            return self.__kyuureki
        
        import re
        kyureki_obj = Kyureki.from_ymd(self.year, self.month, self.day)
        kyureki_kanji = str(kyureki_obj)
        
        kyureki_kanji.replace('正', '01')
        kyureki_kanji.replace('朔の', '01')
        kyureki_kanji.replace('朔', '01')
        
        # print(kyureki_kanji)
        
        ary =  [int(a) for a in re.split('[年月日閏]', kyureki_kanji) if a != '']
        
        # return rekityuu(ary[0], ary[1], ary[2])
        return '{:04d}-{:02d}-{:02d}'.format( ary[0], ary[1], ary[2] )



        
        
        


    # 十干(甲乙丙丁戊己庚辛壬癸）
    @property
    def 十干(self):
        return self.jikkan
    
    @property
    def jikkan(self):
        JIKKAN = '甲乙丙丁戊己庚辛壬癸'
        number = (self.toordinal() + 4) % 10
        return JIKKAN[number]





    # 十二支（じゅうにし、えと）'子丑寅卯辰巳午未申酉戌亥'
    @property
    def 十二支(self):
        return self.jyuunishi
    
    @property
    def jyuunishi(self):
        JYUUNISHI = '子丑寅卯辰巳午未申酉戌亥'
        number = (self.toordinal()  + 2) % 12
        return JYUUNISHI[number]




    # 十二直
    @property
    def 十二直(self):
        return self.jyuunichoku
    
    @property
    def jyuunichoku(self):
        IS_DEBUG_MODE = False
        
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
        
        if len(self.__jyuunichoku_from_date):
            return self.__jyuunichoku_from_date[ str(self) ]
        
        
        
        current_jyuunityoku_number = 99
        

        dates = SolarTerms24.dates_of('大雪', self.year - 1)
        for date in dates:
            eto = rekityuu.fromisoformat(date).jyuunishi
            if eto == '子':
                if IS_DEBUG_MODE: print('子 found\t', date, '\t===============')
                current_jyuunityoku_number = 0
                
            if current_jyuunityoku_number == 99:
                continue
            
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12


        dates = SolarTerms24.dates_of('冬至', self.year - 1)
        for date in dates:
                
            #1月分はスキップ
            month = date.split('-')[1]
            if month == "01":
                continue

            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12


        dates = SolarTerms24.dates_of('冬至', self.year)
        for date in dates:
                
            #12月分はスキップ
            month = date.split('-')[1]
            if month == "12":
                continue
            
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
        


        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('小寒', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 


        dates = SolarTerms24.dates_of('大寒', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
  
    
 
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立春', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
        dates = SolarTerms24.dates_of('雨水', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
    
 
    
 
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('啓蟄', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            

        dates = SolarTerms24.dates_of('春分', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12 
 
    
 
    
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('清明', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
        dates = SolarTerms24.dates_of('穀雨', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12 
    
 

    
        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立夏', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('小満', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12     
 


        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('芒種', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('夏至', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    



        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('小暑', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('大暑', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    




        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立秋', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('処暑', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    




        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('白露', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('秋分', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    




        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('寒露', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
        
 
        dates = SolarTerms24.dates_of('霜降', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    



        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('立冬', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('小雪', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12    



        current_jyuunityoku_number -= 1
        dates = SolarTerms24.dates_of('大雪', self.year)
        for date in dates:
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12
 
            
 
        dates = SolarTerms24.dates_of('冬至', self.year)
        for date in dates:
            #1月分はスキップ
            month = date.split('-')[1]
            if month == "01":
                continue
            
            self.__jyuunichoku_from_date[date] = JYUUNITYOKU[current_jyuunityoku_number]
            if IS_DEBUG_MODE: print( date, '\t', JYUUNITYOKU[current_jyuunityoku_number] )
            current_jyuunityoku_number = (current_jyuunityoku_number + 1) % 12   


        return self.__jyuunichoku_from_date[ str(self) ]





    # 二十八宿
    @property
    def 二十八宿(self):
        return self.nijyuuhassyuku

    @property
    def nijyuuhassyuku(self):
        NIJYUUHASSYUKU = [
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
        
        number = (self.toordinal() + 24) % 28
        return NIJYUUHASSYUKU[number]






    # 不成就日
    def 不成就日ですか(self):
        return self.is_fujyoujyunichi()
    
    def is_fujyoujyunichi(self):
        qreki = self.kyuureki
        _, month, day = [int(a) for a in qreki.split('-')]
        
        if month == 1 or month == 7:
            if day in [3, 11, 19, 27]: return True
            else: return False
        
        if month == 2 or month == 8:
            if day in [2, 10, 28, 26]: return True
            else: return False
        
        if month == 3 or month == 9:
            if day in [1, 9, 17, 25]: return True
            else: return False
        
        if month == 4 or month == 10:
            if day in [4, 12, 20, 28]: return True
            else: return False
        
        if month == 5 or month == 11:
            if day in [5, 13, 21, 29]: return True
            else: return False
        
        if month == 6 or month == 12:
            if day in [6, 14, 22, 30]: return True
            else: return False 
            








    # 受死日
    def 受死日ですか(self):
        return self.is_jyushibi
    
    def is_jyushibi(self):
        _dates = []
        
        _eto = ['', '戌', '辰', '亥', '巳', '子', '午', '丑', '未', '寅', '申', '卯', '酉']
        
        #十二支と二十四節気を受け取り、該当する日を self._dates配列に格納する。
        def set_dates(eto_number, term_name):
            eto = _eto[eto_number]
            dates = SolarTerms24.dates_of(term_name, self.year)
            
            for date in dates:
                k = rekityuu.fromisoformat(date)
                if eto == k.jyuunishi:
                    _dates.append(date)

        set_dates(1, '立春')
        set_dates(1, '雨水')
        set_dates(2, '啓蟄')
        set_dates(2, '春分')
        set_dates(3, '清明')
        set_dates(3, '穀雨')
        set_dates(4, '立夏')
        set_dates(4, '小満')
        set_dates(5, '芒種')
        set_dates(5, '夏至')
        set_dates(6, '小暑')
        set_dates(6, '大暑')
        set_dates(7, '立秋')
        set_dates(7, '処暑')
        set_dates(8, '白露')
        set_dates(8, '秋分')
        set_dates(9, '寒露')
        set_dates(9, '霜降')
        set_dates(10, '立冬')
        set_dates(10, '小雪')
        set_dates(11, '大雪')
        set_dates(11, '冬至')
        set_dates(12, '小寒')
        set_dates(12, '大寒')

        return str(self) in _dates




    # 十死日
    def 十死日ですか(self):
        return self.is_jyuushinichi()
    
    def is_jyuushinichi(self):
        term_name = SolarTerms24.term_of_date( str(self) )
        jyuunishi = self.jyuunishi
    

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



    # 二十四節気
    @property
    def 二十四節気(self):
        return self.sekki
    
    @property
    def sekki(self):
        return SolarTerms24.term_of_date(date)



    # 三隣亡
    def 三隣亡ですか(self):
        return self.is_sanrinbou()
    
    def is_sanrinbou(self):
        term = self.sekki
        
        # 一・四・七・十月	亥（い）の日
        if term in ['立春', '雨水', '立夏', '小満', '立秋', '処暑', '立冬', '小雪']:
            if k.jyuunishi == '亥':
                return True
            else:
                return False


        # # 二・五・八・十一月	寅（とら）の日
        if term in ['啓蟄', '春分', '芒種', '夏至', '白露', '秋分', '大雪', '冬至', ]:
            if k.jyuunishi == '寅':
                return True
            else:
                return False


        # # 三・六・九・十二月	午（うま）の日
        if term in ['清明', '穀雨', '小暑', '小暑', '大暑', '寒露', '霜降', '小寒', '大寒', ]:
            if k.jyuunishi == '午':
                return True
            else:
                return False      




    # 八専
    def 八専ですか(self):
        return self.is_hassen()
    
    def is_hassen(self):
        HASSEN = [
            '壬子',  
            '甲寅', 
            '乙卯', 
            '丁巳', 
            '己未', 
            '庚申', 
            '辛酉', 
            '癸亥', ]
            
        jika = self.jikkan
        jyuu = self.jyuunishi
        kanshi = jika + jyuu
            
        return kanshi in HASSEN




    # 十方暮
    def 十方暮ですか(self):
        return self.is_jippoukure()
    
    def is_jippoukure(self):
        JIPPOUKURE = [
            '甲申', 
            '乙酉', 
            '丙戌', 
            '丁亥', 
            '戊子', 
            '己丑', 
            '庚寅', 
            '辛卯', 
            '壬辰', 
            '癸巳', ]
        
        jika = self.jikkan
        jyuu = self.jyuunishi
        kanshi = jika + jyuu
        
        return kanshi in JIPPOUKURE




    # 天赦日
    def 天赦日ですか(self):
        return self.is_tenshanichi()
    
    def is_tenshanichi(self):
        term = SolarTerms24.term_of_date( str(self) )

        if term in ['立春', '雨水', '啓蟄', '春分', '清明', '穀雨']:
            jikkan = self.jikkan
            jyuunishi = self.jyuunishi
            
            if jikkan + jyuunishi == '戊寅':
                return True
            else: return False

    
        if term in ['立夏', '小満', '芒種', '夏至', '小暑', '大暑', ]:
            jikkan = self.jikkan
            jyuunishi = self.jyuunishi
            
            if jikkan + jyuunishi == '甲午':
                return True
            else: return False



        if term in ['立秋', '処暑', '白露', '秋分', '寒露', '霜降']:
            jikkan = self.jikkan
            jyuunishi = self.jyuunishi
            
            if jikkan + jyuunishi == '戊申':
                return True
            else: return False    



        if term in ['立冬', '小雪', '大雪', '冬至', '小寒', '大寒']:
            jikkan = self.jikkan
            jyuunishi = self.jyuunishi
            
            if jikkan + jyuunishi == '甲子':
                return True
            else: return False 






    # 一粒万倍日
    def 一粒万倍日ですか(self):
        return self.is_ichiryuumandainichi()
    
    def is_ichiryuumandainichi(self):
        term = SolarTerms24.term_of_date( str(self) )
        
        if term == '小寒' or term == '大寒':
            if self.jyuunishi == '卯' or self.jyuunishi == '子':
                return True
            else: return False
        

        if term == '立春' or term == '雨水':
            if self.jyuunishi == '丑' or self.jyuunishi == '午':
                return True
            else: return False
            
            
        if term == '啓蟄' or term == '春分':
            if self.jyuunishi == '酉' or self.jyuunishi == '寅':
                return True
            else: return False
            

        if term == '清明' or term == '穀雨':
            if self.jyuunishi == '子' or self.jyuunishi == '卯':
                return True
            else: return False
            
        
        if term == '立夏' or term == '小満':
            if self.jyuunishi == '卯' or self.jyuunishi == '辰':
                return True
            else: return False
            

        if term == '芒種' or term == '夏至':
            if self.jyuunishi == '巳' or self.jyuunishi == '午':
                return True
            else: return False
            

        if term == '小暑' or term == '大暑':
            if self.jyuunishi == '酉' or self.jyuunishi == '午':
                return True
            else: return False
            

     
        if term == '立秋' or term == '処暑':
            if self.jyuunishi == '子' or self.jyuunishi == '未':
                return True
            else: return False
            
        

        if term == '白露' or term == '秋分':
            if self.jyuunishi == '卯' or self.jyuunishi == '申':
                return True
            else: return False
            
        

     
        if term == '寒露' or term == '霜降':
            if self.jyuunishi == '酉' or self.jyuunishi == '午':
                return True
            else: return False
            
        


        if term == '立冬' or term == '小雪':
            if self.jyuunishi == '酉' or self.jyuunishi == '戌':
                return True
            else: return False
            
        
     
        if term == '大雪' or term == '冬至':
            if self.jyuunishi == '亥' or self.jyuunishi == '子':
                return True
            else: return False
            


    # 寅の日
    def 寅の日ですか(self):
        return self.is_toranohi()
    
    def is_toranohi(self):
        return self.jyuunishi == '寅'




    # 己の日
    def 己の日ですか(self):
        return self.is_minohi()
    
    def is_minohi(self):
        return self.jyuunishi == '巳'



    # 己巳の日
    def 己巳の日ですか(self):
        return self.is_tuchinotominohi()
    
    def is_tuchinotominohi(self):
        return self.jikkan == '己' and self.jyuunishi == '巳'



    # 大明日
    def 大明日ですか(self):
        return self.is_daimyouichi()
    
    def is_daimyouichi(self):
        DAIMYOUNICHI = [
            '戊午', 
            '己巳', 
            '庚午', 
            '辛未', 
            '壬申', 
            '癸酉', 
            '丁丑', 
            '己卯', 
            '壬午', 
            '甲申', 
            '丁亥', 
            '壬辰', 
            '乙未', 
            '壬寅', 
            '甲辰', 
            '乙巳', 
            '丙午', 
            '丁未', 
            '己酉', 
            '庚戌', 
            '辛亥', 
            '丙辰', 
            '己未', 
            '庚申', 
            '辛酉', 
            ]
        
        kanshi = self.jikkan + self.jyuunishi
        return kanshi in DAIMYOUNICHI




    # 甲子
    def 甲子ですか(self):
        return self.is_kasshi()

    def is_kasshi(self):
        kanshi = self.jikkan + self.jyuunishi
        return kanshi == '甲子'



    # 節分
    def 節分ですか(self):
        return self.is_setsubun()
    
    def is_setsubun(self):
        setsubun_data = SolarTerms24.節分(self.year)
        # print(setsubun_data)
        
        for a_setsubun in setsubun_data:
            term, date = a_setsubun
            if date == str(self):
                return True
        
        return False




    # 彼岸
    def 彼岸ですか(self):
        return self.is_higan()

    def is_higan(self):
        term = SolarTerms24.term_of_date( str(self) )
        if term != '春分' or term != '秋分':
            return False
        
        dates = []
                
        date_string = SolarTerms24.date_of('春分', self.year)
        r = rekityuu.fromisoformat(date_string)
        one_day_ago = r.back()
        two_days_ago = r.back().back()
        three_days_ago = r.back().back().back()
        one_day_after = r.advance()
        two_days_after = r.advance().advance()
        three_days_after = r.advance().advance().advance()
        
        dates += [str(a) for a in [three_days_ago, two_days_ago, one_day_ago, r, one_day_after, two_days_after, three_days_after] ]


        date_string = SolarTerms24.date_of('秋分', self.year)
        r = rekityuu.fromisoformat(date_string)
        one_day_ago = r.back()
        two_days_ago = r.back().back()
        three_days_ago = r.back().back().back()
        one_day_after = r.advance()
        two_days_after = r.advance().advance()
        three_days_after = r.advance().advance().advance()
        
        dates += [str(a) for a in [three_days_ago, two_days_ago, one_day_ago, r, one_day_after, two_days_after, three_days_after] ]

        return str(self) in dates





    def 土用ですか(self):
        return self.is_doyou()
    
    def doyou(self):
        result = []
        doyou_seen = {}
        
        
        
        d = rekityuu.fromisoformat( SolarTerms24.date_of('立春', self.year))
        dates = []
        for _ in range(18):
            d = d.back()
            dates.append(d)
        
        dates.sort()
        
        for d in dates:
            if d.jyuunishi == '丑' and '冬土用 丑の日' not in doyou_seen:
                doyou_seen['冬土用 丑の日'] = True
                result.append( [str(d), '冬土用 丑の日'] )
            else:
                result.append( [str(d), '冬土用'] )
                
                
                
        d = rekityuu.fromisoformat( SolarTerms24.date_of('立夏', self.year))
        dates = []
        for _ in range(18):
            d = d.back()
            dates.append(d)
        
        dates.sort()
        
        for d in dates:
            if d.jyuunishi == '丑' and '春土用 丑の日' not in doyou_seen:
                doyou_seen['春土用 丑の日'] = True
                result.append( [str(d), '春土用 丑の日'] )
            else:
                result.append( [str(d), '春土用'] )



        d = rekityuu.fromisoformat( SolarTerms24.date_of('立秋', self.year))
        dates = []
        for _ in range(18):
            d = d.back()
            dates.append(d)
        
        dates.sort()
        
        for d in dates:
            if d.jyuunishi == '丑' and '夏土用 丑の日' not in doyou_seen:
                doyou_seen['夏土用 丑の日'] = True
                result.append( [str(d), '夏土用 丑の日'] )
            else:
                result.append( [str(d), '夏土用'] )



        d = rekityuu.fromisoformat( SolarTerms24.date_of('立冬', self.year))
        dates = []
        for _ in range(18):
            d = d.back()
            dates.append(d)
        
        dates.sort()
        
        for d in dates:
            if d.jyuunishi == '丑' and '秋土用 丑の日' not in doyou_seen:
                doyou_seen['秋土用 丑の日'] = True
                result.append( [str(d), '秋土用 丑の日'] )
            else:
                result.append( [str(d), '秋土用'] )

        return result
    
    
    


    def is_doyou(self):
        
        result = self.doyou()
        
        for a_result in result:
            date, doyou = a_result
            if str(self) == date:
                return doyou
            
        return ''







    def 社日ですか(self):
        return self.is_syanichi()
    
    def is_syanichi(self):


        syunbun = rekityuu.fromisoformat( SolarTerms24.date_of('春分', ｓelf.year) )
        backward = syunbun.back()
        forward = syunbun.advance()
        
        theDays = []
        
        while True:
            if backward.jikkan == '戊':
                theDays.append( str(backward) )
                break
            if forward.jikkan == '戊':
                theDays.append( str(forward) )
                break
            backward = backward.back()
            forward = forward.back()
        

        
        syuubun = rekityuu.fromisoformat( SolarTerms24.date_of('秋分', ｓelf.year) )
        backward = syuubun.back()
        forward = syuubun.advance()

        while True:
            if backward.jikkan == '戊':
                theDays.append( str(backward) )
                break
            if forward.jikkan == '戊':
                theDays.append( str(forward) )
                break
            backward = backward.back()
            forward = forward.back()


        return str(self) in theDays








    def 八十八夜ですか(self):
        return self.is_hachijyuuhachiya()


    def _hachijyuuhachiya(self):
        rissyun = self.fromisoformat( SolarTerms24.date_of('立春', self.year) )
        delta = datetime.timedelta(days=87)
        hachijyuuhachiya = rissyun + delta
        return str(hachijyuuhachiya)

    
    def is_hachijyuuhachiya(self):
        return str(self) == self._hachijyuuhachiya()








    # 二百十日
    def 二百十日ですか(self):
            return self.is_nihyakutouka()

            
    def nihyakutouka(self):
        rissyun = self.fromisoformat( SolarTerms24.date_of('立春', self.year) )
        delta = datetime.timedelta(days=209)
        date_nihyakutouka = rissyun + delta
        return str(date_nihyakutouka)      
    
    def is_nihyakutouka(self):
        return str(self) == self.nihyakutouka()
    



    # 二百二十日
    def 二百二十日ですか(self):
            return self.is_nihyakuhatsuka()

            
    def nihyakuhatsuka(self):
        rissyun = self.fromisoformat( SolarTerms24.date_of('立春', self.year) )
        delta = datetime.timedelta(days=219)
        date_nihyakutouka = rissyun + delta
        return str(date_nihyakutouka)      
    
    def is_nihyakuhatsuka(self):
        return str(self) == self.nihyakuhatsuka()




    def 大土ですか(self):
        return self.is_ooduti()
    
    def is_ooduti(self):
        OODUTI = ['庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥', '丙子']
        kanshi = self.jikkan + self.jyuunishi
        return kanshi in OODUTI





    def 小土ですか(self):
        return self.is_koduti()
    
    def is_koduti(self):
        KODUTI = ['戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申']
        kanshi = self.jikkan + self.jyuunishi
        return kanshi in KODUTI





    def 三伏ですか(self):
        return self.is_sanpuku()

    def sanpuku(self):
        dates = []
        seen_counter = 0
        
        date = rekityuu.fromisoformat( SolarTerms24.date_of('夏至', self.year) )
        while True:
            if date.jikkan == '庚':
                seen_counter += 1
                
                if seen_counter == 3:
                    dates.append( str(date) )
                elif seen_counter == 4:
                    dates.append( str(date) )
                    break
            date = date.advance()

            
            
        date = rekityuu.fromisoformat( SolarTerms24.date_of('立秋', self.year) )
        while True:      
            if date.jikkan == '庚':
                dates.append( str(date) )
                break
            date = date.advance()
        
        return dates
 
       

    def is_sanpuku(self):
        dates = self.sanpuku()
        
        return str(self) in dates






    def 庚申ですか(self):
        return self.is_koushin()


    def is_koushin(self):
        kashi = self.jikkan + self.jyuunishi
        if kashi == '庚申':
            return True
        else:
            return False






    def 臘日ですか(self): #（ろうじつ）
        return self.is_roujitsu()
    
    def roujitsu(self):
        dates = []
        
        d = rekityuu.fromisoformat( SolarTerms24.date_of('小寒', self.year) )
        seen_couner = 0
        while True:
            # print('While1')
            if d.jyuunishi == '辰':
                seen_couner += 1
                if seen_couner == 2:
                    dates.append( str(d) )
                    break
            d = d.advance()


        d = rekityuu.fromisoformat( SolarTerms24.date_of('大寒', self.year) )
        if d.jyuunishi == '辰':
            date.append( str(d) )
        else:
            backword_d = d.back()
            forward_d = d.advance()
            while True:
                # print('While2')
                # print(backword_d.jyuunishi)
                # print(forward_d.jyuunishi)
                if backword_d.jyuunishi == '辰':
                    # print(backword_d.jyuunishi)
                    dates.append( str(backword_d) )
                    break
                if forward_d.jyuunishi == '辰':
                    # print(forward_d.jyuunishi)
                    dates.append( str(forward_d) )
                    break
                backword_d = backword_d.back()
                forward_d = forward_d.advance()


        d = rekityuu.fromisoformat( SolarTerms24.date_of('大寒', self.year) )
        while True:
            if d.jyuunishi == '戌':
                dates.append( str(d) )
                break
            d = d.advance()
        
        
        # k = rekityuu(self.year, 12, 9).kyuureki
        # dates.append( k )
        #convert_kyuureki_to_shinreki
        
        
        kyuureki_string = "{:04d}-{:02d}-{:02d}".format(self.year - 1, 12, 9)
        # print( kyuureki_string )
        
        shinreki_string = self.convert_kyuureki_to_shinreki(kyuureki_string)
        # print(shinreki_string )
        
        dates.append(shinreki_string)
        
        
        return dates
    



    def is_roujitsu(self):
        dates = self.roujitsu()
        # print( dates )
        return str(self) in dates




















if __name__ == '__main__':
    IS_TEST_MODE = False
    
    
    if IS_TEST_MODE:
        print('イニシャライザ r = rekityuu(2022, 5, 8)')
        r = rekityuu(2022, 5, 8)
        print( r )
        print()
        print()



    if IS_TEST_MODE:
        print("イニシャライザ　r = rekityuu.fromisoformat('2022-05-08')")
        r = rekityuu.fromisoformat('2022-05-08')
        print( r )
        print()
        print()



    if IS_TEST_MODE:
        print('イニシャライザ　r = rekityuu.today()')
        r = rekityuu.today()
        print( r )
        print()
        print()



    if IS_TEST_MODE:
        print('イニシャライザ　r = rekityuu.fromordinal(1_000_000)')
        r = rekityuu.fromordinal(1_000_000)
        print( r )
        print()
        print()



    if IS_TEST_MODE: # advance(), back()
        print('l = k.advance() #一日進んだオブジェクトを返す')
        print('l = k.back() #一日戻ったオブジェクトを返す')
        k = rekityuu.today()
        for _ in range(60):
            k = k.advance()
            print(k)
        print()
        
        for _ in range(60):
            k = k.back()
            print(k)
        print()
        print()






    if IS_TEST_MODE:
        print('曜日')
        t = rekityuu.today()
        for date in rekityuu.dates_in_month(t.month, t.year):
            k = rekityuu.fromisoformat(date)
            print( "{}\t{}".format( k,  k.曜日))

        print()
        print()
        

    if False:
        r = '2022-05-13'
        shinreki = rekityuu.convert_kyuureki_to_shinreki(r)

    
    if False:
        print('旧暦から新暦へ変換')
        print('旧暦 ->\t新暦')
        t = rekityuu.today()
        
        for kyuureki in rekityuu.dates_in_year(t.year):
            d = rekityuu.fromisoformat(kyuureki)
            shinreki = d.convert_kyuureki_to_shinreki(str(d))

            # print( "旧暦：{}\t新暦：{}".format( kyuureki,  shinreki))
            print( kyuureki, '\t', shinreki )
        print() 
        print()







    if IS_TEST_MODE:
        print('旧暦')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            print( "旧暦：{}\t新暦：{}".format( k.旧暦,  k))
        print() 
        print()



    if IS_TEST_MODE:
        print('二十四節： どの二十四節気に入っているか')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            print( "{}\t{}".format( k,  k.二十四節気))
        print() 
        print()



    if IS_TEST_MODE:
        print('六曜')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_month(t.month, t.year):
            k = rekityuu.fromisoformat(date)
            print( "{}\t{}".format( k,  k.六曜))
        
        print() 
        print()        
        
        
        
    if IS_TEST_MODE:
        print('jikkan 十干、 jyuunishi 十二支')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_month(t.month, t.year):
            k = rekityuu.fromisoformat(date)
            print( "{}\t{},\t{}".format( k,  k.十干, k.十二支))
        print()
        print()

        


    if IS_TEST_MODE:
        print('十二直')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_month(t.month, t.year):
            k = rekityuu.fromisoformat(date)
            print( "{}\t{}".format( k,  k.十二直))
            print( "{}\t{}".format( k,  k.十二直))
        print() 
        print()       



    if IS_TEST_MODE:
        print('二十八宿')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_month(t.month, t.year):
            k = rekityuu.fromisoformat(date)
            print( "{}\t{}".format( k,  k.二十八宿))
        
        print() 
        print()  
        
    


    if IS_TEST_MODE:
        print('不成就日ですか')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.不成就日ですか():
                print( "{}\t{}".format( k,  '不成就日') )
            else:
                print( date )
        print() 
        print()  



    # 受死日
    if IS_TEST_MODE:
        print('is_jyushibi()、受死日ですか')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.受死日ですか():
                print( "{}\t{}".format( k,  '受死日') )
            else:
                print( date )
        print() 
        print()  
        
    
    # 十死日
    if IS_TEST_MODE:
        print('is_jyuushinichi(), 十死日')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.十死日ですか():
                print( "{} -> {}".format( k,  '十死日') )
            else:
                print( date )
        print() 
        print()
    


    # 三隣亡
    if IS_TEST_MODE:
        print('is_sanrinbou() 三隣亡')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.三隣亡ですか():
                print( "{}\t{}".format( k,  '三隣亡') )
            else:
                print( date )
        print() 
        print()



    # 八専
    if IS_TEST_MODE:
        print('is_hassen() 八専のうち間日を除く8日間は同気が重なる（比和）ことから吉はますます吉となり、凶はますます凶となるとされた。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.八専ですか():
                print( "{}\t{}".format( k,  '八専') )
            else:
                print( date )
        print() 
        print()


    # 十方暮
    if IS_TEST_MODE:
        print('is_jippoukure() 十方暮（じっぽうくれ）。この期間は、天地の気が相剋して、万事うまく行かない凶日とされている。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.十方暮ですか():
                print( "{}\t{}".format( k,  '十方暮') )
            else:
                print( date )
        print() 
        print()



    # 天赦日（てんしゃにち）
    if IS_TEST_MODE:
        print('is_tenshanichi() 天赦日は天の生気が万物を養い、すべてを赦す（ゆるす）最良の日。すべての暦注に優先し、他の日取りが悪くても一切障りない大吉日。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.天赦日ですか():
                print( "{}\t{}".format( k,  '天赦日') )
            else:
                print( date )
        print() 
        print()




    # 一粒万倍日
    if IS_TEST_MODE:
        print('is_ichiryuumandainichi() 一粒万倍日は「何かを始めるのに最適な日」とされ、宝くじを買うなどお金に関連することによい日とされている。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.一粒万倍日ですか():
                print( "{}\t{}".format( k,  '一粒万倍日') )
            else:
                print( date )
        print() 
        print()


    # 寅の日
    if IS_TEST_MODE:
        print('is_toranohi() 寅の日は吉日の中で最も金運に縁の有る日とされている。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.寅の日ですか():
                print( "{}\t{}".format( k,  '寅の日') )
            else:
                print( date )
        print() 
        print()    



    # 巳の日
    if IS_TEST_MODE:
        print('is_minohi() 巳の日は吉日の中で最も金運に縁の有る日とされている。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.己の日ですか():
                print( "{}\t{}".format( k,  '巳の日') )
            else:
                print( date )
        print() 
        print()
        
        
        
    # 己巳の日
    if IS_TEST_MODE:
        print('is_tuchinotominohi() 60日に1度巡ってくる「己巳の日（つちのとみのひ）」は、巳の日の中でもさらに縁起がよい日とされています。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.己巳の日ですか():
                print( "{}\t{}".format( k,  '己巳の日') )
            else:
                print( date )
        print() 
        print()
        
        
        
        
        
    # 大明日
    if IS_TEST_MODE:
        print('is_daimyouichi(): 大明日は「大みょう」と書かれることが多い。大吉日、特に善事・吉事に良い日。建築、移転、旅行などは殊によい。')
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.大明日ですか():
                print( "{}\t{}".format( k,  '大明日') )
            else:
                print( date )
        print() 
        print()



    # 甲子
    if IS_TEST_MODE:
        print('is_kasshi: 甲子（かっし,かし,こうし,きのえね）六十干支の最初。五行説でも「木水」の組み合わせで相生。このため目出度い日とされ、この日に祭り（甲子祭）をするなどの風習があった。')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.甲子ですか():
                print( "{}\t{}".format( k,  '甲子') )
            else:
                print( date )
        print() 
        print()




    # 節分
    if IS_TEST_MODE:
        print('is_setsubun: 節分')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.節分ですか():
                print( "{}\t{}".format( k,  '節分') )
            else:
                print( date )
        print() 
        print()




    #彼岸
    if IS_TEST_MODE:
        print('is_setsubun: 節分ですか')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.彼岸ですか():
                print( "{}\t{}".format( k,  '彼岸') )
            else:
                print( date )
        print() 
        print()




    #土曜
    if IS_TEST_MODE:
        print('is_doyou(): 土用ですか()')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.土用ですか():
                print( "{}\t{}".format( k,  k.土用ですか()) )
            else:
                print( date )
        print() 
        print()






    #社日
    if IS_TEST_MODE:
        print('is_syanichi(): 社日ですか()')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.社日ですか():
                print( "{}\t{}".format( k,  '社日') )
            else:
                print( date )
        print() 
        print()



    #八十八夜
    if IS_TEST_MODE:
        print('is_hachijyuuhachiya(): 八十八夜ですか()')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.八十八夜ですか():
                print( "{}\t{}".format( k,  '八十八夜') )
            else:
                print( date )
        print() 
        print()



    #二百十日
    if IS_TEST_MODE:
        print('is_nihyakutouka(): 二百十日ですか()')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.二百十日ですか():
                print( "{}\t{}".format( k,  '二百十日') )
            else:
                print( date )
        print() 
        print()


    #二百二十日
    if IS_TEST_MODE:
        print('is_nihyakuhatsuka(): 二百二十日ですか()')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.二百二十日ですか():
                print( "{}\t{}".format( k,  '二百二十日') )
            else:
                print( date )
        print() 
        print()
        
        
        
        
        
    if IS_TEST_MODE:
        print('is_ooduti(), 大土ですか()\tis_koduti(), 小土ですか')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.大土ですか():
                print( "{}\t{}".format( k,  '大土') )
            elif k.小土ですか():
                print( "{}\t{}".format( k,  '小土') )
            else:
                print( date )
        print() 
        print()




    if IS_TEST_MODE:
        print('is_sanpuku(), 三伏ですか（）')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.三伏ですか():
                print( "{}\t{}".format( k,  '三伏') )
            else:
                print( date )
        print() 
        print()        







    if IS_TEST_MODE:
        print('is_koushin(), 庚申ですか（）')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.庚申ですか():
                print( "{}\t{}".format( k,  '庚申') )
            else:
                print( date )
        print() 
        print()        
    





    if IS_TEST_MODE:
        print('is_roujitsu(), 臘日ですか()')        
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            if  k.臘日ですか():
                print( "{}\t{}".format( k,  '臘日') )
            else:
                print( date )
        print() 
        print()
        
        if False:
            t = rekityuu.today()
            kyuureki = "2021-12-09"
            shinreki = t.convert_kyuureki_to_shinreki(kyuureki)
        print( shinreki )
        print() 
        print()






    if True:
        t = rekityuu.today()
        
        for date in rekityuu.dates_in_year(t.year):
            k = rekityuu.fromisoformat(date)
            
            text = str(k)
            text += " (" + k.youbi + ") "
            text += k.rokuyou
            text += "\t" + k.jyuunichoku
            text += "\t" + k.nijyuuhassyuku
            
            if k.is_fujyoujyunichi():
                text += "\t不成就日"
            
            if k.is_jyushibi():
                text += "\t受死日"
            
            if k.is_jyuushinichi():
                text += "\t十死日"
            
            
            if k.is_sanrinbou():
                text += "\t三隣亡"
            
            
            if k.is_hassen():
                text += "\t八専"
            
            
            if k.is_jippoukure():
                text += "\t十方暮"
            
            if k.is_ichiryuumandainichi():
                text += "\t一粒万倍日"
                
            
            if k.is_tenshanichi():
                text += "\t天赦日"
                
            
            if k.is_toranohi():
                text += "\t寅の日"
                  
            
            if k.is_minohi():
                text += "\t己の日"

                
            
            if k.is_tuchinotominohi():
                text += "\t己巳の日"                
                                
            
            if k.is_daimyouichi():
                text += "\t大明日"
                
                
                                
            
            if k.is_kasshi():
                text += "\t甲子"
                
            if k.is_setsubun():
                text += "\t節分"
                

            if k.is_higan():
                text += "\t彼岸"

            if k.is_doyou():
                text += "\t土用"

            if k.is_syanichi():
                text += "\t社日"

            if k.is_hachijyuuhachiya():
                text += "\t八十八夜"   
                
            if k.is_nihyakutouka():
                text += "\t二百十日"                                
            
            if k.is_nihyakuhatsuka():
                text += "\t二百二十日"             
                                

            if k.is_ooduti():
                text += "\t大土"
                
                
            if k.is_koduti():
                text += "\t小土"
                
                
            if k.is_sanpuku():
                text += "\t三伏"
                
                
                
            if k.is_koushin():
                text += "\t庚申"
                
            if k.is_roujitsu():
                text += "\t臘日"    
                

                
                
            print( text )
            
        
