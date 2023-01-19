import sqlite3
from save import _formatter

con = sqlite3.connect("../for_try-selenium/db.db")
cur = con.cursor()
#cur.execute("CREATE TABLE crawler(id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, _date TEXT, title TEXT, link TEXT, price REAL, fee REAL, cost REAL, gb INTEGER, distributor TEXT)")
#cur.execute("CREATE TABLE date(date INTEGER, monthname TEXT, month INTEGER, year INTEGER)")
#cur.execute("DROP TABLE date")
#cur.execute("ALTER TABLE preorder ADD phone")
#cur.execute("INSERT INTO crawler(model, _date, title, link, price, fee, cost, gb, distributor) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (, , , , , , , , ))

#res = cur.execute("SELECT _date FROM crawler")
#_dates = res.fetchall()

#for d in _dates: # d is tuple.

#    dd = d[0] 
#    cur.execute("UPDATE crawler SET date = ? WHERE _date = ?", (_formatter(dd), dd))
#    con.commit()

#cur.execute("UPDATE now_product SET num = ? WHERE id = ?", (50, 1))
#cur.execute("DELETE FROM crawler WHERE id > 0")
#cur.execute("ALTER TABLE crawler ADD date TEXT")
#con.commit()
#res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(res.fetchone())
#print(res.fetchall())
res = cur.execute("SELECT model, date, _date, title, cost, gb, distributor FROM crawler WHERE gb > ? AND id > ? ORDER BY date", (0, 590))
#res = cur.execute("SELECT id FROM crawler")
print(res.fetchall())
cur.close()
con.close()
