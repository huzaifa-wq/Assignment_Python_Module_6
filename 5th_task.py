def remove_uneven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Main program
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cut_down_list = remove_uneven(original_list)

print("Original list:", original_list)
print("List without uneven numbers:", cut_down_list)
