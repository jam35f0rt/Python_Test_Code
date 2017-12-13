"""
Sum square difference description: 
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first
one hundrednatural numbers and the square of the sum
"""
"""The code i suppose  write with the lessons 1 to 2.5"""

def diff(a):
   x,square,add = 1,0,0
   while x <= a:
      square = square + (x*x)
      add = add + x
      x = x + 1
   return (add*add - square)
print (diff(100))

"""Here is the code of my skills """

def diffJames(a):
   sumSquare,add =0,0
   for x in range( a+1 ):
      add, sumSquare = add + x, sumSquare + (x*x)
   return (add*add  - sumSquare)
print (diffJames(100))
