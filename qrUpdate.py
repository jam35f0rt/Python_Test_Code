def diff(a):
   square,add =0,0
   for x in range( a+1 ): add, square = add + x, square + (x*x)
   return (-square + (add*add))
print (diff(10))
