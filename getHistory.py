#encoding: utf-8
import urllib2
import time
from bs4 import BeautifulSoup
import MySQLdb

def getBeautifulSoup(url) :
    times = 0
    while times < 10 :
        # print "The " + str(times + 1) + " times getting data!"
        try :
            req = urllib2.Request(url)
            res = urllib2.urlopen(req, timeout = 15).read()
            return BeautifulSoup(res, "html.parser")
        except :
            print "Could not get data from " + url
            print "Sleep 3 seconds and retrying ..."
            time.sleep(3)
            times = times + 1
    return ""

def getUrl(type, page) :
    url = "http://caipiaow.com/index.php?m=kaijiang&a=index&cz="+ \
    type + "&type=ssc&p=" + str(page)
    return url

def checkThree(dataNumber) :
    if dataNumber[0] == dataNumber[1] :
        return "1"
    if dataNumber[0] == dataNumber[2] :
        return "1"
    if dataNumber[1] == dataNumber[2] :
        return "1"
    return "0"

def checkDup(lastNumber, dataNumber) :
    if lastNumber[0] =="-" :
        return "0"
    for i in range(len(lastNumber)) :
        if lastNumber[i] == dataNumber[i] :
            return "1"
    return "0"

def getMaxID(type) :
    cur = conn.cursor()
    statement = "select max(ID) from " + type + "ssc;"
    cur.execute(statement)
    return cur.fetchone()[0] + 1

def insertDB(type, date, time, dataNumber, front3, end3, frontDup4, endDup4, allDup) :
    try :
        ID = str(getMaxID(type))
        cur = conn.cursor()
        statement = "insert into " + "`" + type + "ssc`"  + \
        "(`ID`,`date`,`time`,`number`,`front3`,`end3`,`front4`,`end4`,`all`) VALUES ('" + ID + "','" + \
        date + "','" + time + "','" + dataNumber +"','"+ front3 + "','" + end3 + "','" + \
        frontDup4 + "','" + endDup4 + "','" + allDup + "')"

        print cur.execute(statement)
        cur.close()
        conn.commit()
	print " ".join([date, time.strip(), dataNumber, front3, end3, frontDup4, endDup4, allDup])
    except MySQLdb.Error,e:
	print "\tMysql Error %d: %s" % (e.args[0], e.args[1])
        pass

def getDataAndrInsertDB(type, page = 1) :
    url = getUrl(type, page)
    soup = getBeautifulSoup(url)
    if not soup :
        print "Exit"
        exit(1)
    tableTr = soup.findAll("table")[1].findAll("tr")[1:]
    tableTr.reverse()
    lastNumber = "-----"
    for index, tr in enumerate(tableTr) :
        #if index <= 12 : continue
        td = tr.findAll("td")
        date = td[1].span.text.encode("utf8")
        time = td[2].text.encode("utf8")
        dataNumberDiv = td[3].div.findAll("span")
        dataNumber = ""
        for span in dataNumberDiv :
            dataNumber = dataNumber + span.text.encode("utf8")

        #print " ".join([type, date, time, dataNumber])
        insertDB(type, date, time, dataNumber, checkThree(dataNumber[0:3]),
                 checkThree(dataNumber[2:]), checkDup(lastNumber[0:4], dataNumber[0:4]),
                 checkDup(lastNumber[1:5], dataNumber[1:5]), checkDup(lastNumber, dataNumber))
        lastNumber = dataNumber
    return

host = "localhost"
user = "root"
passwd = "root@lottery"
port = 3306
database = "lottery"

conn=MySQLdb.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset='utf8')

for type in ["cq", "jx", "tj", "xj"] :
    page = 1
    print "Get data from " + type
    getDataAndrInsertDB(type, page)
conn.close()
