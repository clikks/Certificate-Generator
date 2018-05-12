#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__= 'lux'



yunfo_list = {'BSNAP300J16090151': 'C4CD451002E2'}

meizhou_list =  {'BSNAP300J16110344': 'C4CD4510079B',
                'BSNAP300J16090118': 'C4CD451002C1',
                'BSNAP300J16110177': 'C4CD451006F4'}
        
citylist = {
    'yunfo' : yunfo_list,
    'meizhou' : meizhou_list
}

certificate_dir = '/home/sky/gen_certificates/certficates'
xlsx = '/home/sky/gen_certificates/result.xlsx'

def get_citylist(city):
   return citylist.get(city)
