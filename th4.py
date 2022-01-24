import threading
import time

def clean_home():
    time.sleep(3)

def clean_yard():
    time.sleep(4)

def invite_pepole():
    time.sleep(2)    

home = threading.Thread()
yard = threading.Thread()
invite = threading.Thread()
