#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy

# 这里是正确的 应该以spider上级目录(cdfx)为根目录
from cdfx.items import CdfxItem


class cdfxScrapy(scrapy.Spider):
    """
        成都房协网  预售楼盘公示
    """
    name = 'cdfangxie'
    allowed_domains = ["cdfangxie.com"]
    host = "http://www.cdfangxie.com"
    start_urls = (
        host + "/Infor/type/typeid/36.html",
    )

    def parse(self, response):
        #  楼盘li 标签  list
        li_list = response.xpath("//ul[@class='ul_list']/li")
        # 遍历爬取 信息
        for li in li_list:
            flag = li.xpath("span[1]/a/text()").extract_first()
            if flag is not None:
                item = CdfxItem()
                item['title'] = li.xpath("span[1]/a/text()").extract_first()
                item['date'] = li.xpath("span[2]/text()").extract_first()
                item['href'] = self.host + li.xpath("span[1]/a/@href").extract_first()
                print(item)
                yield item
        # 翻页处理
        has_next_page = response.xpath("//div[@class='pages2']/b/a[contains(text(), '下一页')]").extract_first()
        if has_next_page is not None:
            next_page = self.host + response.xpath(
                "//div[@class='pages2']/b/a[contains(text(), '下一页')]/@href").extract_first()
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
