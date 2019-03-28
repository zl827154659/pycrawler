# -*- coding:utf-8 -*-

from crawler import Crawler
import logging, sys
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

def main():
    crawler = Crawler(10000)
    logger.info('run')
    crawler.run(url='https://www.szlcsc.com/')
    # crawler.run(url='https://item.szlcsc.com/112678.html')


if __name__ == '__main__':
    main()
