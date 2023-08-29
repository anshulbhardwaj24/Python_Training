import threading
import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, 5, self.counter)
#       print ("Exiting " + self.name)

# def print_time(threadName, counter, delay):
#    while counter:
#       if exitFlag:    
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1

# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()

# print ("Exiting Main Thread")




# synchronization in thrreads
class myThread (threading.Thread):
   def __init__(self, threadID, name, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
   def run(self):
      print( "Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.delay, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(1, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")
