import threading
import time

def get_info_1(name, age, job):
    time.sleep(4)
    thread_name = threading.currentThread().getName()
    print(f"{name} | {age} | {job} --> {thread_name}")

def get_info_2(name, age, job):
    time.sleep(4)
    thread_name = threading.currentThread().getName()
    print(f"{name} | {age} | {job} --> {thread_name}")

get_info_1("armin", 18, "developer")
get_info_2("aylin", 19, "doctor")