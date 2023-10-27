def count_vowels(input_string):
    input_string = input_string.lower()
    count = 0
    for char in input_string:
        if char in 'aeiou':
            count += 1
    return count

input_string = "idi naxui"
result = count_vowels(input_string)
print(f"Кількість голосних літер у рядку '{input_string}': {result}")
