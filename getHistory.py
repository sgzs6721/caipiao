#encoding: utf-8
import urllib2
import time
# from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import MySQLdb

def getBeautifulSoup(url) :
    times = 0
    while times < 10 :
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

        clock     = datetime.split(" ")[1]
        year      = num[:4]
        month     = num[4:6]
        day       = num[6:8]
        no        = num[8:]

        if datetime[:4] == "0000" :
            weekday = "0"
        else :
            timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
            weekday   = time.strftime("%w", timeArray)

        statement = "insert into " + category + type  + \
        "(`num`,`year`,`month`,`day`, `weekday`,`time`,`no`,`first`,`second`,`third`,`fourth`,`last`) VALUES ('" + \
        num + "','" + year + "','" + month + "','" + day + "','" + weekday + "','" + clock + "','" + no + "','" + \
        dataNumber[0] + "','" + dataNumber[1] + "','" + dataNumber[2] + "','" + dataNumber[3] + "','" + dataNumber[4] + "')"
        cur.execute(statement)
        cur.close()
        conn.commit()
        print " ".join([num, year, month, day, weekday, clock, no, dataNumber[0], dataNumber[1], dataNumber[2], dataNumber[3], dataNumber[4]])

    except MySQLdb.Error, e:
        # print "\tMysql Error %d: %s" % (e.args[0], e.args[1])
        pass

def getDataAndInsertDB(type, category, getPages, page = 1) :

    times = 3
    while times > 0 :
        try :
            url = getUrl(type, category, page)
            soup = getBeautifulSoup(url)
            if not soup :
                print "Exit"
                exit(1)

            if getPages :
                pages = soup.find(id='pages').text.encode("utf8").split(" ")[2].split("/")[1]
                return int(pages)

            else:

                tableTr = soup.findAll("table")[1].findAll("tr")[1:]
                tableTr.reverse()
                for index, tr in enumerate(tableTr) :
                    td = tr.findAll("td")
                    date = td[1].span.text.encode("utf8")
                    timeN = td[2].text.encode("utf8")
                    dataNumberDiv = td[3].div.findAll("span")
                    dataNumber = []
                    for span in dataNumberDiv :
                        dataNumber.append(span.text.encode("utf8"))

                    insertDB(type, category, date, timeN, dataNumber)
            times = 0

        except :
            print "Get Data Error, try again after 2 seconds ..."
            time.sleep(2)
            times = times - 1
            if times == 0 : exit(1)

    return

host = "localhost"
user = "root"
passwd = "1qazxsw2"
port = 3306
database = "lottery"

conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset='utf8')

# pageType = {"11x5" :["gd", "jx"]}
pageType = {"ssc":["cq", "xj"]}


for type in pageType :
    for category in pageType[type] :
        page = getDataAndInsertDB(type, category, True)
        # page = 500
        minute = "0"
        # if category == "sd" : minute = "5"
        while page > 0 :
            print "Get data(p" + str(page) + ") from " + category + type
            getDataAndInsertDB(type, category, False, page)
            page = page - 1

            if str(time.localtime()[4])[1:] == minute :
                print "Sleeping 150 seconds ......"
                time.sleep(100)
                page = page + 1
conn.close()
