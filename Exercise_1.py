# implementing stack as an array
# TC = O(1)
# SC = O(n)


class myStack:

  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file


     def __init__(self):
      self.arr = []
      self.size = 0
         
     def isEmpty(self):
      return self.size ==0

         
     def push(self, item):
      self.arr.append(item)
      self.size+=1
         
     def pop(self):
      if self.isEmpty():
        raise "Stack Empty"
      self.size-=1
      return self.arr.pop()
  
     def peek(self):
      if self.isEmpty:
        raise "Stack Empty"
      return self.arr[-1]

        
     def size(self):
      return self.size
         
     def show(self):
      return self.arr
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
