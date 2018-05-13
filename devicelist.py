#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__= 'xul'

import os


yunfo_list = {'BSNAP300J16090151': 'C4CD451002E2'}

jiangmen_list = {'BSNAP300J16110344': 'C4CD4510079B',
                 'BSNAP300J16090118': 'C4CD451002C1',
                 'BSNAP300J16110177': 'C4CD451006F4'}

citylist = {
    'yunfo': yunfo_list,
    # 'meizhou': meizhou_list
    'jiangmen': jiangmen_list
}

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
certificate_dir = os.path.join(CURRENT_PATH, 'cert')
xlsx = os.path.join(CURRENT_PATH, 'result.xlsx')


def get_citylist(cityname):
    device_data = citylist.get(cityname)
    if not device_data:
        print('指定城市数据不存在，请添加数据后再试！')
        exit(-1)
    return device_data
