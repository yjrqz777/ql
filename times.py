import datetime
import time


t = time.time()
t=int(t)

print (t) #秒级时间戳

stamp =1683597594
print(stamp)

times=datetime.datetime.fromtimestamp(stamp)
print(times)