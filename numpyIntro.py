import numpy as np
#TERMINOLOGIES
#ndarry: a multidimensional array that has a fixed number of items and type (like arrayList in Java)
#0-D Array: elements of an array
#nested array: arrays with array elements
arr= np.array([1,2,3,4,5])
print(arr)

print(np.__version__)

#Creating a ndarry array (fixed type of elements)
#0-D: just elements
arr0 = np.array(1)
#1-D: Has 0-D elements as elements
arr1 = np.array((1,2,3,4,5))
#2-D: 2nd order tensor(array) with multiple arrays
arr2 = np.array([1,2,3,4], [1,2,3])
#3-D array: 2-D array as elements
arr3 = np.array( [[1,2,3],[1,2]],[[1,2,3,4], [2,3]] )

#check dimension of array

print(arr0.ndim) #should return 0

#Making n-dimensional arrays
arrn = np.array([1,2,3], ndmin = 5)
print("number of dimensions", arrn) # should use "+" to combine for lists


#Array Slicing 
#[startIndex: endIndex-1]
print(arr[1:5])#[1:5:1]
print(arr[:5:1]) #[0:5:1]
print(arr[1:]) #[1:len(arr)-1:1]

#Array Slicing: neg slice
print(arr[-3:-1]) #from arr[len(arr)-3-1]

#Array Slicing: steps
print(arr[1:3:2]) #every other number is printed; if step = 3, every 3 numbers

#In 2-D
print(arr2[0, 1:3]) #in first element, from 1 to 2
print(arr2[1:3, 3]) #print the third index for both elements
print(arr2[0:2, 3:5]) #print index 3-4 for both the 0 and 1 element
print(arr2[::2]) #every other element for all


#Checking Data Types
print(arr.dtype)

#Data Types
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''


#making array w/ fixed data type: ndarry
 arry = np.array([1,2,3], dtype = 'S') # changes to string
#string-> integer is not possible
#converting data type using astype()

arrf = np.array([1.1, 1.2, 1,3], dtype = 'f')
arri = arrf.astyoe('i') #convert float to integer

#copy vs view
#a copy is not the original and the changes won't be saved.
#The view won't own the data but make direct changes
arrex = np.array([1,2,3])
x = arrex.copyO()
y = arrex.view()
arrex[0, 0] = 1

#checking ownership with bases 
print(y.base) # would return arrex array
print(x.base) #would reutrn "None"

#shaping/reshaping arrays

#shape = # of dimensions, # of elements

print(x.shape)
print(arrn.shape) 


