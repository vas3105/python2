def take_user_input():
    name = [input(f"Enter name {i + 1}: ") for i in range(5)]
    no = [int(input(f"Enter number for {name[i]}: ")) for i in range(5)]
    return name, no

name, no = take_user_input()
data_array = [[name[i], no[i]] for i in range(5)]

data_dict = {}
for item in data_array:
    data_dict[item[0]] = item[1]

sorted_data_array = sorted(data_array, key=lambda x: x[1])

print("Original Data Array:", data_array)
print("Dictionary:", data_dict)
print("Sorted Data Array based on values: ", sorted_data_array)

