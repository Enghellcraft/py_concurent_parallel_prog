import threading
from time import sleep
import time

# Global Variables
n = 0
flag = False

def trivialConcurrent2_1 () :
    
    def p() :
        global n
        k1 = 1
        n = k1
        print(f"Proceso p: n = {n}")
        
    def q() :
        global n
        k2 = 1
        n = k2
        print(f"Proceso q: n = {n}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start()
    
# trivialConcurrent2_1() 

def trivialSequential2_2() :
    k1 = 1
    k2 = 2
    
    def p() :
        global n
        time.sleep(0.8)
        n = k1
        print(f"Proceso p: n = {n}")
        
    def q() :
        global n
        n = k2
        print(f"Proceso q: n = {n}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start()

# trivialSequential2_2()
    
def atomicAssignment2_3() :
    
    def p() :
        global n
        time.sleep(0.8)
        n = n + 1
        print(f"Proceso p: n = {n}")
        
    def q() :
        global n
        n = n + 1
        print(f"Proceso q: n = {n}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start()   
    
# atomicAssignment2_3()

def statementWOneGlobalRef2_4() : 
    
    def p() :
        global n
        #time.sleep(0.8)
        temp = n
        n = temp + 1 
        print(f"Proceso p: n = {n}")
        
    def q() :
        global n
        temp = n
        n = temp + 1 
        print(f"Proceso q: n = {n}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start()    
    
# statementWOneGlobalRef2_4() 

def stopTheLoop2_5() :
    def p() :
        global n
        global flag
        while flag == False:
            n = 1 - n
            print(f"Proceso p: n = {n}, flag: {flag}")
        
    def q() :
        global n
        global flag
        flag = True
        print(f"Proceso q: n = {n}, flag = {flag}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start() 
    
# stopTheLoop2_5()

def statementRegisterMachine2_6() :
    def p() :
        global n
        r1 = n
        print(f"Before -> Proceso p: n = {n}")
        r1 = r1 + 1  
        n = r1
        print(f"After -> Proceso p: n = {n}")
        
    def q() :
        global n
        r1 = n
        print(f"Before -> Proceso q: n = {n}")
        r1 = r1 + 1  
        n = r1
        print(f"After -> Proceso q: n = {n}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start() 
    
# statementRegisterMachine2_6()

def volatileVariables2_8() :
    def p() :
        global n
        local1: int
        local2: int
        local1 = (n + 5) * 7
        local2 = n + 5
        print(f"Before -> Proceso p: n = {n}, local1 = {local1}, local2 = {local2}")
        n = local1 * local2
        print(f"After -> Proceso p: n = {n} local1 = {local1}, local2 = {local2}")
        
    def q() :
        global n
        local: int 
        print(f"Before -> Proceso q: n = {n}")
        local = n + 6
        print(f"After -> Proceso q: n = {n}, local = {local}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start() 
    
# volatileVariables2_8()

def concurrentCount2_9() :
    def p() :
        global n
        temp: int
        for i in range(10):
            temp = n
            sleep(0.8)
            n = temp + 1
            print(f"Step {i} -> Proceso p: n = {n}, temp = {temp}")

    def q() :
        global n
        temp: int 
        for i in range(10):
            temp = n
            sleep(0.8)
            n = temp + 1
            print(f"Step {i} -> Proceso q: n = {n}, temp = {temp}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start() 
    
# concurrentCount2_9()

def incrementignDecrementing2_10() :
    def p() :
        global n
        temp: int
        for i in range(10):
            temp = n
            sleep(0.8)
            n = temp + 1
            print(f"Step {i} -> Proceso p: n = {n}, temp = {temp}")

    def q() :
        global n
        temp: int 
        for i in range(10):
            temp = n
            sleep(0.8)
            n = temp - 1
            print(f"Step {i} -> Proceso q: n = {n}, temp = {temp}")
        
    proc1 = threading.Thread(target=p)
    proc2 = threading.Thread(target=q)
    
    proc1.start()
    proc2.start() 
    
# incrementignDecrementing2_10()

