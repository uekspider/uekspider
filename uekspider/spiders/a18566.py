# -*- coding: utf-8 -*-
import scrapy


class A18566Spider(scrapy.Spider):
    name = '19082'
    allowed_domains = ['hq.tsinghua.edu.cn']
    start_urls = ['http://hq.tsinghua.edu.cn/front/frontAction.do?ms=gotoSecond&lmid=12457']

    def parse(self, response):
        hrefs = response.xpath("//section[@class='r_cont']/dl/dt/a/@href").re("\d+")  # 从页面中获取所有列表题目
        titles = response.xpath("//section[@class='r_cont']/dl/dt/a/text()").extract()  # 从页面中获取所有列表题目
        urls = [ 'http://hq.tsinghua.edu.cn/front/frontAction.do?ms=gotoThird&lmid=12457&sign=hq&xxid=%s'%url for url in hrefs]
        for url in urls:
            yield scrapy.Request(url,self.getCon)

    def getCon(self,response):
        title = response.xpath("/html/body/div[2]/article/section/h1/text()").extract()
        print(title)