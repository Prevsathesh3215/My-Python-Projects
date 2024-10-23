import random
#
# original = [n for n in range(1, 11)]
# input = [n for n in original]
# random.shuffle(input)
# print(f"{input}\n")
# count = 0
#
# def insertion_sort(input):
#     for i in range(len(input) - 1):
#         next = input[i + 1]
#         current = input[i]
#         if input[i] > input[i + 1]:
#             input[i + 1] = current
#             input[i] = next
#             print('repeat')
#
#         global count
#         count += 1
#         print(input)
#
#
#     for x in range(len(original) - 1):
#         if input[x] != original[x]:
#             print('enter new func\n')
#             insertion_sort(input)
#
#     return input
#
# print(insertion_sort(input))
# print(count)


def insertionSort(arr):
    count = 0
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        print('run for')
        print(arr)
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            count += 1 
            print('run while')
            print(arr)
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position


# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [n for n in range(1, 11)]
random.shuffle(arr)
insertionSort(arr)
print(arr)