#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1年でラッキーな日を列記する
@author: naokitakisawa
"""

import datetime as dt
import pandas as pd
import locale

from qreki import Kyureki

import Jikkan
import Jyuunishi
import Ichiryuumanbainichi
import Tenshanichi
import Fujyoujyunichi
import Nijyuuhassyuku
import Jyushibi
import Jyuunityoku

print('不成就日とは、何事もうまくいかない、何をしても良い結果にならず願い事が叶わない縁起の悪い日（凶日）。\n')
print('天赦日とは、天が万物の罪を赦す（許す）日で、最上の大吉日。年に5～6日しかないことから、「大安よりお日柄が良い」といわれる。')
print('一粒万倍日とは、新しいことをスタートするのに良い日とされ、特に仕事始めや開業、種まき、お金の支出に吉。しかし借金や借りを作ることは、苦労の種が増えるのでよくないとされる。他の暦注と日が重なったとき、吉日と重なれば一粒万倍日の効果が倍増し、凶日と重なれば半減するという。\n')
print('鬼宿日とは、二十八宿の「鬼」の日。大吉日、長寿や名誉を祝うのに殊に良い日。')
print('受死日は「病を患えば必ず死ぬ最悪の大凶日」という扱いを受けており、一説には他の暦注を一切無視して凶日にしてしまうほどの力があると言われております。')
print('寅の日は、干支の中でも最も金運に縁のある吉祥日。金運将来日。読み方は「とらのひ」。')
print('己巳と巳')
thisYear = dt.date.today().year


date_index = pd.date_range(start=str(thisYear) + '-01-01', end=str(thisYear) + '-12-31', freq="D")
date_ary = date_index.to_series().dt.strftime("%Y-%m-%d")

fujyou = Fujyoujyunichi.Fujyoujyunichi(thisYear)
jyushibi = Jyushibi.Jyushibi(thisYear)
jyuunityoku = Jyuunityoku.Jyuunityoku(thisYear)

for a_date in date_ary.values:
    y, m, d = [int(a) for a in a_date.split('-')]
    date = dt.date(y, m, d)
    
    # 曜日
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    youbi = date.strftime('%a')
    
    
    events = ''
    
    # 六曜
    k = Kyureki.from_ymd(y, m, d)
    events += k.rokuyou
    
    
    # 十二直
    events += '、　' + jyuunityoku.jyuunityoku(a_date)
    
    # 二十八宿の鬼宿日
    nijyuuhassyuku = Nijyuuhassyuku.nijyuuhassyukubi(a_date)
    events += '、　' + nijyuuhassyuku + '宿'
        
    # 不成就日
    if fujyou.is_fujyoujyunichi(a_date):
        events += '、　不成就日'
    
    
    # 受死日
    if jyushibi.is_jyushibi(a_date):
        events += '、　受死日'
        
        
    # 天赦日
    tensyanichi = Tenshanichi.is_tensyanichi(a_date)
    if tensyanichi:
        events += '、　天赦日'
    
    # 一粒万倍日
    chiryuumanbainichi = Ichiryuumanbainichi.is_ichiryuumanbainichi(a_date)
    if chiryuumanbainichi:
        events += '、　一粒万倍日'
        
    #十二支
    jyuunishi = Jyuunishi.jyuunishi_of_date(a_date)
    if jyuunishi == '寅':
        events += '、　寅の日'
    
    jyuunishi = Jyuunishi.jyuunishi_of_date(a_date)
    jikkan = Jikkan.jikkan_date(a_date)
    if jyuunishi == '巳' and jikkan == '己':
        events += '、　己巳の日'
    elif jyuunishi == '巳':
        events += '、　巳の日'
    
    
    
    
    
    
    print( "{} ({})\t {}".format(date, youbi, events))