# Script Name                    : AutoReport.py
# Author                    : zhd
# Created                    : December 31, 2015
# Last Modified                    : 
# Version                    : 1.0

# Modifications                    : 

# Description                    : This script is automatically generated report.

import os, time, datetime
import urllib
from selenium import webdriver
from splinter import Browser

bo = Browser('chrome')
url = "http://192.168.1.102:8080/report/print.html"     # The report website.

def dwonload(city, area, date):
    '''
    select area and date then query and download.
    '''
    area.click()
    time.sleep(2)
    bo.find_by_xpath('//*[@id="tools"]/span[2]/input[1]').fill(date)
    time.sleep(2)
    bo.find_by_id('query').click()
    while 1:
        src = bo.find_by_id("main")[0]['src']
        if 'static' in src: 
            msg = src.split('/')[6].split('.')[0]            
            msg = urllib.unquote(str(msg)).decode('utf-8')
            #print area'name and date
            print '|' + '_'*4 + msg         
            
            break
        else:
            time.sleep(5)
            
    #print 'Query OK'

    #print 'downloading ...'
    bo.find_by_id('out_w').click()
    #waitting for downloading for 10s
    time.sleep(10)
    bo.visit(url)
    bo.reload()   
    bo.find_by_xpath('//*[@id="tools"]/span[1]/span/span').click()
    time.sleep(2)

def select(date):
    '''
    select city and area
    '''
    bo.visit(url)
    bo.reload()
    bo.find_by_xpath('//*[@id="tools"]/span[1]/span/span').click()
    time.sleep(2)
    i = 1
    while 1:
        city = bo.find_by_xpath('/html/body/div[4]/div/ul/li[' + str(i) + ']/div/span[3]')
        if city:
            #print i, city.first.text
            #print city's name
            print i, city.first.text
            j = 1
            while 1:
                area = bo.find_by_xpath('/html/body/div[4]/div/ul/li[' + str(i) + ']/ul/li[' + str(j) + ']/div/span[4]')
                #print ' '*4 + area.first.text
                if area:                    
                    dwonload(city, area, date)
                else:
                    break
                j = j + 1
        else:
            break
        i = i+1

if __name__ == '__main__':

    # report date, 2014-7\8 and 2015-1\4: date_dict = {'2014':[7,8], '2015':[1,4]},
    date_dict = {'2014':[6,7,8]}
    for (k, v) in date_dict.items():
        for v0 in v:
            date = k + '-' + '{:0>2}'.format(v0) + '-01'
            print '*'*20 + date + '*'*20        
            select(date)
