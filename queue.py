class Queue(object):

    def __init__(self):
        self.my_queue = []

    def enqueue(self,item):
        self.my_queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print "queue empty"
            raise Exception('Queue is empty!')
        else:
            val = self.my_queue[0]
            del self.my_queue[0]
        return val

    def is_empty(self):
        return self.my_queue == []

    def size(self):
        return len(self.my_queue)

    def __repr__(self):
        return str(self.my_queue)


if __name__ == '__main__':
    q=Queue()
    print "Add: 10"
    q.enqueue(10)
    print "Add: 20"
    q.enqueue(20)
    print "Queue:", q
    print "Size:", q.size() 
    print "dequeue:", q.dequeue()
    print "Queue:", q