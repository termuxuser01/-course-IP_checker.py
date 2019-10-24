import sqlite3
from string import ascii_lowercase as lw
from string import ascii_uppercase as up

db = sqlite3.connect("mylove.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS alpha (id INTEGER, letter TEXT);")
db.execute("CREATE TABLE IF NOT EXISTS upper_alpha (id INTEGER, letteru TEXT);")


update_db = "INSERT INTO alpha VALUES(?, ?);"

UPDATE_CURSOR = db.cursor()

for t in zip(range(1,27), lw):
  UPDATE_CURSOR.execute(update_db, t)

db.commit()
 
update_db = "INSERT INTO upper_alpha VALUES(?, ?);"

for t in zip(range(1,27), up):
  UPDATE_CURSOR.execute(update_db, t)

db.commit()  
  
for i, l, u in db.execute("SELECT alpha.id, alpha.letter, upper_alpha.letteru FROM alpha JOIN upper_alpha ON alpha.id = upper_alpha.id"):
  print(f'id: {i}\nletter: {l}\nuppercase: {u}')
  print("-" * 40)

db.close()
