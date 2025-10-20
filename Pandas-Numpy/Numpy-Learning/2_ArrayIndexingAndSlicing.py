'''
Access Array Elements:

        --> Array indexing is the same as accessing an array element.
        --> You can access an array element by referring to its index number.
        --> The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

Slicing arrays

        --> Slicing in python means taking elements from one given index to another given index.
        --> We pass slice instead of index like this: [start:end].
        --> We can also define the step, like this: [start:end:step].
        --> If we don't pass start its considered 0
        --> If we don't pass end its considered length of array in that dimension
        --> If we don't pass step its considered 1
'''

# 1D array :

import numpy as np
     #           0 1  2  3  4
arr1 = np.array([1,2,3,4,5]) 
print(f" Arr1 : {arr1}")

print(f"FirstElement arr1[0] : {arr1[0]}")  # First element
print(f"Array 2nd element arr1[1]  : {arr1[1]}") # Second element
print(f"Array Last element by Normal index  arr1[{len(arr1)-1}] : {arr1[len(arr1)-1]}") # Last element by normal index
print(f"Array Last element by Negative Index arr1[-1] : {arr1[-1]}") # Last element by Negative Index
print(f"Array 2nd last element by Negative Index arr1[-2] : {arr1[-2]}") # 2nd last element by Negative Index


print("\n\n ---------------------  Slicing Operator  START for 1D  ---------------------------------\n")
print(f"\n Lets  Access with Slicing operator- 2nd element to last :  {arr1[1:len(arr1)]}") # a:b (b is excluded) to it will run from start to len(arr1)-1

print(f"\n 2nd and 3rd element only : {arr1[1:3]}") # 2nd and 3rd element only


print("\n\n ---------------------  Slicing Operator  END for 1D  ---------------------------------\n")


# Create a 2D array
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]
                  ])

print(f"\nArr2d : \n{arr2d}")
print(f"\nIn 2D array, access element at all 1st row arr2d[1]: {arr2d[1]}") # access element at all 1st row
print(f"\nIn 2D array, access element 1st row 2nd element arr2d[1][1]: {arr2d[1][1]}") # access element 1st row 2nd element
print(f"\nIn 2D array, other way access element 1st row 2nd element arr2d[1][1]: {arr2d[1,1]}") # another way to access element 1st row 2nd element - 6

print("\n\n ---------------------  Slicing Operator  START for 2D  ---------------------------------\n")
print(f"\n In 2D array find last element of2nd dimension->  arr2d[1, -1] : {arr2d[1, -1]}") # In 2D array find last element of2nd dimension
print(f"\n With Two Bracket In 2D array find last element of2nd dimension->  arr2d[1][-1] : {arr2d[1][-1]}") # In 2D array find last element of 2nd dimension With TWO bracket
print(f"\n In 2D array find last element of 3rd dimension->  arr2d[2, -1] : {arr2d[2, -1]}") # In 2D array find last element of 2nd dimension with ONE bracket
print(f"\n In 2D array find last element of last dimension->  arr2d[-1, -1] : {arr2d[-1, -1]}") #  In 2D array find last element of last dimension with ONE bracket
print(f"\n With Two Bracket In 2D array find last element of last dimension->  arr2d[-1][-1] : {arr2d[-1][-1]}") # In 2D array find last element of last dimension with two bracket

print("\n\n ---------------------  Slicing Operator  END for 2D  ---------------------------------\n")



print(f"Data Type of 1D array : {arr1.dtype}") # int64
# Explanation: All elements are integers, so NumPy infers the dtype as 64-bit integers (int64).

print(f"Data Type of 2D array : {arr2d.dtype}") # int64
# Explanation: Same as above, elements are integers, so dtype is int64.

arrStr = np.array(["apple","banana", "cherry"])
print(f"String type numpy array : {arrStr}")
print(f"DATA TYPE of String type numpy array : {arrStr.dtype}") # <U6
'''
Explanation:
- NumPy represents strings using fixed-size Unicode string types.
- <U6 means:
    <  : little-endian byte order (not important for strings)
    U  : Unicode string type
    6  : maximum number of characters (not bytes) per element
- The longest string in the array is "banana" or "cherry", both 6 characters long.
- So, NumPy sets the dtype to <U6 to allocate space for up to 6-character Unicode strings.
- This is different from Python's flexible str type; NumPy uses fixed-size types for efficiency.
'''