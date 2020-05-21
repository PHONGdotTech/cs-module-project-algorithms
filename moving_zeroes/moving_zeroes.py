'''
Input: a List of integers
Returns: a List of integers
'''
import sys
sys.setrecursionlimit(5000)

def moving_zeroes(arr):
    # count = 0
    # for x in arr:
    #     if x == 0:
    #         count += 1

    #     if count == len(arr):
    #         return arr

    # if arr[0] == 0:
    #     for i in range(len(arr)-1):
    #         if arr[i] == 0:
    #             arr.pop(i)
    #             arr.append(0)
    #     return moving_zeroes(arr)
    # else:
    #     for i in range(len(arr)-1):
    #         if arr[i] == 0:
    #             arr.pop(i)
    #             arr.append(0)

    # return arr

    # # checks to see if entire array is 0, if it is, doesnt need to be sorted. just return it
    # # O(c)
    # if arr == [0] * len(arr):
    #     return arr

    # # loop through array, if a zero exists pop it and append it to end
    # # O(n^n)
    # for i in range(1,len(arr)-1):
    #     if arr[i] == 0:
    #         arr.append(arr.pop(i))
    #     if arr[i-1] == 0 and arr[1] == 0:
    #         moving_zeroes(arr)

    # # if the first item is 0, pop it and append
    # if arr[0] == 0:
    #     arr.append(arr.pop(0))

    # return arr

    if arr == [0] * len(arr):
        return arr

    newArr = []
    count = 0
    if 0 in arr:
        for i in range(len(arr)):
            if arr[i] == 0:
                count += 1
            else:
                newArr.append(arr[i])

        for _ in range(count):
            newArr.append(0)

        return newArr

    else:
        return arr
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    # arr = [0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0, 1,0,4,5,7,0,6,0] 
    # arr = [0,0,0,0]
    # arr = [1,0,0,0,0,0,0,0,0,0,0,0,2,3,4,0,5,0,6]
    # arr = [0, 0, 0, 0, 3, 2, 1] 

    arr = [0] * 9999
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append(0)
    arr.append(4)

    # arr = [1]
    # for x in range(9):
    #     arr.append(0)
    # arr.append(1)
    # arr.append(2)
    # arr.append(3)
    # arr.append(0)
    # arr.append(4)

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")