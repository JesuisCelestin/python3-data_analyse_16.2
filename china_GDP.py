__author__ = 'Administrator'
#! /usr/bin/python <br> # -*- coding: utf8 -*-
import json
import pygal
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'gdp.json'
with open(filename) as f:
    gdp = json.load(f)

china_gdp = []
year_list = []
filename_chn = 'China.json'

with open(filename_chn,'w') as f_c:
    for gdp_dict in gdp:
        if gdp_dict['Country Name'] == 'China':
            json.dump(gdp_dict,f_c)
            year = gdp_dict['Year']
            value = gdp_dict['Value']
            year_list.append(int(year))
            china_gdp.append(int(float(value)))
#GDP增长率
num = len(china_gdp)
zero = [0 for count in range(0,num-1)]
growth_rate = [int(10000*(china_gdp[count+1] - china_gdp[count])/china_gdp[count])/100
               for count in range(0,num-1)]
line_chart = pygal.Line()
line_chart.title = 'Chinese GDP \'s growth rate from ' \
                   ''+str(year_list[0])+' to '+str(year_list[20])+' ( % )'

line_chart.x_labels = map(str,year_list[0:20])
line_chart.add('GDP growth rate',growth_rate[0:20])
line_chart.render_to_file(''+line_chart.title+'v5.svg')
'''
plt.figure(figsize=(10,6))
plt.title('Chinese GDP \'s growth rate from '+str(year_list[0])+' to '+str(year_list[-2])+'')
plt.plot(year_list[:-1],growth_rate,'r--')
plt.plot(year_list[:-1],zero,'b--')
plt.scatter(year_list[:-1],growth_rate,c='r')
plt.xlim([year_list[0], year_list[-2]])
plt.ylim([growth_rate[0]-2, max(growth_rate)+2])
plt.xlabel('Year From 1960 to 2013',fontsize = 14)
plt.ylabel('GDP growth rate ( % )',fontsize = 14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('Chinese GDP \'s growth rate from '+str(year_list[0])+' to '+str(year_list[-2])+'.png',
            bbox_inches='tight')
plt.show()
'''
'''
hist = pygal.Bar()
hist.title = 'Chinese GDP from '+str(year_list[0])+' to '+str(year_list[-1])+''
hist.x_labels = year_list
hist.x_title = 'Year From '+str(year_list[0])+' to '+str(year_list[-1])+''
hist.y_title = 'GDP (dollars)'
hist.add('Chinese GDP',china_gdp)
hist.render_to_file(hist.title+'.svg')
'''
