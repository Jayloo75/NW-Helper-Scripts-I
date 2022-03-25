import sqlite3

conn = sqlite3.connect('db/resources.db')

c = conn.cursor()



c.execute("""CREATE TABLE scans (
            resource_id INTEGER,
            price real NOT NULL,
            quantity real NOT NULL,
            timestamp  NOT NULL
            )""")

# c.execute("""DROP TABLE resources""")








# c.execute("""CREATE TABLE resources (
#             id INTEGER PRIMARY KEY,
#             name varchar(20) NOT NULL,
#             image_name varchar(20) NOT NULL,
#             searchable_name varchar(20) NOT NULL
#             )""")

# c.execute("""DROP TABLE resources""")

tp_items = [
    ["Oil", "oil.png", "oil"],
    ["Green Wood", "green-wood.png", "green w"],
    ["Charcoal", "charcoal.png", "charc"],
    ["Iron Ore", "iron-ore.png", "iron o"],
    ["Starmetal Ore", "starmetal-ore.png", "starmetal o"],
    ["Orichalcum Ore", "orichalcum-ore.png", "orichalcum o"],
    ["Gold Ore", "gold-ore.png", "gold ore"],
    ["Silver Ore", "silver-ore.png", "silver ore"],
    ["Platinum Ore", "platinum-ore.png", "platinum ore"],
    ["Iron Ingot", "iron-ingot.png", "iron ing"],
    ["Steel Ingot", "steel-ingot.png", "steel ingo"],
    ["Starmetal Ingot", "starmetal-ingot.png", "starmetal in"],
    ["Orichalcum Ingot", "orichalcum-ingot.png", "orichalcum ing"],
    ["Silver Ingot", "silver-ingot.png", "silver ingo"],
    ["Gold Ingot", "gold-ingot.png", "gold ing"],
    ["Platinum Ingot", "platinum-ingot.png", "platinum Ing"]
    ]


# for item in tp_items:
#     c.execute("insert into resources (name, image_name, searchable_name) values (?, ?, ?)", item)


# c.execute("""INSERT INTO resources values (null, 'Oil', 'Oil')""")
# c.executemany("insert into resources (id, name, image_name, searchable_name) values (null, ?, ?, ?)", tp_items)
# c.executemany("insert into resources (name, image_name, searchable_name) values (?, ?, ?)", tp_items)

# conn.commit()

c.execute("SELECT * FROM resources")
rows = c.fetchall()
for row in rows:
    print(row)

# close the connection
c.close()



