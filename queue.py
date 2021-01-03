class Queue:
    
    def __init__(self):
        self.queue = []
    
    def queueup(self,val):
        if len(self.queue) == 0:
            self.queue.append(val)
        else:
            self.queue+=[0]
            for i in range(len(self.queue)-1,-1, -1):
                print(self.queue)
                self.queue[i] = self.queue[i-1]
            self.queue[0] = val

    def dequeue(self):
        return self.queue.pop()

myQueue = Queue()
myQueue.queueup(1)
myQueue.queueup(2)
myQueue.queueup(3)
myQueue.queueup(4)
myQueue.queueup(5)
print(myQueue.queue)
print(myQueue.dequeue())
print(myQueue.queue)


        