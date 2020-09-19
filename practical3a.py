# Perform Stack operations using Array implementation.


class ArrayStack:
    
    def __init__(self):
        self._data = []
        
    def display(self):
        print(self._data)
        
    def is_empty(self):
        '''checks if stack is empty'''
        return len(self._data) == 0
    
    def push(self, value):
        self._data.append(value)
        
    def pop(self):
        '''pops value - last vala 4 in above list - (-1 element)'''
        if not self.is_empty():
            return self._data.pop()
        else:
            raise Exception('Stack is empty')

a1 = ArrayStack()
a1.push(2)
a1.push(4)
a1.push(6)
print("After push() ")
a1.display()

print("After pop() ")
a1.pop()
a1.display()


