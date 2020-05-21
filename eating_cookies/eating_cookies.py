'''
Input: an integer
Returns: an integer
'''
import sys
sys.setrecursionlimit(10000)

def eating_cookies(n, cache=None):
    total = 0
    if n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # cache = [0 for _ in range(n+1)]
            cache = {i:0 for i in range(n+1)}
        for start_with in range(1,3+1):
            if n >= start_with:
                total += eating_cookies(n - start_with, cache)
        cache[n] = total
        return cache[n]

    # if n == 0:
    #     return 1
    # if n < 0:
    #     return 0
    # return eating_cookies(n-1, cache)+eating_cookies(n-2, cache)+eating_cookies(n-3, cache)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5000
    # num_cookies = 50 # 10562230626642
    # num_cookies = 30 # 53798080
    # num_cookies = 10 # 274
    # num_cookies = 5 # 13
    # num_cookies = 4 # 7
    # num_cookies = 3 # 4


    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
