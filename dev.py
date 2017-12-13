"""Write a function vowels() that takes a string
as argument and returns the number of vowels.
Note: The function has to deal with both
lowercase and uppercase characters.
// vowels("hello, world!") >> 3
// vowels("HELLO, WORLD!") >> 3
"""

"""The code i suppose write with the lessons 1 to 2.5"""

def vowels(text):
   n, som = 0, 0
   while n < len(text) :
      a = 0
      b = text[n]
      while a < 12:       # len("aeiouyAEIOUY")  == 12
         z = b.find("aeiouyAEIOUY"[a])
         if z >= 0 :
            som += 1
         a = a +1
      n = n + 1
   return som

"""Here is the code of my skills """

def vowelsJames(text):
   sumVowels = 0
   for i in text :
      sumVowels +=1 if i in 'aeiouyAEIOUY' else 0
   return sumVowels

def vowelsAdvance(text):
   return sum([ 1 for char in text if char in 'aeiouyAEIOUY' ])


print (vowelsAdvance("") , vowels("") , vowelsJames(""))#>> 0 0 0
print (vowelsAdvance(" ") , vowels(" ") , vowelsJames(" "))#>> 0 0 0
print (vowelsAdvance("Y Y") , vowels("Y Y") , vowelsJames("Y Y"))#>> 2 2 2
print (vowelsAdvance("hello, world!") , vowels("hello, world!") , vowelsJames("hello, world!"))#>> 3 3 3
print (vowelsAdvance("HELLiO, WORLD!") , vowels("HELLiO, WORLD!") , vowelsJames("HELLiO, WORLD!"))#>> 4 4 4
print (vowelsAdvance("hellaoo, world!") , vowels("hellaoo, world!") , vowelsJames("hellaoo, world!"))#>> 5 5 5
print (vowelsAdvance("HELLAO, IIWORLD!") , vowels("HELLAO, IIWORLD!") , vowelsJames("HELLAO, IIWORLD!"))#>> 6 6 6
 