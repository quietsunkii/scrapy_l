#! /bin/sh

export PATH=$PATH:/usr/local/bin

cd /home/pi/scrapy_l/

nohup scrapy crawl mediaget >> mediaget.log 2>&1 &
