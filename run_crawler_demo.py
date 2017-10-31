import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import os
import shutil
import glob
import sys
import csv

curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
tmpDir = os.path.abspath(os.path.join(curDir,'demo/tmp/'))

# remove old crawling data
try:
    shutil.rmtree(tmpDir)
except:
    pass 

# get the product name from the arguments
pruduct = sys.argv[1]

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
s=get_project_settings()

# Change the depth limit here
s['DEPTH_LIMIT'] = 2
process = CrawlerProcess(s)

# Add spiders to crawl
process.crawl('amazon',product=pruduct)
process.crawl('ebay',product=pruduct)
process.crawl('shopclues',product=pruduct)
process.crawl('olx',product=pruduct)

# Start Crawling
process.start()

# Add results to results.csv file after crawling is complete
interesting_files = glob.glob(tmpDir+'/*.csv')
header_saved = False
with open('results.csv','wb') as fout:
    for filename in interesting_files:
        if os.path.getsize(filename) > 0:
            with open(filename) as fin:
                header = next(fin) 
                if not header_saved:
                    fout.write(header)
                    header_saved = True
                for line in fin:
                    fout.write(line)