class Stack(object):
    def __init__(self):
        self.stack_list = []

    def push(self,val):
        self.stack_list.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            val = self.stack_list[-1]
            del self.stack_list[-1]
            return val

    def is_empty(self):
        return len(self.stack_list) == 0

    def __repr__(self):
        return str(self.stack_list)

if __name__ == '__main__':
	s=Stack()
	print "Push: 10"
	s.push(10)
	print "Push: 20"
	s.push(20)
	print "Stack:", s
	print "pop:", s.pop()
	print "Stack:", s
	