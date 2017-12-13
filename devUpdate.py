'''Write a function vowels() that takes a string as argument and returns the number of vowels.
Note: The function has to deal with both lowercase and uppercase characters.
// vowels("hello, world!") >> 3
// vowels("HELLO, WORLD!") >> 3'''
def vowels(text):
   thevowels, n, c, som = "aeiouyAEIOUY", 1, 0, 0 
   while n <= len(text):
      n, c, b, k, a = n+ 1, 1+c, text[c], 0, 1
      while a <= len(thevowels):
         k, a, z = k + 1, a + 1, b.find(thevowels[k])
         if z >= 0:
            som=som+1
   return (str(som))     
print (vowels("helalo, world!"))#>> 4
print (vowels("HELAiLO, WORLD!"))#>> 5 

def vowels(text):
   thevowels, sumVowels = "aeiouAEIOU", 0
   for i in text : sumVowels +=1 if i in thevowels else 0
   return (sumVowels)
print (vowels("hello, world!"))#>> 3
print (vowels("helalo, world!"))#>> 4
print (vowels("HELAiLO, WORLD!"))#>> 5
