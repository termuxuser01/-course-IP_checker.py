def fibo():
  current, previous = 0, 1
  while True:
    yield current
    current, previous = current + previous, current

fib = fibo()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
