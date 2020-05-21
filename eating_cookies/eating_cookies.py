'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    total = 0
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for start_with in range(1,3+1):
            if n >= start_with:
                total += eating_cookies(n - start_with)
        return total

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     print("entered n == 1, so add 1 and start_with to total")
    #     return 1
    # elif n == 2:
    #     print("entered n == 2, so add 3 and start_with to total")
    #     return 2
    # elif n == 3:
    #     print("entered n == 3, so add 4 and start_with to total")
    #     return 4
    # else:
    #     print("entered else")
    #     print(f"cookies is {n}")
    #     for start_with in range(1,3+1):
    #         print(f"\nloop start")
    #         print(f"Current total is {total}")
    #         print(f"start_with is {start_with}")
    #         if n > start_with:
    #             total += start_with + eating_cookies(n-start_with)
    #         print(f"total is now {total}")
    #     return total

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
