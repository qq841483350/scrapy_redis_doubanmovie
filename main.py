#coding:utf8
from scrapy import cmdline
cmdline.execute('scapy crawl doubanmovie'.split())  #这里的doubanmovie是spiders下的文件