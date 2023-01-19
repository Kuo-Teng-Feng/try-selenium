import sqlite3

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

def sort_from_db_by_date(model, _from, _to, gb, distributor): # return id list abstracted from db.db

    con = sqlite3.connect("../for_try-selenium/db.db")
    cur = con.cursor()
    
    com = f"SELECT id FROM crawler WHERE model = '{model}'" # ' in " necessary for str.!
    if gb != 0:
        com += f' AND gb = {gb}'
    if distributor != "":
        com += f" AND distributor = '{distributor}'" # ' in " necessary for str.!
    com += f" AND date >= '{_from}' AND date <= '{_to}' ORDER BY date" # ' in " necessary for str.!

    res = cur.execute(com)
    l = res.fetchall() # element in this list is always tuple.
    cur.close()
    con.close()
    
    ll = []
    for ele in l:
        ll.append(ele[0])

    return ll # id list.

#print(sort_from_db_by_date("GPU 2080ti", "2023.01.01", "2023.01.19", 0, ""))