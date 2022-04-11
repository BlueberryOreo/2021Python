import random


def bubble_sort(lst: list):
    for ii in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


if __name__ == "__main__":
    nums = [random.randint(1, 1000) for i in range(1000)]
    bubble_sort(nums)
    print(nums)
