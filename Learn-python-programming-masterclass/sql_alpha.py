import sqlite3
from string import ascii_lowercase as lw
from string import ascii_uppercase as up

db = sqlite3.connect("alpha.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS  alpha (id INTEGER, name TEXT);")
db.execute("CREATE TABLE IF NOT EXISTS upper_alpha (id INTEGER, letteru TEXT);")

UPDATE_DB = "INSERT INTO alpha VALUES( ?, ?);"
update_cursor = db.cursor()

for t in zip(range(26), lw):
  update_cursor.execute(UPDATE_DB, t)

UPDATE_DB = "INSERT INTO upper_alpha VALUES( ?, ?);"

for t in zip(range(26), up):
  update_cursor.execute(UPDATE_DB, t)

db.commit()

for id, letter, letteru in db.execute("SELECT alpha.id, alpha.name, upper_alpha.letteru FROM alpha INNER JOIN upper_alpha ON alpha.id = upper_alpha.id;"):
  print("id: ", id)
  print("letter: ", letter)
  print("uppercase: ", letteru) 
  print("-" * 40)

db.close()
