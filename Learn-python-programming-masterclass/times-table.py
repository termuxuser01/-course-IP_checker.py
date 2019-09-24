with open('times_tables.txt', 'w') as f:
  for i in range(1, 13):
    for m in range(1, 13):
      f.write("{} times {} is {}\n".format(i, m, i * m))
