counter = 0
from timeit import default_timer as timer
start = timer()
for i in range(11111111111111, 99999999999999+1):
    if counter % 10000000000000 == 1:
        print(i)
    counter +=1
print(counter)
print(timer()-start)