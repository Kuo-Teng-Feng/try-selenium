import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()
#cur.execute("CREATE TABLE reviewXiao(id INTEGER PRIMARY KEY AUTOINCREMENT, keyword TEXT, date TEXT, _date TEXT, stars INTEGER, text TEXT, person TEXT)")
#cur.execute("DROP TABLE date")
#cur.execute("INSERT INTO crawler(model, _date, title, link, price, fee, cost, gb, distributor) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (, , , , , , , , ))

#res = cur.execute("SELECT _date FROM crawler")
#cur.execute("UPDATE now_product SET num = ? WHERE id = ?", (50, 1))
#cur.execute("DELETE FROM crawler WHERE id > 0")
#cur.execute("ALTER TABLE crawler ADD date TEXT")
#con.commit()
#res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
#res = cur.execute("SELECT id, keyword, _date, stars FROM reviewXiao WHERE id > ? AND date > ? ORDER BY date", (617, "2023.01.01"))
res = cur.execute("SELECT _date, date, stars, text FROM reviewXiao")
for t in res.fetchall():
    print("\n") 
    for ele in t: print(ele)
cur.close()
con.close()
