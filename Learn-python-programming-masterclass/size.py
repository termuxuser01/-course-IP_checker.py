import sys

def myrange(n: int):
  print("my ranges starts")
  start = 0 
  while start <= n:
    print(f"my range is returning {start}")
    yield start
    start += 1

#_ = input("line 11") 
#big_range = range(1000)
big_range = myrange(10)
#_ = input("line 13")
#this will make the first value appended to big_list to be '1'
print(next(big_range))
#print(sys.getsizeof(big_range))

big_list= []

#_ = input("line 20")
for s in big_range:
  big_list.append(s)
 # _ = input("line 23")
  # this allows you to see each time the generator is called



#print(sys.getsizeof(big_list))

print(big_range)
print(big_list)

print("looping again or not")

for i in big_range:
  print(i)
