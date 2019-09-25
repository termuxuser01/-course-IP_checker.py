import time
from time import time as my_timer
import random

input("press enter to start: ")

time.sleep(random.randint(1,6))
start_time = my_timer()

input("press enter to stop: ")

end_time = my_timer()

print("you started at: " + time.strftime('%X', time.localtime(start_time)))
print("and ende at: " + time.strftime('%X', time.localtime(end_time)))

print('you scored {}'.format(end_time - start_time))
