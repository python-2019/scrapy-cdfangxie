# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os

from scrapy.conf import settings


class CdfxPipeline(object):

    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH")
        dir = file_path[0:file_path.rfind("/")]
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.file = open(file_path, 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        headers = ['楼盘', '发布日期', '链接']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        row = [item['title'], item['date'], item['href']]
        self.csv_writer.writerow(row)
        print(row)
        return item

    def close_spider(self, spider):
        self.file.flush()
