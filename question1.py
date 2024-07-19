# Question 1:  Write a program that takes an array and Find Second largest element in an array
# For example -: Input: array = [12, 35, 1, 10, 34, 1]
#code:
def largest_element(arr):
    largest=arr[0]
    second_largest=arr[0]
    for i in range(len(arr)): # Here in this loop we are comparing every element of the array with the initial largest value and if that element is largest than the previous largest value, then the new largest value is updated. 
        if arr[i]>largest:
            largest=arr[i] # At the end of this loop, we get the largest value in the array.
    for i in range(len(arr)): # Here in this loop we are excluding the largest value and finding out the largest value which will be the second largest.
        if arr[i]>second_largest and arr[i]!=largest:
            second_largest=arr[i]
    return second_largest

print('The second largest element of the array is', largest_element([12,35,1,10,34,1]))
