def add_hyphens(text):
    return "-".join(text)

def print_unique_chars(text):
    unique = set(text)
    print("Унікальні символи:")
    for char in unique:
        print(char)

user_str = input("Введіть рядок символів: ")

formatted_str = add_hyphens(user_str)
print("Рядок з дефісами:", formatted_str)

print_unique_chars(user_str)
