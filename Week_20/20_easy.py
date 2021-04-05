import datetime
import time
from os import system

while(True):
    now = datetime.datetime.now()
    current_time = now.strftime('%Y-%b-%d %H:%M:%S')
    print (current_time)
    time.sleep(1)
    system('clear')