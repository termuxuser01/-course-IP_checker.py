menu = []
menu.append(["egg", "bacon", "spam"])
menu.append(["sausage", "egg", "bacon", "ham"])
menu.append(["spam", "egg", "bacon"])
menu.append(["ham", "sausage", "bacon"])
menu.append(["spam", "egg", "bacon"])
menu.append(["spam", "egg", "spam"])
menu.append(["ham", "bacon", "cheese"])

m = 0

for meal in menu:
  i = 0 
  m += 1
  if not "spam" in meal:
    print("meal number {}".format(m))
    for ingredient in meal:
      i += 1
      print("ingredient {} is {}".format(i, ingredient))
