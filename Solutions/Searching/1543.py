# 문서 검색

string = input()
comp = input()

count = 0
i = 0
while i <= len(string) - len(comp) + 1:
    if string[i:i + len(comp)] == comp:
        count += 1
        i += len(comp)
    else:
        i += 1
print(count)
