import sqlite3

con = sqlite3.connect("../for_try-selenium/db.db")
cur = con.cursor()
    
def save(l): # l = list of data.
    
    if len(l) == 0:
        return
    for o in l:
        _save(o)

def _save(o): # drop the repeated ones.
    
    model = o.model
    _date = o._date
    title = o.title
    link = o.link
    price = o.price
    fee = o.fee
    cost = o.cost
    gb = o.gb
    distributor = o.distributor
    
    res = cur.execute("SELECT _date, title, price, gb FROM crawler WHERE _date = ? AND title = ? AND price = ? AND gb = ?", (_date, title, price, gb))
    if len(res.fetchall()) == 0:
        cur.execute("INSERT INTO crawler(model, _date, title, link, price, fee, cost, gb, distributor) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (model, _date, title, link, price, fee, cost, gb, distributor))
    
    con.commit()
    cur.close()
    con.close()