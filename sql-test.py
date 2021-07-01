import sqlite3

con = sqlite3.connect('db.sqlite')

con.execute("INSERT INTO cards (number, name, date, cvc) VALUES (?, ?, ?, ?)",
            ("1111 2222 3333 4444", "Vasya Ivanov", "02/25", 425))
result = con.execute("SELECT * FROM cards")

for row in result:
    print(row)

con.commit()
con.close()