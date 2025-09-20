import numpy as np

# Creating a 1D array
numpyArr1Ad = np.array([1, 2, 3, 4, 5]) # arryay() is return an object of numpy ndarray class
print("numpy 1D Array:", numpyArr1Ad)

print("Type of numpyArr1Ad:", type(numpyArr1Ad)) # z<class 'numpy.ndarray'>Type of numpyArr1Ad: <class 'numpy.ndarray'>
print("Dimensions of numpyArr1Ad:", numpyArr1Ad.ndim) # 1
print(f" Size of 1D array : {numpyArr1Ad.size}") # 5 total number of elements- size is count number of elements.

'''
The array object in NumPy is called ndarray, it provides a lot of supporting functions that 
make working with ndarray very easy.

inside array() - we can pass LIST, TUPLE, etc. and it will convert it into ndarray object. np.array() can accept lists, tuples, and other array-like iterables — not just lists and tuples. ✔️
so array() method of numpy is used to create numpy array from these array-like iterables.
'''




# create 2D array
arr2 =np.array([ [1 ,2, 3],
                 [10, 20, 30]
               ]) # 2,3 array 2 rows and 3 columns

print(f" numpy 2D array : ")
print(arr2)
print(f"Type of array : {type(arr2)}") # <class 'numpy.ndarray'>
print(f" Dimensions of arr2 : {arr2.ndim}") # 2

print(f"Shape of 2 d array : {arr2.shape}") # (2, 3) 2 rows and 3 columns
print(f"Size of 2 d array : {arr2.size}") # 6  total number of elements- size is count number of elements.
print(f"Data type of 2 d array : {arr2.dtype}") # int64

