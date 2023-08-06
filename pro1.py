
def count_word_frequency(paragraph, specific_word):
    words = paragraph.split()

    x="car"
    cnt = 0
    for word in words:
        if word == specific_word:
            cnt += 1
    if x in words:
      print("CLASS=",type(x))
    print("count of the words",cnt)



def count_characters(paragraph):
    alphabet_count = 0
    numeric_count = 0
    special_count = 0

    for char in paragraph:
        if char.isalpha():
            alphabet_count += 1
        elif char.isnumeric():
            numeric_count += 1
        else:
            special_count += 1

    return alphabet_count, numeric_count, special_count

paragraph = "Hi hello my name is sidarth 23, car "
words = count_word_frequency(paragraph, "car")
alpha_count, numeric_count, special_count = count_characters(paragraph)
print("Alphabet count:", alpha_count)
print("Numeric count:", numeric_count)
print("Special symbol count:", special_count)

vehicle_data_set = {5847, 67.14, "sedan", True, "electric", 2023}
print("Initial Set:", vehicle_data_set)

popped_element = vehicle_data_set.pop()
print("Popped Element:", popped_element)
print("Updated Set:", vehicle_data_set)

vehicle_data_set.discard("sedan")
print("Set after Discarding 'sedan':", vehicle_data_set)

del_element = 3.14
vehicle_data_set.discard(del_element)
print("Set after Deleting Element", del_element, ":", vehicle_data_set)

vehicle_data_set.clear()
print("Cleared Set:", vehicle_data_set)

vehicle_features_set = {"sedan", "electric", "suv", "hybrid", "convertible"}

sorted_set_descending = sorted(vehicle_features_set, reverse=True)

print("Set in descending order:", sorted_set_descending)

vehicle_tuple = ("Toyota", "Camry", 2023, "sedan")


make, model, year, category = vehicle_tuple

print("Unpacked Variables:")
print("Make:", make)
print("Model:", model)
print("Year:", year)
print("Category:", category)

new_make = "Honda"
new_model = "Civic"
new_year = 2022
new_category = "sedan"

vehicle_tuple = (new_make, new_model, new_year, new_category)

print("Updated Tuple:", vehicle_tuple)

domain_name = "automobile"
character_to_count = 'o'

count_of_character = domain_name.count(character_to_count)
print(f"Count of '{character_to_count}': {count_of_character}")

domain_name = "automobile"


print("Slicing:")
print(domain_name[:])      # Get the entire string
print(domain_name[2:6])    # Get characters from index 2 to 5 (exclusive)
print(domain_name[2:])     # Get characters from index 2 to the end
print(domain_name[:6])     # Get characters from the beginning to index 5 (exclusive)
print(domain_name[::2])    # Get every second character
print(domain_name[::-1])   # Reverse the string using negative step


print("Negative Indexing:")
print(domain_name[-1])     # Get the last character
print(domain_name[-3])     # Get the third character from the end
