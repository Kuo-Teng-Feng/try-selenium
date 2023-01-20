import sqlite3
import matplotlib.pyplot as P
from caller import call, sort_from_db_by_date

class Graph:

    def __init__(self, model, begin, end, val1, val2, val3): # 3 lines at most. end - begin < 2 years.

        self.model = model
        self.begin = begin
        self.end = end
        self.val = [val1, val2, val3] # [[[x1, x2....], [y1, y2...], [xv1, xv2...], [yv1, yv2...]], [], []]

    def draw(self):

        val = self.val
        v1 = val[0]

        x1 = v1[0]
        y1 = v1[1]
        xv1 = v1[2]
        yv1 = v1[3]
        P.plot(x1, y1, linestyle = ":", marker = ".", color = "darkblue", ms = 13)

        for i in range(1, 3): # v2 or v3
            
            v = val[i] 
            if v == []: continue
            P.plot(v[0], v[1], linestyle = "-", marker = "*", color = "blue", ms = 13)

        if xv1 != []: P.xticks(x1, xv1, rotation = 30) # determined once for all.
        if yv1 != []: P.yticks(y1, yv1) # determined once for all.
        P.xlabel(f"{self.begin} ~ {self.end}", fontsize = 10)
        P.ylabel("final price", fontsize = 10)
        P.title(self.model, fontsize = 16)
        P.show()

# with sql
def graphify(ids, gb, distributor): # ids = sort_from_db_by_date(conditions['model'], conditions['begin'], conditions['end'], conditions['gb'], conditions['distributor'])

    con = sqlite3.connect("../for_try-selenium/db.db")
    cur = con.cursor()

    res = cur.execute(f"SELECT model, date, price FROM crawler WHERE id IN {tuple(ids)} ORDER BY date") # tuple(list)!
    l = res.fetchall()

    postfix = " "
    if distributor == "": pass
    else: posfix += distributor + " "
    if gb == 0: pass
    else: postfix += gb + "G"

    start = l[0]
    model = start[0] + postfix
    begin = start[1]
    end = l[len(l)-1][1]
    val1 = date_cost(l)
    val2 = [] # week_avg(val1)?
    val3 = [] # month_avg(val1)? 

    cur.close()
    con.close()

    return Graph(model, begin, end, val1, val2, val3)

def date_cost(l): # [(model, date, price),...]

    print(l)
    y = []
    x = []
    xvalues = []
    yvalues = [] # no one line = ... = ....
    yyyy = 0

    for ele in l:

        d = ele[1] # date in str.
        y.append(ele[2]) # price
        xvalues.append(d)

        mm = float(d[5:7])
        dd = float(d[8:])/31
        year = int(d[:4])

        if yyyy > 0 and yyyy < year: mm += 12 # cross new year.                        
        else: # of the same year.
            if yyyy == 0: yyyy = year # 1. ele

        x.append(mm + dd)

    return [x, y, xvalues, yvalues]


# with class data as datalist. not checked yet.
def sort_datalist_by_date(datalist):

    return datalist.sort(key = _key)

def _key(d): # data element in datalist

    return d.date

def graphify_datalist(datalist): # of the same model, sort first by date.

    _from = datalist[0]
    _to = datalist[len(datalist) - 1]

    val1 = date_cost_from_datalist(datalist) # cost one bx one. [x[data1._date, ...], y[data1.cost, ...]]
    val2 = [] # week_avg(val1) # weekly average
    val3 = [] # month_avg(val1) # monthly average

    return Graph(_from.model, _from.date, _to.date, val1, val2, val3)

def date_cost_from_datalist(datalist):

    y = []
    x = []
    xvalues = []
    yvalues = []
    yyyy = 0

    for d in datalist:

        date = d.date
        xvalues.append(date)
        y.append(d.price)

        mm = float(date[5:7])
        dd = float(date[8:])/31
        year = int(date[:4])

        if yyyy > 0 and yyyy < year: mm += 12 # cross new year.                        
        else: # of the same year.
            if yyyy == 0: yyyy = year # 1. ele
            
        x.append(mm + dd)        

    return [x, y, xvalues, yvalues]

#def week_avg(l): # l = val1 = [x[data1._date, ...], y[data1.cost, ...], xv, yv]


# db-based.
if __name__ == '__main__':
    
    conditions = call() # {'model' : model, 'begin' : begin, 'end' : end, 'gb' : gb, 'distributor' : distributor}
    model = conditions['model']
    begin = conditions['begin']
    end = conditions['end']
    gb = conditions['gb']
    distributor = conditions['distributor']
    ids = sort_from_db_by_date(model, begin, end, gb, distributor)    
    graphify(ids, gb, distributor).draw() # check if gb or distributor counts as condition.