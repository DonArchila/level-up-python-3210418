
# Save a dictionary to a file and load it back
def save_dict(dictionary, file_path):
    with open(file_path, "w") as file:
        for key, value in dictionary.items():
            file.write(f"{key}: {value}\n")

# Load a dictionary from a file
def load_dict(file_path):
    with open(file_path, "r") as file:
        dictionary = {}
        for line in file:
            key, value = line.strip().split(": ")
            dictionary[key] = value
    return dictionary 

# Example usage:
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# save_dict(my_dict, "my_dict.txt")
# loaded_dict = load_dict("my_dict.txt")
# print(loaded_dict)  # Output: {'name': 'John', 'age': '30', 'city': 'New York'}


if __name__ == "__main__":
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    save_dict(my_dict, "my_dict.txt")
    loaded_dict = load_dict("my_dict.txt")
    print(loaded_dict)  # Output: {'name': 'John', 'age': '30', 'city': 'New York'}