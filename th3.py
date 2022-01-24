import threading
import time

def greeting():
    time.sleep(5)
    print('Hello :)')

daemon = threading.Thread(target=greeting, name='greet')
daemon.setDaemon(True)
daemon.start()
print('finished')
time.sleep(6)
print(daemon.is_alive()) 