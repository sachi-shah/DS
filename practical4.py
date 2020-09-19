# Perform Queues operations using Circular Array implementation.


class ArrayQueue:

    
    default_len = 5 


    
    def __init__ (self):
        self._data = [None] * ArrayQueue.default_len
        self._size = 0
        self._front = 0
        
    def __len__ (self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception( "Queue is empty" )
            return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception( "Queue is empty" )
        answer = self._data[self._front]
        self._data[self._front] = None 
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        

    def resize(self, cap): 
        old = self._data 
        self._data = [None]*cap 
        walk = self._front
        for k in range(self._size): 
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

a = ArrayQueue()
a.enqueue(1)
a.enqueue(12)
print('After enqueue: ', a._data)

print('Deque : ',a.dequeue())
print('After Deque')
print(a._data)

print('Size : ',a._size)

a.enqueue(34)
a.enqueue(2)

print('After enqueue: ', a._data)

print('Size : ',a._size)

print('Deque : ',a.dequeue())
print('After Deque')
print(a._data)

print('Size : ',a._size)


