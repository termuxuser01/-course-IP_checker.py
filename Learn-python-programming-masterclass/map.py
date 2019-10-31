import timeit

text = "i love veronica vianney contreras, shes nice"

capitals = [char.upper() for char in text]
print(capitals)

#using map
map_capitals = list(map(str.upper, text))
print(map_capitals)
print('-' * 50)

words = [word.upper() for word in text.split(' ')]
print(words)

#using map
map_words = list(map(str.upper, text.split(' ')))
print(map_words)
print('-' * 50)

#iterate a map

for x in map(str.upper, text):
  print(x)


setp = '''
text = "i love veronica vianney contreras, shes nice"
'''

mapper = '''
map_words = list(map(str.upper, text.split(' ')))
'''
comp = '''
words = [word.upper() for word in text.split(' ')]
'''
print("comprehension time: ", timeit.timeit(setup=setp, stmt=comp, number=10000))
print("map time: ", timeit.timeit(setup=setp, stmt=mapper, number=10000))
