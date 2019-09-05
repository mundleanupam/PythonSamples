
def convertsectoday(n):
    out_str = ''
    day = n // (24 * 3600)

    n = n % (24 * 3600)
    hour = n // 3600

    n = n % 3600
    minutes = n // 60

    n = n % 60
    seconds = n

    print(day, "days", hour, "hours",
      minutes, "minutes",
      seconds, "seconds")


def fizzbuzz(m):
    # for num in m: # This is for the array when you want to iterate for the actual numbers in array m
    # for num in range(len(m)): # This is for the loop when you want to iterate for number of elements in array m
    for num in range(m): # This is for the loop when you want to repeat the same operation m times
    # number divisible by 3, print 'Fizz'
    # in place of the number
        if num % 15 == 0:
            print("FizzBuzz")
            continue

    # number divisible by 5, print 'Buzz'
    # in place of the number
        elif num % 3 == 0:
            print("Fizz")
            continue

    # number divisible by 15 (divisible
    # by both 3 & 5), print 'FizzBuzz' in
    # place of the number
        elif num % 5 == 0:
            print("Buzz")
            continue

    # print numbers
        print(num)



def mergeStrings(a, b):
    result = ''
    if len(a) < len(b):
        for i in range(len(a)):
            result += a[i]
            result += b[i]
        result += b[i + 1:len(b)]

    else:
        for i in range(len(b)):
            result += a[i]
            result += b[i]
        result += a[i + 1:len(a)]
    return result


def transformCavity(arr, n):
    result = []
    for row in xrange(1, n - 1):
        for col in xrange(1, n - 1):
            if arr[row - 1][col] != 'X' and int(arr[row - 1][col]) < int(arr[row][col]) and \
                    arr[row + 1][col] != 'X' and int(arr[row + 1][col]) < int(arr[row][col]) and \
                    arr[row][col - 1] != 'X' and int(arr[row][col - 1]) < int(arr[row][col]) and \
                    arr[row][col + 1] != 'X' and int(arr[row][col + 1]) < int(arr[row][col]):
                arr[row][col] = 'X'
    result=arr
    print result


def replaceSpaces(str):
    result = ''
    for ch in str:
        if ch == ' ':
            result = result + '%20'
        else:
            result = result + ch
    print result


def reverse(str):
    result = ''
    for ch in str:
        result = ch + result
    print result


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


def isParenthesisValid(s):
    stack = []
    for ch in s:
        if ch not in "({[)}]":
            continue
        elif ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')
        elif ch == '[':
            stack.append(']')
        elif len(stack) == 0 or stack.pop() != ch:
            return False
    if len(stack) == 0:
        return True


def remove_duplicates(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


def dedupe_v2(x):
    return list(set(x))


def reverse_words(str):
    str_new = str.split(" ")
    result = ""
    print str_new
    for word in reversed(str_new):
        result = result + " " +word
    print result


def reverse_words1(str):
    str_new = str.split(" ")
    result = ""
    print str_new
    for i in range(len(str_new)-1, -1, -1):
        result = result + " " + str_new[i]
    print result


reverse_words1("Anupam is my name")
dup_list = {1, 2, 3, 4, 1, 3, 4, 6, 7, 8}
print(remove_duplicates(dup_list))
string = "{[]{()}}"
print check(string)
print isParenthesisValid(string)
string = "[{}{})(]"
print check(string)
print isParenthesisValid(string)

reverse("Mr John Smith ")
replaceSpaces("Mr John Smith ")
arr1 = [[1 ,2 ,3 ,4] ,[1 ,23 ,4 ,5]]
arr2 = [[str(1) ,str(2) ,str(3) ,str(4)], [str(2) ,str(3) ,9 ,str(4)], [str(1) ,str(2) ,str(4) ,str(3)], [str(1) ,str(1) ,str(1) ,str(1)]]
transformCavity(arr2, 4)
str = mergeStrings('HackerRank', 'Monday')
print str
n = 129600
convertsectoday(n)
arr = [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fizzbuzz(100)
#fizzbuzz(arr)
