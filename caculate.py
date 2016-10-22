import MySQLdb
from pprint import pprint

total = 0
def getData() :
    cursor = conn.cursor()
    cursor.execute('select num,first,second,third,fourth,last from cqssc')
    result = cursor.fetchall()
    return result

def getArrayData(array) :
    arraySplited = [[],[],[],[],[]]
    for record in array :
        for i in range(1,6) :
            dic = {}
            dic['no'] = record[0]
            dic['num'] = record[i]
            arraySplited[i-1].append(dic)
    return arraySplited

def fixSimulate(array) :
    modes = [26, 13, 22, 11, 5, 18, 9, 20]
    for category in modes :
        base = list(bin(category).replace('0b','').zfill(5))
        for matchType in ['b', 's', 'o', 'e'] :
            for index, position in enumerate(array) :
                getMatch(base, position, matchType, index)

def getMatch(base, array, matchType, position) :
    count = 0
    for index, num in enumerate(array) :
        result = getResult(matchType, int(num['num']))
        if result != base[(index + 1) % 5 - 1] :
            count += 1
            print position + 1, index + 1, matchType, num['no'], num['num'], 'NOT MATCHED'
        else :
            print position + 1, index + 1, matchType, num['no'], num['num'], 'MATCHED', count + 1
            count = 0

def getResult(matchType, num) :
    if matchType == 'b' :
        result = '1' if num > 4 else '0'
    if matchType == 's' :
        result = '1' if num < 5 else '0'
    if matchType == 'o' :
        result = '1' if num % 2 == 1 else '0'
    if matchType == 'e' :
        result = '1' if num % 2 == 0 else '0'
    return result

host = "localhost"
user = "root"
passwd = "1qazxsw2"
port = 3306
database = "lottery"

conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset='utf8')
data = getArrayData(getData())
fixSimulate(data)
conn.close()