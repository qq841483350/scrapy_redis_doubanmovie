# -*- coding: utf-8 -*-
'''scrapy-redis爬取豆瓣电影排行榜信息并将信息插入到Mongodb数据库,python操作mongodb  http://movie.douban.com/top250/  电影名称，电影信息，电影评分，一句话评价并保存到CSV文件中
'''
import scrapy,sys
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy_redis.spiders import RedisSpider
class DoubanmovieSpider(RedisSpider):
    name = "doubanmovie"
    redis_key = 'doubanmovie:start_urls'
    allowed_domains = ["movie.douban.com"]   #允许域名
    # start_urls = (
    #     'http://movie.douban.com/top250',
    # )
    url="http://movie.douban.com/top250"
    def parse(self, response):
        item=DoubanItem()
        selector=Selector(response)
        Movies=selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            titles=eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()  #其实是一外列表，有三个标题
            title=' '.join(titles) #把列表中的标题，以空格形式连接起来     #标题
            movieInfos=eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            movieInfo=''.join(movieInfos) #电影信息
            star=eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]  #电影评分
            quote=eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()  #一句话总结
            if quote:
                quote=quote[0]
            else:
                quote='............................................................'
            # print quote
            item['title']=title
            item['movieInfo']=movieInfo
            item['star']=star
            item['quote']=quote
            yield item
        nextLink=selector.xpath('//span[@class="next"]/a/@href').extract()#下一页URL
        if nextLink:  #判断是否有下一页
            nextLink=nextLink[0]
            # print nextLink,'00000000000000000000000000000000000000000000000000000000'
            yield Request(self.url+nextLink,callback=self.parse)  #回调函数

