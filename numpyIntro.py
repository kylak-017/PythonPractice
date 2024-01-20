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

