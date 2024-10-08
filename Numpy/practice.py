import numpy as np
#Task 1 => creating and manipulating arrays
#Creating an 3x3 array with values ranging from 1-9
arr = np.arange(1,10).reshape(3,3)
#Multipying the entire array with 5 and storing ans in a variable called result
result = arr * 5
#Replacing the middle element of the array with 0
result[1,1] = 0
print(result)
print("Task 1 Ends Here :)\n ")


#Task 2 => Matrix Operations
#Creating 2x2 matrices
arr1  = np.matrix(((1,2,3),(4,5,6)), dtype='int32')
#Performing element wise addition
element_wise_addition = np.sum(arr1)
print(element_wise_addition)
print("Task 2 Ends Here :)\n ")


#Task 3 => Statistical Functions
arr2 = np.random.randint(10,100,size=(15))
print("This is a numpy array of 15 integers btwn 10-100: {}".format(arr2))
#Finding the mean 
mean_of_arr2 = np.mean(arr2)
print("This is the mean of arr2: {}".format(mean_of_arr2))
#Finding the median 
median_of_arr2 = np.median(arr2)
print("This is the median of arr2: {}".format(median_of_arr2))
#Finding the standard deviation 
standard_deviation_of_arr2 = np.std(arr2)
print("This is the standard deviation of arr2: {}".format(standard_deviation_of_arr2))
#Finding the variance of the array
variance_of_arr2 = np.var(arr2)
print("This is the variance of arr2: {}".format(variance_of_arr2))
print("Task 3 Ends Here :)\n ")

#Task4 => Array Slicing and Indexing
#Create a 4x4 array where each element is the square of its index
#Function for creating the array elements
arr3 = np.zeros((4,4))
def create_elements(arry):
    for i in range(len(arry)):
        for j in range(len(arry[i])):
            arry[i][j] = ((i**2) + (j**2))
    return arry
array_elements = create_elements(arr3)
print(array_elements)
print("\n ")
#Extract the last two rows and last two columns
last_two_cols = array_elements[2:]
last_two_rows = array_elements[2:4]
print("These are the two last rows:\n {}".format(last_two_rows))
print("These are the two last columns:\n {}".format(last_two_cols))
#Replacing row1 with all zeros
zero_array = np.zeros((1,1))
array_elements[:1] = zero_array
print("The first row has been replaced with zeros:\n {} ".format(array_elements))
print("Task 4 Ends Here :) \n")

#Task 5 => Inverse and Determinant of a matrix
#Create a 3x3 matrix
arr5 = np.matrix(((1,2,3),(4,5,6),(7,8,9)))
#Calculating the determinant of the matrix
determinant_of_arr5 = np.linalg.det(arr5)
print("This is the determinant of arr5: {}".format(determinant_of_arr5))
def check_matrix_determinant(): #Function to check if a matrixes determinant is zero
    if determinant_of_arr5 == 0:
        print("The matrix does not have a non-determinant")
    else:
        inverse_of_arr5 = np.linalg.inv(arr5)
        print("The matrix has a determinant.It's inverse is:\n {}".format(inverse_of_arr5))
check_matrix_determinant()
print("Task 5 Ends Here :) ")