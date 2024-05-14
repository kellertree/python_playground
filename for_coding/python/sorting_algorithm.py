def counting_sort_ABC(arr):
    # Initialize count dictionary for 'A', 'B', and 'C'
    count = {'A':0, 'B':0, 'C':0}

    # Count the occurrences of each element in the array
    for element in arr:
        if element in count:
            count[element] += 1

    # Generate the sorted array based on the counts
    sorted_arr = ['A'] * count['A'] + ['B'] * count['B'] + ['C'] * count['C']

    return sorted_arr

# Example usage:
input_list = ['B', 'C', 'A', 'B', 'C', 'A', 'A']
sorted_list = counting_sort_ABC(input_list)
print(sorted_list)


