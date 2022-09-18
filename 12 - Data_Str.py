#Tuple: Set of DS immutable ordered
        #tuple is list w fixed order


my_tuple = ()
print(type(my_tuple))

thisTuple = ("apple","orange")
print(thisTuple)

thisTuple = ("apple",)
print(thisTuple)
print(type(thisTuple))

thisTuple = 2, 'city', 19.4
print(thisTuple)
print(type(thisTuple))

x, y, z = thisTuple   # tuple unpacking  also , , z
print(x)
print(y)
print(z)

print(thisTuple[0])     # 1st element of typle
print(thisTuple[1:])  # slicing

#thisTuple[0] = 6   # cant add like that or modify - not supp item assignment
thisTuple = 2, 'city', [3,45,9]
thisTuple[2][1] = 10
print(thisTuple)

newTuple = (1,2,2,2,3,4)
print(newTuple.count(2))   # how many time 2 value in tuple
print(newTuple.index(4))   # find index of value

print(3 in newTuple)    # check value in tuple 







#sets: unordered, mutable, value store only once,  DS - sequence of values, 

A = {1,2,3,3,3,4,5,6}  # value store multiple time only stored once
print(A)
B = {}
print(type(B))   # come as dictionary
B = set()       # define set empty
print(type(B))
B.add(7)
print(B)
B.update([8,9,10])
print(B)

B.discard(7)
print(B)
B.remove(8)
print(B)

B.discard(11)
print(B)

# B.remove(11)
# print(B)

A = {1,2,3,4,5,6}
B = {2, 6, 7, 8, 9}

print(A.intersection(B))  # common items
print(A & B)             

print(A.union(B))
print(A | B)

print(A.difference(B))
print(A - B)

print(B.difference(A))
print(B -A)

print(A.symmetric_difference(B))  # al items not in intersection
print((A.union(B)) - (A.intersection(B)))
print(A ^ B)





#dictionary  - Key value pair, 


my_dict = {}
print(type(my_dict))
d1 = {1:'cat', 2:'dog', 'name':'John'}
print(d1)
print(d1['name'])
print(d1[2])

d2 = dict([(1,'cat'),(2,'dog')])
print(d2)

print(d2[2])
print(d2.get(2))

x = d2.pop(2)
print(x)
print(d2)

d2['phone'] = 1234565

print(d2)

newDict = {'USA':'Washington DC', 'France':'Paris', 'Egypt':'Cairo', 'Germany': 'Berlin'}
print('USA' in newDict)
print('Paris' in newDict)
print(newDict.keys())
print('Egypt' in newDict)

print(newDict.items())
for item in newDict.items():
    print(item)

for i in newDict:
    print(i)

for i in newDict:
    print(newDict[i])


