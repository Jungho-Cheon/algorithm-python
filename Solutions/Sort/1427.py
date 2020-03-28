data = ' '.join(input())
array = list(map(int, data.split()))
array.sort(reverse=True)
for i in array:
    print(i, end='')
print()
