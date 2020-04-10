import random


def Factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def Sum_List_Nums(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + Sum_List_Nums(list[1:])


def Create_Rand_List():
    rand_list = set()
    while len(rand_list) != 10:
        rand_list.add(random.randint(1, 100))
    rand_list = list(rand_list)
    return rand_list


def Palindrome_Check(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    else:
        return Palindrome_Check(text[1:-1])


def Solution1(num):
    print(num)
    if num == 1:
        return True
    if num % 2 == 0:
        Solution1(num // 2)
    else:
        Solution1(3 * num + 1)


# F(1) = 1
# F(2) = 2
# F(3) = 4
# F(4) = 7
# F(5) = 13

def func2(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    else:
        return func2(data - 1) + func2(data - 2) + func2(data - 3)


print(func2(6))
