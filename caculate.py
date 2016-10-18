#encoding: utf-8
import urllib2
import time
import pprint
# from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import MySQLdb



def getData() :
    cursor = conn.cursor()
    cursor.execute('select num,first,second,third,fourth,last from cqssc')
    result = cursor.fetchall()
    return result


host = "localhost"
user = "root"
passwd = "1qazxsw2"
port = 3306
database = "lottery"

conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset='utf8')

for record in getData() :
    print record[1] + "\n"
conn.close()