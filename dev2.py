def deference(num):
   i,summ,prod=1,0,0
   while i<=num:
      prod=prod+i
      summ=summ+i*i
      i =i+1
   return (-summ+(prod*prod))
print (deference(5))