#encoding: utf-8
import urllib2
import time
# from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import MySQLdb

def getBeautifulSoup(url) :
    times = 0
    while times < 10 :
        # print "The " + str(times + 1) + " times getting data!"
        try :
            req = urllib2.Request(url)
            res = urllib2.urlopen(req, timeout = 15).read()
            # return BeautifulSoup(res, "html.parser")
            return BeautifulSoup(res)

        except :
            print "Could not get data from " + url
            print "Sleep 3 seconds and retrying ..."
            time.sleep(3)
            times = times + 1
    return ""

def getUrl(type, category, page) :
    if type == "11x5" : category = category + type
    url = "http://caipiaow.com/index.php?m=kaijiang&a=index&cz="+ \
    category + "&type=" + type + "&p=" + str(page)
    return url

def insertDB(type, category, num, datetime, dataNumber) :
    try :
        cur = conn.cursor()

        no        = num[8:]
        timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
        year      = time.strftime("%Y", timeArray)
        month     = time.strftime("%m", timeArray)
        day       = time.strftime("%d", timeArray)
        weekday   = time.strftime("%w", timeArray)
        clock     = datetime.split(" ")[1]

        statement = "insert into " + category + type  + \
        "(`num`,`year`,`month`,`day`, `weekday`,`time`,`no`,`first`,`second`,`third`,`fourth`,`last`) VALUES ('" + \
        num + "','" + year + "','" + month + "','" + day + "','" + weekday + "','" + clock + "','" + no + "','" + \
        dataNumber[0] + "','" + dataNumber[1] + "','" + dataNumber[2] + "','" + dataNumber[3] + "','" + dataNumber[4] + "')"

        cur.execute(statement)
        cur.close()
        conn.commit()
        print " ".join([num, year, month, day, weekday, clock, no, dataNumber[0], dataNumber[1], dataNumber[2], dataNumber[3], dataNumber[4]])

    except MySQLdb.Error,e:
        print "\tMysql Error %d: %s" % (e.args[0], e.args[1])
        pass

def getDataAndrInsertDB(type, category, page = 1) :
    url = getUrl(type, category, page)
    soup = getBeautifulSoup(url)
    if not soup :
        print "Exit"
        exit(1)
    tableTr = soup.findAll("table")[1].findAll("tr")[1:]
    tableTr.reverse()
    for index, tr in enumerate(tableTr) :
        #if index <= 12 : continue
        td = tr.findAll("td")
        date = td[1].span.text.encode("utf8")
        time = td[2].text.encode("utf8")
        dataNumberDiv = td[3].div.findAll("span")
        dataNumber = []
        for span in dataNumberDiv :
            dataNumber.append(span.text.encode("utf8"))

        insertDB(type, category, date, time, dataNumber)
    return

host = "localhost"
user = "root"
passwd = "1qazxsw2"
port = 3306
database = "lottery"

conn=MySQLdb.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset='utf8')

pageType = {"ssc":["cq", "xj", "tj"], "11x5": ["jx", "sd", "gd"]}
pageType = {"ssc":["cq"]}


for type in pageType :
    page = 1
    print "Get data from " + type
    for category in pageType[type] :
        getDataAndrInsertDB(type, category, page)
conn.close()
