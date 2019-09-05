import datetime

"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""


def get_input():
    name = raw_input("Enter your name: ")
    print("Your name is " + name)
    age = int(input("Enter your age: "))
    future_age = 100 - age
    cal = datetime.datetime.now()
    year = cal.year
    print("You will be 100 years old in " + str(future_age) + " Years")
    print("You will be 100 years old in Year " + str(future_age + year))
    another_number = int(input("Enter another number: "))
    for i in range(another_number):
        print("You will be 100 years old in " + str(future_age) + " Years")


def even_odd():
    num = int(input("Enter a number: "))
    if num % 4 is 0:
        print("Number " + str(num) + " is Even and divisible by 4")
    elif num % 2 is 0:
        print("Number " + str(num) + " is Even")
    else:
        print("Number " + str(num) + " is Odd")


def print_list(list=None):
    new_list = []
    for num in list:
        if num <= 5:
            new_list.append(num)
    print new_list


def divisors():
    num = int(input("Please choose a number to divide: "))
    list_range = list(range(1, num + 1))
    # print(list_range)
    divisor_list = []
    for number in list_range:
        if num % number == 0:
            divisor_list.append(number)
    print(divisor_list)


def common(list1 = [], list2 = []):
    print(set(list1) & set(list2))


def common1(list1 = [], list2 = []):
    list1_uniq = set(list1)
    list2_uniq = set(list2)
    result = []
    for element in list1_uniq:
        if element in list2_uniq:
            result.append(element)
    print result


def is_palindrome(str):
    new_str = ''
    for ch in str:
        new_str = ch + new_str
    if str == new_str:
        return True
    else:
        return False


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]
print(b)

print(is_palindrome("TOYOTA"))
print(is_palindrome("TaaT"))
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common(list1, list2)
divisors()
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print_list(a)
even_odd()
get_input()
