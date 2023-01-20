import sqlite3
    
def save(l): # l = list of data.
    
    if len(l) == 0: return

    for o in l:

        try: _save(o)
        except: print("save error", o._date, o.title, o.cost, o.gb, o.distributor)

def _save(o): 
    
    con = sqlite3.connect("../for_try-selenium/db.db")
    cur = con.cursor()
    
    model = o.model
    _date = o._date
    date = _formatter(_date)
    title = o.title
    link = o.link
    price = o.price
    fee = o.fee
    cost = o.cost
    gb = o.gb
    distributor = o.distributor
    
    # drop the repeated ones.
    res = cur.execute("SELECT _date, title, price, gb FROM crawler WHERE _date = ? AND title = ? AND price = ? AND gb = ?", (_date, title, price, gb))
    if len(res.fetchall()) == 0:
        cur.execute("INSERT INTO crawler(model, date, _date, title, link, price, fee, cost, gb, distributor) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (model, date, _date, title, link, price, fee, cost, gb, distributor))
        con.commit()
    # to exclude the repeated and save the right model, 
    # let for ex. "0000ti" goes be4 "0000", "1111s" be4 "1111" in keywords.        
    cur.close()
    con.close()

def _formatter(dd): # 'Verkauft 17. Dez 2022' -> '2022.12.17'. An insurance.
    
    temp = dd.replace('Verkauft ', "").replace(' Jan ', '1.').replace(' Feb ', '2.').replace(' Mär ', '3.').replace(' Apr ', '4.').replace(' Mai ', '5.').replace(' Jun ', '6.').replace(' Jul ', '7.').replace(' Aug ', '8.').replace(' Sep ', '9.').replace(' Okt ', '10.').replace(' Nov ', '11.').replace(' Dez ', '12.')
    l = temp.split(".")
    l.reverse() # alters l self and must be alone standing. 
    ll = []
    for ele in l:
        
        if len(ele) == 1: ll.append("0" + ele)
        else: ll.append(ele)

    return ".".join(ll)