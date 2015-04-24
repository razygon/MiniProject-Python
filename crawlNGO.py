#! /usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import csv
import time

url_head=r"http://www.chinadevelopmentbrief.org.cn/org"

def debugPrint(print_str):
    print print_str
    pass

def writetoFile(ngolist):
    with open("NGOlist3.csv", 'wb') as csvfile:
        fwriter = csv.writer(csvfile, delimiter='|',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(["No","title_cn","titel_en", "URL","founded_year", "field", "ppl", "location", "detail"])
        for item in ngolist:
            fwriter.writerow(item)

def parseSoup(No, url, parsed_soup):
    if parsed_soup.find("div","ml_name mt15"):
        title_cn = unicode(parsed_soup.find("div","ml_name mt15").h1.string).encode('utf-8')
        try:
            title_en = unicode(parsed_soup.find("div","ml_name mt15").font.string).encode('utf-8') #if null, non
        except:
            title_en = ' '
        lis = parsed_soup.find("ul", "ml_tag fl ml10 mt20").find_all("li")
        for item in lis:
            if  u"成立时间" in item.text:
                founded = unicode(item.text[item.text.find(u"：")+1:]).encode('utf-8')
            elif u"工作领域" in item.text:
                field = unicode(item.text[item.text.find(u"：")+1:]).encode('utf-8')
            elif u"机构规模" in item.text:
                ppl = unicode(item.text[item.text.find(u"：")+1:]).encode('utf-8')
            elif u"项目地区" in item.text:
                location = unicode(item.text[item.text.find(u"：")+1:]).encode('utf-8')
        description = ' '.join(unicode(parsed_soup.find("div","jgjs mt20").text).encode('utf-8').split())
        out = [No,title_cn, title_en, url, founded, field, ppl, location, description]
        return out
    else:
        return None


def main():
    start=time.time()
    sum_valid_ngo = 0
    ngolist = [] #[title, founded year, field, ppl, location, description]
    for i in range(1,4001):
        try:
            url = url_head + str(i)+"/"
            debugPrint(url)
            # req = urllib2.Request(url)
            soup = urllib2.urlopen(url)
            # print type(url)
            out_soup = parseSoup(str(i), url, BeautifulSoup(soup.read()))
            if out_soup:
               # print out_soup
                ngolist.append(out_soup)
                sum_valid_ngo = sum_valid_ngo +1
            else:
                print str(i)+" is not valid"
        except:
            pass
        # print url+"  no content"
    writetoFile(ngolist)
    print sum_valid_ngo
    consumed=time.time()-start
    print consumed

if __name__ == '__main__':
    main()
