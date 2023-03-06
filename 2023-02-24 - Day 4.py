"""Given an array of integers, find the first missing positive integer in linear time and constant space. In other
words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def func(array):
    num = 1
    while True:
        if num not in array:
            return num
        else:
            num += 1


if __name__ == "__main__":
    if func([3, 4, -1, 1]) == 2:
        print("Success")
    if func([1, 2, 0]) == 3:
        print("Success")
