import sqlite3
import math
import matplotlib.pyplot as P
from data import data

class Graph:

    def __init__(self, model, begin, end, val1, val2, val3):

        self.model = model
        self.begin = begin
        self.end = end
        self.val = [val1, val2, val3] # [[[y1, y2....], [x1, x2...]], [], []]

    def draw(self):



def graphify(datalist): # of the same model, in order of _date.

    _from = datalist[0]
    _to = datalist[len(datalist) - 1]

    val1 = date_cost(datalist) # cost one by one. [y[data1._date, ...], x[data1.cost, ...]]
    val2 = week_avg(val1) # weekly average
    val3 = month_avg(val1) # monthly average

    return Graph(_from.model, _from._date, _to._date, val1, val2, val3)

def date_cost(datalist):

    x = y = []

    for d in datalist:
        
        y.append(d._date)
        x.append(d.cost)

    return [y, x]

def week_avg(l): # l = val1 = [y[data1._date, ...], x[data1.cost, ...]]

    dates = l[0]
    costs = l[1]
    n = math.floor(len(dates) / 7)

    wa = {}
    for i in range(0, n)


def sort_by_date(datalist): # of the model.



con = sqlite3.connect("../for_try-selenium/db.db")
cur = con.cursor()
