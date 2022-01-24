import threading
import time

def get_info_1(name, age, job):
    time.sleep(4)
    thread_name = threading.currentThread().getName()
    print(f"{name} | {age} | {job} --> {thread_name}")

def get_info_2(name, age, job):
    time.sleep(1)
    thread_name = threading.currentThread().getName()
    print(f"{name} | {age} | {job} --> {thread_name}")

# get_info('moahammad', 20, 'developer )
th_1 = threading.Thread(target=get_info_1, args=('mohammad',20, 'developer'), name='info1')

# get_info(name='mohammad', job='developer')
th_2 = threading.Thread(target=get_info_2, kwargs={'name': 'mohammad','age':19, 'job': 'ML'}, name='info2')

th_1.start()
th_2.start()