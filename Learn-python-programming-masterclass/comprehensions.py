#return square of numbers to list the old fashion way

l1 = [1, 2, 3, 4, 5, 6]
sqr = []
str1 = "hello"

for l in l1:
  sqr.append(l ** 2)

print(sqr)

square = [l ** 2 for l in l1]

print(square)

str2 = [s * 3 for s in str1]

print(str2)

text = "what have the romans ever done for us?"

upperc = [s.upper() for s in text]

print(''.join(upperc))

#dont do this this is very expensive
words = [w for w in text.split()]

print(words)

words2 = text.split(' ')

print(words2)
