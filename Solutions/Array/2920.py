array = list(map(int, input().split()))

ascending = True
descending = True

for i in range(len(array) - 1):
    if array[i] < array[i + 1]:
        descending = False
    else:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
