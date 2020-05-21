'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0
    for x in arr:
        if x == 0:
            count += 1

        if count == len(arr):
            return arr

    if arr[0] == 0:
        for i in range(len(arr)-1):
            if arr[i] == 0:
                arr.pop(i)
                arr.append(0)
        return moving_zeroes(arr)
    else:
        for i in range(len(arr)-1):
            if arr[i] == 0:
                arr.pop(i)
                arr.append(0)

    return arr

    # print(arr)
    # for i in range(len(arr)-1):
    #     if arr[i] == 0:
    #         arr.append(arr.pop(i))

    # print(arr)
    # for i in range(len(arr)-1):
    #     if arr[i] == 0:
    #         arr.append(arr.pop(i))

    # print(arr)
    # for i in range(len(arr)-1):
    #     if arr[i] == 0:
    #         arr.append(arr.pop(i))

    # return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 0, 0, 3, 0,0,0,0,2,0,0,0, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")