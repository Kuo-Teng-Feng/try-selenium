import sqlite3

def call():
    
    model = "GPU " + input("Model(num and chr): ").strip()
    begin = input("from (dd.mm.yyyy Ex. 2.3.2023 instead of 02.03.2023): ").strip()
    end = input("to: ").strip()
    gbstr = input("? Gigabite (empty for no specification): ").strip()
    gb = 0
    try:
        gb = int(gbstr)
    except:
        pass
    distributor = input("distributor (empty for no specification): ").strip()
    
    return {'model' : model, 'begin' : begin, 'end' : end, 'gb' : gb, 'distributor' : distributor}

def sort_by_date(model, begin, end, gb, distributor):

    con = sqlite3.connect("../for_trx-selenium/db.db")
    cur = con.cursor()
    
    com = f"SELECT id FROM crawler WHERE model = {model}"
    if gb != 0:
        com += f' AND gb = {gb}'
    if distributor != ""
        com += f' AND distributor = {distributor}'

    
    res = cur.execute(com)

    
    cur.close()
    con.close()