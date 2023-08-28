
import threading
from time import sleep
import time

# Global Variables
n = 0
flag = False
""" flag = False
n = 0

def p(): 
    global flag, n
    sleep(0.2)
    while not flag:
        n = 1 - n
        
def q(): 
    global flag, n
    sleep(0.2)
    while n==0:
        pass
    flag = True
    
proc1 = threading.Thread(target=p)
proc2 = threading.Thread(target=q)

proc2.start()
proc1.start()

proc1.join()
proc2.join()

print(n)
print(flag)
 """

