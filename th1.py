import threading

def sum1():
    answer = 0
    for i in range(1,10**8):
        answer+=i
    print('thread_name:', threading.currentThread().getName())    
    print('sum1 = ', answer)    

def sum2():
    answer = 0
    for i in range(1,100):
        answer+=i
    print('thread_name:', threading.currentThread().getName())    
    print('sum2 = ', answer) 


sum_1 = threading.Thread(target=sum1, name='sum_1')
sum_2 = threading.Thread(target=sum2, name='sum_2')

sum_1.start()
sum_2.start()