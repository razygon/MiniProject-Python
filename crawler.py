#!/usr/bin/python
from spider import webspider as myspider
import sys, optparse

def crawler(URLs):
        for line in open(URLs, 'r'):
                URL = line.strip()
                print URL
                links = myspider(b=URL, w=10, d=2, t=1)
                link_count = len(links[0])
                out = URL+": has a link count of "+str(link_count)
                print "[+] Web Crawl Results for: "+URL
                print out
                for item in links[1]:
                        print item

def main():
        parser = optparse.OptionParser(sys.argv[0]+' '+ \
        '-r <file_with URLs>')
        parser.add_option('-r', dest='URLs', type='string', \
                help='specify target file with URLs')
        (options, args) = parser.parse_args()
        URLs=options.URLs

        if (URLs == None):
                print parser.usage
                sys.exit(0)
        else:
                crawler(URLs)

if __name__ == "__main__":
      main()
