# %%
# Problem 1
def hello(name):
    return f"Hello {name}, my name is Zhiying."

problem_1 = hello("Morty")
problem_1

# %%
# Problem 2
def divisible(num):
    return [i for i in range(10001) if i % num == 0]

problem_2 = divisible(3)
problem_2

# %%
# Problem 3
def remove_none(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}

problem_3 = remove_none({"a": 1, "b": "Mitch", "c":None})
problem_3

# %%
# Problem 4
def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

list_p4 = [218931, 9**2, 0, True, "apple", -56, None]
problem_4 = length(list_p4)
problem_4

# %%
# Problem 5
def my_reverse(list):
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list

list_p5 = [False, -900, 1, 2**3, "CAR", 29293984859, None]
problem_5 = my_reverse(list_p5)
problem_5


# %%
# Problem 6
def my_min(list):
    if not list:
        return None
    min_value = list[0]
    for num in list:
        if num < min_value:
            min_value = num
    return min_value

list_p6 = [29485, 0, -8**99, 2*3, 9-1, 8837459397, 39485//7, 193748%8]
# print(list_p6)
problem_6 = my_min(list_p6)
problem_6

# %%
# Problem 7
def written_numbers(n):
    numbers = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
    }
    
    result = {}
    for i in range(n + 1):
        if i in numbers:
            result[i] = numbers[i]
        else:
            hundreds = i // 100
            tens = (i % 100) // 10
            ones = i % 10
        
            if hundreds > 0:
                result[i] = numbers[hundreds] + " hundred"
                if tens > 0 or ones > 0:
                    result[i] += " and "
            else:
                result[i] = ""
        
            if tens >= 2:
                result[i] += numbers[tens * 10]
                if ones > 0:
                    result[i] += "-" + numbers[ones]
            elif tens == 1:
                result[i] += numbers[i % 100]
            elif ones > 0:
                result[i] += numbers[ones]

    return result

problem_7 = written_numbers(999)
problem_7

# %%
# Problem 8
def fizzbuzz(n):
    result = ""
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            result += "fizzbuzz\n"
        elif i % 3 == 0:
            result += "fizz\n"
        elif i % 5 == 0:
            result += "buzz\n"
        else:
            None
    return result.rstrip("\n")

problem_8 = fizzbuzz(16)
print(problem_8)


