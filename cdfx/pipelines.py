# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class CdfxPipeline(object):

    def open_spider(self, spider):
        self.file = open('成都房协.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        headers = ['楼盘', '发布日期', '链接']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        row = [item['title'], item['date'], item['href']]
        self.csv_writer.writerow(row)
        print(row)
        return item

    def close_spider(self, spider):
        self.file.closed()
