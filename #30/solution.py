# Create a function which returns the Modulo of the two given numbers.
mod = lambda dividend, divisor : dividend%divisor
mod(-13, 64)
mod(50, 25)
mod(-6, 3)

# Create a function that counts the number of digits in a number. Conversion of the number to a string is not allowed.
filter_list = lambda li : [ item for item in li if type(item) != str]
print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))

# Create a function that takes two number strings and returns their sum as a string.
def add(num1, num2):
    try:
        result = str(int(num1) + int(num2))
    except:
        result = "Invalid Operation"
    return result
print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))

# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
def digits_count(num):
    count = 0
    while True:
        count += 1
        num = int(int(num)/10)
        if not num >0:
            break
    return count
print(digits_count(4666))
print(digits_count(544))
print(digits_count(121317))
print(digits_count(0))
print(digits_count(12345))
print(digits_count(1289396387328))