# crawler_python
here records some crawler scripts, for specific purpose or general purpose
##crawlNGO.py
*usage*: python crawlNGO.py

This is specifically used to crawl the NGO list from http://www.chinadevelopmentbrief.org.cn/directoryindex.html. The idea is quite simple, analyse how they generate url for each NGO, and the content with the html, it's very fast to get the solution.
However, I still encountered some problem when I program it.
* urllib can't work well with bs, the type has conflict. Luckily, urllib2 works well. I guess urllib is good at crawling web links, urllib2 is good to crawling the content together with bs.
* csv can't write unicode, at first I thought this is encode/decode problem. Finally I realized it's because csc can only write string.

## crawler.py & spider.py
*usage*: python crawler -r <file with urls>

This one is for general purpose to deeply crawl the website you provided, with width deepth you set. For some unknown reason, the original spider.py can't run on my computer, so I did a little modification(search "by rg").
*It's originally from* https://github.com/smartFlash/pySecurity/blob/master/zh-cn/0x6.md
