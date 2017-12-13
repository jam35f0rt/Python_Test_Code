def perfect_number(num,som):
   for i in range(1,num):
      if num%i==0:
         som += i
   return ('perfect is '+ str(num)) if som==num or num==1 else ('not perfect is '+str(num))
print ( perfect_number(int(input('Please enter your number : ')),0) )

