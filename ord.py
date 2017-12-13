print ( ord(chr(5)) )
print (ord('a'))
print ( 12*[0] )

data = {'a':1,'b':20,'c':50,'d':9}
print (data)
print (max(data.values()) ) #50
print (max([i for i in data.values()]) ) #50
print(max(data.items(), key=lambda k: k[1])) #('c', 50)
print(data[max(data, key=data.get)]) #50
print(max(data, key=data.get)) #c

print ('************')
verification = None
verification = verification or []
verification.append(data)
verification = None
print (verification)
print ('************')

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    '''a = []
    for w in keyword:
        a.append(ord(w))
    return sum(a)%buckets''' 

    return sum([ ord(w) for w in keyword ])%buckets

table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print ('lenght of the table is '+ str(len(table)))

print (hash_string('a',12))
#>>> 1

print (hash_string('Andy',5))

print (hash_string('b',12))
#>>> 2

print (hash_string('a',13))
#>>> 6

print (hash_string('au',12))
#>>> 10

print (hash_string('udacity',12))
#>>> 11
