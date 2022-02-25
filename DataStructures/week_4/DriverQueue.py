import Queue, psutil 

Packages = Queue.Queue()
print(Packages.is_empty()) # true, we just created it
Packages.enqueue('lamp')
Packages.enqueue('puzzle')
Packages.enqueue('television')
print(Packages)
print(Packages.dequeue()) 
print(Packages.size()) 

process_list = psutil.pids() 
Processes = Queue.Queue()
print('My number of processes is {}'.format(Processes.size()))
for process in process_list:
    if process % 2 == 0: # even
        Processes.enqueue(process)
print('My number of even processes is {}'.format(Processes.size()))
print(Processes)
print("My first task is {}".format(Processes.dequeue()))
