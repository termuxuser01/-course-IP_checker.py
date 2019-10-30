menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
 
for meal in menu:
    if "spam" not in meal:
        print(meal)

spam_meal = [meal for meal in menu if "spam"  in meal]
print(spam_meal)

#spam or eggs can contain bacon and sausage as long as they are not together

fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal if not ("spam" in meal and "sausage" in meal)]

print(fussy_meals)

else_list =  []
for meal in menu:
    if "spam" not in meal:
        else_list.append(meal)
    else:
      else_list.append("meal was skipped")

print("-" * 40)

print(else_list)

x = "vianney"

expresion = "my love" if x == "vianney" else "bitch"

print(expresion)

print("*" * 50)

else_list =  []
for meal in menu:
    if "spam" not in meal:
        else_list.append(meal)
    else:
      else_list.append("meal was skipped")

#do the same as for loop

nw = [meal if "spam" not in meal else "meal was skipped" for meal in menu]
print(nw)
