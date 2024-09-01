#solution1
def add_numbers(num1, num2):
    return num1+ num2

print(add_numbers(2,5))

#solution2
def is_even(num):
    return num % 2 == 0
# this function returns true if number is even and otherwise

print(is_even(6))
print(is_even(9))

# solution3

def reverse_string(text):
    return text[:: -1] # this function returns the reverse of the string name
print(reverse_string ("yassir"))

# solution4

def count_vowels(text):
    # this functions returns vowels aeiou in the string
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

result = count_vowels("Hello peter") 
print(result)  

#solution5


def calculate_factorial(n):
    if n == 0:
        return 1
    
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial


result = calculate_factorial(3)
print(result) 

#solotion6
def apply_decorator(func):
    
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def sample_function():
    return "Function executed"

print(sample_function())  

#solution7
def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])

people = [("muturi", 30), ("yasir", 25), ("joy", 35), ("shariff", 22)]
sorted_people = sort_by_age(people)

print(sorted_people)  



#solution 8
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy() 
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  
        else:
            merged_dict[key] = value  
    
    return merged_dict


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)


#solution9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")


car1 = Car("nissan", "GTR",2020 )
car1.display_info()