""" write a program that will moves all Zeroes to end of an array
For example -: Input: array = [1,2,0,4,3,0,5,0]; """
#Code:
def pushZerosToEnd(arr, num): 
    count = 0 # count variable holds the number of non-zero integers. 
    for i in range(num): #In this loop, all the non-zero integers are pushed to one side by overwriting the index of element 0 with the next non zero integer.
        if arr[i] != 0:
            arr[count] = arr[i] 
            count+=1
    while count < num:  #Here we are inserting 0s for the remaining indices of the array. 
        arr[count] = 0
        count += 1
 
arr = [1,2,0,4,3,0,5,0] 
num = len(arr) 
pushZerosToEnd(arr, num) 
print("Array after pushing all zeros to end of array:") 
print(arr) 