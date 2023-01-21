import sqlite3

def call():
    
    model = input("Model (keyword): ").strip()
    _begin = input("from (yyyymmdd Ex. 20230203 instead of 23.2.3): ").strip()
    _end = input("to (inclusive): ").strip()
    gbstr = input("? Gigabyte (empty for no specification): ").strip()
    distributor = input("distributor (empty for no specification): ").strip()

    gb = 0
    try: gb = int(gbstr)
    except: pass

    if "." not in _begin and " " in _begin: begin = _begin.replace(" ", ".")
    elif "." not in _begin: begin = _begin[:4] + '.' + _begin[4:6] + '.' + _begin[6:]
    else: begin = _begin

    if "." not in _end and " " in _end: end = _end.replace(" ", ".")
    elif "." not in _begin: end = _end[:4] + '.' + _end[4:6] + '.' + _end[6:]
    else: end = _end
    
    return {'model' : model, 'begin' : begin, 'end' : end, 'gb' : gb, 'distributor' : distributor}

def sort_from_db_by_date(model, _from, _to, gb, distributor): # return id list abstracted from db.db

    con = sqlite3.connect("../for_try-selenium/db.db")
    cur = con.cursor()
    
    com = f"SELECT id FROM crawler WHERE model LIKE '{model}'" # ' in " necessary for str.! Vaguer: '{model}%'.
    if gb != 0: com += f' AND gb = {gb}'
    if distributor != "": com += f" AND distributor LIKE '{distributor}'" # ' in " necessary for str.!
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