def list_01 (l):
   b='No'
   for i in range (1,len(l)):
      for j in range (1,len(l)):
          if l[i]=l[j]:
             b='Yes'
   return (b)

class rectangle:
   def _init_(self, list_of_dots = []):
      self.dots = list_of_dots
   def square(self):
      return (self.dots[2,1]-self.dots[1,1])*(self.dots[2,2]-self.dots[1,2])
   def perimetr(self):
      return 2*(self.dots[2, 1] - self.dots[1, 1]) + (self.dots[2, 2] - self.dots[1, 2])