import sqlite3
import matplotlib.pyplot as P
from save import _formatter #'Verkauft 17. Dez 2022' -> '2022.12.17'.
from caller import call, sort_by_date

class Graph:

    def __init__(self, model, begin, end, val1, val2, val3):

        self.model = model
        self.begin = begin
        self.end = end
        self.val = [val1, val2, val3] # [[[x1, x2....], [y1, y2...]], [], []]

    def draw(self):

        val = self.val
        P.plot(val[0][0], val[0][1], linestyle = "", marker = ".", color = "darkblue", ms = 13)
        P.xlabel(f"{self.begin} ~ {self.end}", fontsize = 10)
        P.ylabel("final price", fontsize = 10)
        P.title(self.model, fontsize = 16)
        P.show()

g = Graph("test", "begin", "end", [[1,1,2,3,4,4,6,7], [2,5,4,6,8,9,3,7]], [], [])
g.draw()

# with sql
conditions = call() # {'model' : model, 'begin' : begin, 'end' : end, 'gb' : gb, 'distributor' : distributor}
sort_by_date(conditions['model'], conditions['begin'], conditions['end'], conditions['gb'], conditions['distributor'])


    
# with class data as datalist
def graphify(datalist): # of the same model, sort first by ._date with sql.

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

#def week_avg(l): # l = val1 = [x[data1._date, ...], y[data1.cost, ...]]

#if __name__ == '__main__':
    
    