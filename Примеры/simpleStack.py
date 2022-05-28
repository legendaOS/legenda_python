class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, value):
        if self.head is None:
            buf = Node(value, None)
            self.head = buf
        else:
            buf = Node(value, self.head)
            self.head = buf
            
    def pop(self):
        if self.head is None:
            return None
        else:
            if self.head.prev is None:
                buf = self.head.value
                self.head = None
                return buf
            else:
                buf = self.head.value
                self.head = self.head.prev
                return buf
                
                
                
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop()) #3
print(s.pop()) #2
print(s.pop()) #1
print(s.pop()) #None