# scrapy_redis_doubanmovie
scrapy-redis爬取豆瓣电影排行榜信息并将信息插入到Mongodb数据库



1、启动mongodb,在mongodb目录下启用DOS命令，运行：.\mongod --dbpath ./data

2、启动redis 在redis目录下启用DOS命令，运行  .\redis-server redis.windows.conf

3、运行doubanmovie.py  添加Script关联main

4、喂URL，在redis目录下直接运行 redis-cli.exe文件 或DOS命令下运行 redis-cli,然后运行 lpush doubanmovie:start_urls http://movie.douban.com/top250

5、完成
