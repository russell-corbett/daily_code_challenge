"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def func1(lst, num):
    j = 1
    for i in range(len(lst)):
        while j < len(lst):
            if lst[i] + lst[j] == num:
                return True
            else:
                j += 1
        j = i + 1

    return False


if __name__ == "__main__":
    l = [10, 15, 3, 7]
    n = 22
    print(func1(l, n))
