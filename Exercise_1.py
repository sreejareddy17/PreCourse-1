# Time Complexity : O(1)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :
class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
       self.s = []
         
     def isEmpty(self):
       return len(self.s)==0
         
     def push(self, item):
       self.s.append(item)
         
     def pop(self):
        self.s.pop()
        
     def peek(self):
       if self.s:
         return self.s[-1]
      else:
        return None
      
     def size(self):
       return len(self.s)
         
     def show(self):
       return self.s
         

s = myStack()
s.push('1')
s.push('2')
print(s.peek())
print(s.size())
print(s.pop())
print(s.show())
