import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Provided code runtime: 14.741260051727295 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Binary search runtime: 0.0987551212310791 seconds
def binary_search_algorithm(array, bottom, top, value):
    if top >= bottom:
        # Find the middle
        middle = bottom + (top - bottom)//2
        # If value is less than middle, re-search in the left portion
        if value < array[middle]:
            return binary_search_algorithm(array, bottom, middle-1, value)
        # If value is greater than middle, re-search in the right portion
        if value > array[middle]:
            return binary_search_algorithm(array, middle + 1, top, value)
        if value == array[middle]:
            return duplicates.append(value)
    # if value not found, return empty
    else:
        return duplicates


new_names_1 = sorted(names_1)
for current_name in names_2:
    binary_search_algorithm(new_names_1, 0, len(names_1)-1, current_name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
