def odd():
  start = 1
  while True:
    yield start
    start += 2

def lieb():
  result = 1
  op = 0
  od = odd()
  
  while True:
    if op == 0:
      result -= 1/next(od)
      print("odd number: {}".format(od))
      op = 1
      yield result
    else:
      result += 1/next(od)
      yield result
      print("odd number: {}".format(od))
      op = 0

lie = lieb()

print(next(lie))
print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie))

print(next(lie) * 4)
