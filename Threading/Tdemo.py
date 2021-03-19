import threading
from threading import *
import time
from random import randint

'''
#thread using method
def thread_function(name):
    print("Thread : starting", name)
    time.sleep(2)
    print("Thread : finishing", name)

print(threading.current_thread().getName())
x = threading.Thread(target=thread_function, args=("User Thread",))
x.start()
'''
'''
#thread by extending  class
class Tclass(Thread):
    def run(self):
        print("user thread is running")

print(threading.current_thread().getName()," is running")
t=Tclass()
t.start()
'''
'''
#Thread by using class
class Tclass:
    def disp(self):
        print("user thread is running")

print(threading.current_thread().getName()," is running")
t=Tclass()
x = threading.Thread(target=t.disp)
x.start()
'''

'''
#DeadLock
lock = Lock()
g = 0

def add_one():
   
   global g
   lock.acquire()
   g += 1
   lock.release()

def add_two():
   global g
   lock.acquire()
   g += 2
   lock.release()

threads = []
for func in [add_one, add_two]:
   threads.append(Thread(target=func))
   threads[-1].start()

for thread in threads:
   """
   Waits for threads to complete before moving on with the main
   script.
   """
   thread.join()

print(g)
'''

#wait and notify lock
class SomeItem:
  # init method
  def __init__(self):
    # initialize empty list
    self.list = []
  
  # add to list method for producer
  def produce(self, item):
    print("Adding item to list...")
    self.list.append(item)
    
  # remove item from list method for consumer
  def consume(self):
    print("consuming item from list...")
    item = self.list[0]
    print("Item consumed: ", item)
    self.list.remove(item)

def producer(si, cond):
    r = (randint(1,5))
    # creating random number of items
    for i in range(1, r):
      print("working on item creation, it will take: " + str(i) + " seconds")
      time.sleep(i)
      print("acquiring lock...")
      cond.acquire()
      try:
        si.produce(i)
        cond.notify()
      finally:
        cond.release()
      
def consumer(si, cond):
    cond.acquire()
    while True:
      try:
        si.consume()
      except:
        print("No item to consume...")
        # wait with a maximum timeout of 10 sec
        val = cond.wait(10)
        print(val)
        if val:
          print("notification received about item production...")
          continue
        else:
          print("waiting timeout...")
          break
        
    cond.release()
    
if __name__=='__main__':
  # condition object
  cond = threading.Condition()      #creates default lock
  # SomeItem object
  si = SomeItem()
  # producer thread
  p = threading.Thread(target=producer, args=(si,cond,))
  p.start()
  # consumer thread
  c = threading.Thread(target=consumer, args=(si,cond,))
  c.start()

  #print('Waiting for producer and consumer threads...')
  p.join()
  c.join()
  print("Done")
  