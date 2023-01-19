import sqlite3
from save import _formatter #'Verkauft 17. Dez 2022' -> '2022.12.17'. An insurance.

def call():
    
    model = input("Model (keyword): ").strip()
    begin = input("from (yyyy.mm.dd Ex. 2023.02.03 instead of 23.2.3): ").strip()
    end = input("to (inclusive): ").strip()
    gbstr = input("? Gigabyte (empty for no specification): ").strip()
    distributor = input("distributor (empty for no specification): ").strip()

    gb = 0
    try:
        gb = int(gbstr)
    except:
        pass
    
    return {'model' : model, 'begin' : begin, 'end' : end, 'gb' : gb, 'distributor' : distributor}


def sort_by_date(model, begin, end, gb, distributor): # return id list abstracted from db.db

    _from = _formatter(begin)
    _to = _formatter(end)

    con = sqlite3.connect("../for_trx-selenium/db.db")
    cur = con.cursor()
    
    com = f"SELECT id FROM crawler WHERE model = {model}"
    if gb != 0:
        com += f' AND gb = {gb}'
    if distributor != ""
        com += f' AND distributor = {distributor}'
    com += f" AND date >= {_from} AND date <= {_to} ORDER BY date"
    
    res = cur.execute(com)
    l = res.fetchall() # element in this list is always tuple.
    cur.close()
    con.close()
    
    ll = []
    for ele in l:
        ll.append(ele[0])

    return ll # id list.