import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    runtime = time.clock() - start
    return str(runtime) #result, 


def spin_loop(n):
    i = 0
    while i < n :
        i = i + 1
    return i
    
print (  time_execution( spin_loop(10) )  )
