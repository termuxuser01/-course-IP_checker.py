entries = range(1, 6)

#returns true because all values are true
print("all: {}".format(all(entries)))
#returns true because at least on value is true
print("any: {}".format(any(entries)))

#iterable with one false value
entries2 = [1, 2, 3, 4, False]

#returns false because not all values are true
print("all: {}".format(all(entries2)))
#returns true because at least on value is true
print("any: {}".format(any(entries2)))
