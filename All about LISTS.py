'''
# Unordered list
l1=[1,'Apple',12.93]

# NEGATIVE INDEXING
print(l1[-2])  #Output is Apple (SECOND LAST ELEMENT)


# Ordered list
l2=[1,2,3,4,5,6,7]

# ACCESSING LISTS
print(l2[3])   #Output is 4


x=['a',"b","c","d","e"]
#   0   1   2   3   4    ----> INDEX OF EACH ELEMENT IN THE LIST

#SLICING LISTS
print(x[  1  :  4  :  1  ])
# list[ start: stop : step ]
#i.e...slicing from index 1 to 3
print(x[:3])
print(x[::-1])



#LISTS are MUTABLE meaning "You can MODIFY the CONTENT in lists"
y=[1,2,3,4,5]

y.append(4)  # APPEND: to add an element to the end of the list
print(y)

y[1]=12 # to change the second element( index 1) from 2 to 12
print(y)

y.insert(4,14)# to insert an element 14 at
print(y)      # a specific index 4 (in the position of ELEMENT 5)

y.remove(4)    # To remove the first occurrence of the element 4
print(y)

# Here the element in hte position of index 0
s=y.pop(0) # By default last element is removed and returned
print(s)  #Element removed is 1( index 0 )

# to remove the element by its index
del y[1] # Element removed is 3( index 1 )
print(y)


#Concatenation of 2 lists
x=[1,2,3]
y=[4,5,6]
l=x+y
print(l)


#Repetition
x=[1,2,3,4,5,6]
z=x*3
print(z)


# Membership testing
x=[1,2,3]
print(2 in x)  #Output: True
print(5 in x)   #Output: False


#List's Operations

# 01.extend() : to extend a list to the main list
x=[1,2,3]
x.extend([4,5,6])
print(x)

# 02. clear(): to remove all elements from a list
x = [1,2,3]
x.clear()
print(x)

# 03. index() : to find out the index of given element
q=[1,2,3]
print(q.index(2)) #output: 1


# 04.count(): to find no. of occurrences of that element
w=[1,2,2,2,3]
print(w.count(2))


# 05. sort(): By default key=None and [  Reverse= False  ]
x=[6,3,1,0,5]
x.sort()   # By default , sorting is done in ascending order
print(x)
x.sort(reverse=True)
print(x)


#06. reverse(): Only reverses the elements of the list
x=[4,2,0]
x.reverse()
print(x)

#List Comprehensions
z=[x for x in range(20) if x%2!=0]
print(z)

# Nested lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2]) #Output: 6


# Iterating through lists
x=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in x:
    print(i , sep='  ' , end="     ")
'''

def pass_fail(score):
    if score>=50:
        print("Passed")
    else:
        print("Failed")
score=int(input('?'))
pass_fail(score)









