def process_names(names):
    processed_names = []

    for name in names:
        first_part, second_part = name.split()
        processed_name = f"{first_part.upper()}{second_part.lower()}"
        processed_name = processed_name.replace(" ", "")[:-2]
        processed_names.append(processed_name)

    return processed_names
names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

processed_names = process_names(names)

processed_names.sort()

print("\nProcessed Names:")
for index, name in enumerate(processed_names):
    print(f"{index + 1}: {name}")
