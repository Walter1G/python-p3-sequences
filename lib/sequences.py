#!/usr/bin/env python3
def print_fibonacci(length):
    
    
    fibs = []
    if length == 0:
        print(fibs)
        return fibs
    
    a,b =0,1
    for _ in range(length):
        fibs.append(a)
        a,b = b,a+b
        
        
    print(fibs)
        
    # elif length ==1:  
    #     fibs.append(0)
    #     
    # elif length ==2:
    #     fibs.append(0)
    #     fibs.append(1)
    #     
        
    # if length > 2:
    #      print_fibonacci(length -1) + print_fibonacci(length-2)
         
    # 