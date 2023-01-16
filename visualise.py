import sqlite3
import matplotlib.pyplot as P

class Graph:

    def __init__(self, model, begin, end, val1, val2, val3):

        self.model = model
        self.begin = begin
        self.end = end
        self.val = [val1, val2, val3] # [[[x1, x2....], [y1, y2...]], [], []]

    def draw(self):

        #val = self.val
        val = [[[1,2,2,3,4,6,7], [5,6,7,8,9,3,7]]]
        P.plot(val[0][0], val[0][1], linestyle = "", marker = ".", color = "darkblue", ms = 13)
        #P.xlabel(f"{self.begin} ~ {self.end}", fontsize = 10)
        #P.ylabel("final price", fontsize = 10)
        #P.title(self.model, fontsize = 12)
        P.show()

g = Graph("test", "begin", "end", [[1,1,2,3,4,4,6,7], [2,5,4,6,8,9,3,7]], [], [])
g.draw()

# with class data as datalist
def graphify(datalist): # of the same model, in order of _date.

    _from = datalist[0]
    _to = datalist[len(datalist) - 1]

    val1 = date_cost(datalist) # cost one bx one. [x[data1._date, ...], y[data1.cost, ...]]
    val2 = [] # week_avg(val1) # weekly average
    val3 = [] # month_avg(val1) # monthly average

    return Graph(_from.model, _from._date, _to._date, val1, val2, val3)

def date_cost(datalist):

    y = x = []

    for d in datalist:
        
        x.append(_formatter(d._date))
        y.append(d.cost)

    return [x, y]

def _formatter(l):
    
    
    return 


#def week_avg(l): # l = val1 = [x[data1._date, ...], y[data1.cost, ...]]

    


#def sort_by_date(datalist): # of the model.



#con = sqlite3.connect("../for_trx-selenium/db.db")
#cur = con.cursor()
