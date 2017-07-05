# crawler_python
Here records my mini python projects, most of them are crawlers.

## crawlNGO.py
*usage*: python crawlNGO.py

This is specifically used to crawl for the NGO list from http://www.chinadevelopmentbrief.org.cn/directoryindex.html. The idea is simple, analyze URL pattern, it is very fast to get the solution.
However, I still encountered some problems when I programed it.
* urllib can't work well with bs, the type has conflict. Luckily, urllib2 works well. I guess urllib is good at crawling web links, urllib2 is good to crawling the content together with bs.
* csv can't write unicode, at first I thought this is encode/decode problem. Finally I realized it's because csc can only write string.

## crawler.py & spider.py
*usage*: python crawler -r <file with urls>

This one is for general purpose to deeply crawl the website you provided, with width deepth you set. For some unknown reason, the original spider.py can't run on my computer, so I did a little modification(search "by rg").
*It's originally from* https://github.com/smartFlash/pySecurity/blob/master/zh-cn/0x6.md

## scrapy scripts
Looking into scrapy, I realize this framework is quite awesome, very straightforward, easy to pick up. Recommend! 

## totopredict
TOTO is a Singapore lottory. Pick 6 numbers from 0-50, if you hit 4 or more you can win the money. Normally I only hit 2, but with the predictor I can often hit 3, need a little luck to win.
I didn't play TOTO anymore, didn't win any money, but writting the predicot gave me many fun.
*Code lost in my current computer need to check my old one, to be uploaded*
