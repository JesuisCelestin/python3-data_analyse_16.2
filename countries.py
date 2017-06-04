__author__ = 'Administrator'
#! /usr/bin/python <br> # -*- coding: utf8 -*-
import json
from country_codes import get_country_code
import string as s
from pygal.maps.world import COUNTRIES

def get_first_word(name):
    new_name = ''
    for letter in name:
        new_name += letter
        if letter == ','or letter == ' ' or letter == '.':
            new_name = new_name[:-1] #删掉最后的 , 空格 或者 .
            break
    return new_name

def get_countries(filename,year):
    cc_population = {}
    err_country = []
    with open(filename) as f:
        pop_data = json.load(f)
    err_pop = []
    key = True
    for pop_dict in pop_data:
        if pop_dict['Year'] == str(year):
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_population[code] = population
            if (code == None) :
                err_country.append(country_name)
                err_pop.append(population)
            if country_name == 'World':
                key = False

    new_err = []
    for country_name in err_country:
        new_name = get_first_word(country_name)
        if new_name == 'St':
           new_name = country_name[4:]
           new_name = get_first_word(new_name)
        new_err.append(new_name)

    new_country = {}
    count = -1
    for err_country in new_err:
        count += 1
        for code , country in COUNTRIES.items():
            if err_country in country:
                new_country[code] = err_pop[count]

    for code, pop in new_country.items():
        cc_population[code] = pop

    return cc_population

def get_cm_countries(filename,year):
    cm_countries = {}
    with open(filename) as f:
        pop_data = json.load(f)
    key = True
    for pop_dict in pop_data:
        if pop_dict['Year'] == str(year):
            country_name = pop_dict['Country Name']
            value = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if country_name == 'World':
                key = False
                cm_countries[country_name] = value # 'World' 不在 COUNTRIES 字典里面
            if code and (key == False):
                cm_countries[country_name] = value
    return cm_countries






