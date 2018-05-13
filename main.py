#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__= 'xul'

import os
import logging

from plumbum import cli

from handlers import get_device_data, create_city_dir, key_gen, write_file, close_log


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)


class CertGenerator(cli.Application):
    PROGNAME = '基站证书生成工具'
    VERSION = 'v0.1'
    USAGE = 'python3 main.py [Switches]\n'

    amount = cli.SwitchAttr(["-a", "--amount"], argtype=int, help='指定需要生成的证书数量')
    cityname = cli.SwitchAttr(['-c', '--cityname'], argtype=str, help='指定生成证书的城市名')
    infile = cli.SwitchAttr(['-f', '--in-file'], cli.ExistingFile, help='指定保存有sn和mac的Excel文件作为devicelist', requires=['-c'])

    @cli.switch(["--no-log"], help='关闭屏幕日志输出')
    def remove_handler(self):
        logger.removeHandler(console)
        close_log()

    def main(self):
        logger.debug('amount={},cityname={}'.format(self.amount, self.cityname))
        device_data = get_device_data(self.cityname, self.amount, self.infile)
        if not device_data:
            return(self.helpall())
        cityname_dir = create_city_dir(self.cityname)
        key_dict = key_gen(cityname_dir, device_data)
        cityname = os.path.split(cityname_dir)[1]
        write_file(cityname, key_dict)


if __name__ == '__main__':
    CertGenerator()
