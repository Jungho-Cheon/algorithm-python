# 단어 뒤집기 2

string, temp = input() + " ", ""
arr = []

ck = False

for i in string:
    if i == ' ':
        if not ck:
            print(temp[::-1], end=" ")
            temp = ""
        else:
            print(" ", end="")
    elif i == '<':
        ck = True
        print(temp[::-1] + '<', end="")
        temp = ""
    elif i == '>':
        ck = False
        print('>', end="")
    else:  # 알파벳과 숫자
        if ck:
            print(i, end="")
        else:
            temp += i

print()
