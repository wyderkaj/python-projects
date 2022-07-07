# comparison of binary and linear search

import random
import time

print("Comparison of binary and linear search!")
print("We are looking for a random number in the collection of numbers between 1 and 10000.")
array = range(1,10000)
k = random.randint(1,10000)
n = len(array)

print("\nProof that both searches are looking for the same value:")
print(f"Value that we are looking for is: ", k)

#Linear Search 
# scan entire list and ask if its equal to the the value you are looking for
# if yes return the index, if no then return -1

def LinearSearch(array, n, k):
    for j in range(0, n):
        if (array[j] == k):
            return j
    return -1

result = LinearSearch(array, n, k)

if(result == -1):
    print("Element not found")
else:
    print("In Linear Search element is present at index", result)
    

# binary search uses divide and conquer! We will leverage the fact that our list is sorted
# every time looking value is to the left of the midpoint, we're actually subtracting one from the high. 
# And then every single time our value is to the right of the midpoint, we're adding one to the midpoint for the low. 

def BinarySearch(array, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == k:
            return mid
        elif array[mid] > k:
            return BinarySearch(array, k, low, mid-1)
        else:
            return BinarySearch(array, k, mid + 1, high)
    else:
        return -1

result = BinarySearch(array, k, 0, len(array)-1)

if result != -1:
    print("In Binary Search element is present at index " + str(result))
else:
    print("Element not found")
 
     
 #time analysis   
print("\nComparison of binary and linear search times")
start = time.time()
for k in array:
    LinearSearch(array,n, k)
end = time.time()
print("Linear search time: ", (end - start), "seconds")

start = time.time()
for k in array:
    BinarySearch(array, k, 0, len(array)-1)
end = time.time()
print("Binary search time: ", (end - start), "seconds")

