__author__ = 'Administrator'
#! /usr/bin/python <br> # -*- coding: utf8 -*-
import pygal
import json
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from countries import get_cm_countries
#将数据加载到一个列表中
filename = 'gdp.json'


#根据输入的文件名以及年份画一张图
def one_plot(filename,year):
    cc_GDP = {}
    cc_GDP1={}
    cc_GDP = get_cm_countries(filename,year)
    #把GDP达到万亿以上的国家存进字典 cc_GDP1
    for cc,GDP in cc_GDP.items():
        if  GDP > 1E12:
            cc_GDP1[cc] = GDP

    dic = sorted(cc_GDP1.items(), key=lambda d:d[1], reverse = True)
    dic = dic[0:10]
    line_chart = pygal.HorizontalBar()
    line_chart.title='The top 10 countries in '+str(year)+'-GDP-Rank'
    for element in dic:
        line_chart.add(element[0],int(element[1]))
    line_chart.render_to_file('top 10 in '+str(year)+'.svg')

for year in range(2008,2015):
    one_plot(filename,year)
    # print(year)
'''
wm_style = RotateStyle('#EE2C2C',base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2014, by Country'
wm.add('0-billion',cc_GDP1)
wm.add('1billion-1trillion',cc_GDP2)
wm.add('>1trillion',cc_GDP3)

wm.render_to_file('world_GDP_v8.svg')
'''

