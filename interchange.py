def interchange_first_last(list):
    if len(list) < 2:
        return list  # No change needed if the list has less than 2 elements
    
    # Swap first and last elements
    list[0], list[-1] = list[-1], list[0]
    
    return list

# Example usage:
input_list = [12, 35, 9, 56, 24]
output_list = interchange_first_last(input_list)
print("Input:", input_list)
print("Output:", output_list)

