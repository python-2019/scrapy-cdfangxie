#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy

from cdfx.items import CdfxItem


class cdfxScrapy(scrapy.Spider):
    name = 'cdfx'
    allowed_domains = ["cdfangxie.com"]
    host = "http://www.cdfangxie.com"
    start_urls = (
        host + "/Infor/type/typeid/36.html",
    )

    # //span[@class='sp_name']/following-sibling::span[1] 日期
    def parse(self, response):
        item = CdfxItem()
        li_list = response.xpath("//ul[@class='ul_list']/li")
        for li in li_list:
            title = li.xpath("span[1]/a/text()").extract_first()
            if title is not None:
                item['title'] = title

            date = li.xpath("span[2]/text()").extract_first()
            if date is not None:
                item['date'] = date

            href = li.xpath("span[1]/a/@href").extract_first()
            if href is not None:
                item['href'] = self.host + href
            yield item
        has_next_page = response.xpath("//div[@class='pages2']/b/a[contains(text(), '下一页')]").extract_first()
        if has_next_page is not None:
            next_page = self.host + response.xpath("//div[@class='pages2']/b/a[contains(text(), '下一页')]/@href").extract_first()
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
