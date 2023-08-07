automobile_attributes = ['Engine', 'Transmission', 'Suspension', 'Brakes', 'Steering', 'Body', 'Tires']
print("List with domain attributes:", automobile_attributes)

numeric_list = [10, 5, 7, 15, 20]


numeric_list[0], numeric_list[-1] = numeric_list[-1], numeric_list[0]
print("List after swapping first and last elements:", numeric_list)

sum_of_digits = sum(numeric_list)
print("Sum of the digits in the list:", sum_of_digits)

smallest_element = min(numeric_list)
print("Smallest element in the list:", smallest_element)

automobile_attributes.append('Fuel System')
print("List after appending 'Fuel System':", automobile_attributes)

automobile_attributes.insert(3, 'Exhaust System')
print("List after inserting 'Exhaust System' at index 3:", automobile_attributes)

new_attributes_tuple = ('Lighting', 'Air Conditioning')
automobile_attributes.extend(new_attributes_tuple)
print("List after extending with a tuple:", automobile_attributes)


new_attributes_set = {'Audio System', 'Navigation'}
automobile_attributes.extend(new_attributes_set)
print("List after extending with a set:", automobile_attributes)


new_attributes_dict = {'Safety Features': 'ABS, Airbags'}
automobile_attributes.extend(new_attributes_dict)
print("List after extending with a dictionary:", automobile_attributes)

automobile_models = {
    'Accord': 2019,
    'Civic': 2020,
    'Camry': 2021,
    'Altima': 2018,
}


sorted_automobile_models = dict(sorted(automobile_models.items()))
print("Sorted dictionary in ascending order based on keys:", sorted_automobile_models)

numeric_dictionary = {
    'a': 10,
    'b': 5,
    'c': 7,
    'd': 15,
    'e': 20,
}


sum_of_values = sum(numeric_dictionary.values())
print("Sum of all values in the dictionary:", sum_of_values)

automobile_prices = {
    'Accord': 30000,
    'Civic': 25000,
    'Camry': 32000,
    'Altima': 28000,
}


sorted_automobile_prices = dict(sorted(automobile_prices.items(), key=lambda item: item[1], reverse=True))
print("Sorted dictionary in descending order based on values:", sorted_automobile_prices)
