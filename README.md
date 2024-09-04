# Python Solutions

This repository contains a series of simple Python functions and examples. Each solution demonstrates a basic concept or technique in Python. Below is a brief overview of what each solution does and how you can use it.

## Solutions

### Solution 1: Add Numbers

Function to add two numbers.

```python
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(2, 5))  # Output: 7
```
## Solution2:Check Even Number
```def is_even(num):
    return num % 2 == 0

print(is_even(6))  # Output: True
print(is_even(9))  # Output: False
```
## Solution3: Reverse string 
```def reverse_string(text):
    return text[::-1]

print(reverse_string("yassir"))  # Output: "rissay"
```
## solution4: count Vowels 
```def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

result = count_vowels("Hello peter")
print(result)  # Output: 4
```
## Solution5: Calculate Factorial
```def calculate_factorial(n):
    if n == 0:
        return 1

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    return factorial

result = calculate_factorial(3)
print(result)  # Output: 6
```
## Solution6: Apply Decorator
```def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def sample_function():
    return "Function executed"

print(sample_function())  # Output: Decorator Applied\nFunction executed
```
## solution7 : sort by Age 
```
def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])

people = [("muturi", 30), ("yasir", 25), ("joy", 35), ("shariff", 22)]
sorted_people = sort_by_age(people)

print(sorted_people)  # Output: [('shariff', 22), ('yasir', 25), ('muturi', 30), ('joy', 35)]
```
 ## solution8 : Merge Dictionaries
 ```
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
print(merged_dict)  # Output: {'a': 10, 'b': 25, 'c': 45, 'd': 25}
```
## solution9 : Car class
```
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
print(merged_dict)  # Output: {'a': 10, 'b': 25, 'c': 45, 'd': 25}
```
## License 

This README.md provides a clear explanation of each solution and guides on how to run and understand the code.



