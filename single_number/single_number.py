'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # # my solution O(n^2)
    # for i in arr:
    #     count = 0
    #     for j in arr:
    #         if i == j:
    #             count += 1
    #     if count == 1:
    #         return i

    # # method 1: O(n)?
    # for i in arr:
    #     if arr.count(i) == 1:
    #         return i

    # # method 2: O(2n)
    # # we'll keep an array, call it 'no dupes' to hold numbers we see in the arr array
    # no_dupes = []
    # # iterate through arr
    # for x in arr:
    #     # check to see if the number is already in the no_dupes array
    #     if x not in no_dupes:
    #         no_dupes.append(x)
    #     # if it is, remove it from the 'no_dupes' array
    #     else:
    #         no_dupes.remove(x)
    # # when we're done iterating, the onlly number in our 'no_dupes' array is the odd number out
    # # return it
    # return no_dupes[0]

    # # method 3: O(n)
    # keep track of the counts of how many times we've seen a particular number
    # dictionaries are better at being searched
    counts = {}

    # loop through nums to tally up how many times we've seen each number
    # O(n)
    for x in arr:
        if x in counts: # O(1)
            del counts[x]
        else:
            counts[x] = 1
            
    # loop through all of the key value pairs in count to find the one pair whose value is 1
    # O(1)
    for num in counts:
        if counts[num] == 1:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")