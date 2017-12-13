def primer_number(num):
   for i in range(2, num + 1):
        if num%i == 0 :
         	break
   return (str(num)+' is a prime number') if i == num or num  == 2 else (str(num)+' is not a prime number ')
print (primer_number(int(input('Enter your number : '))))