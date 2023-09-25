import time
from time import perf_counter as timer
import random

timestart = input("Enter the {start} key to start")

time.sleep(random.randint(1,6))

starttime = timer()
timend = input("Enter any key to end")
endtime = timer()
timespan = endtime - starttime
print(f"The timespan is {timespan}")
starttime= time.strftime("%X",time.localtime(starttime))
endtime= time.strftime("%X", time.localtime(endtime))


print(f"The start time is {starttime}")
print(f"The end time is {endtime}")
print(f"The timespan is {timespan}")

