import hashlib


N = input()
set_A = set(input().split(' '))
set_A = list(set_A)
dict_A = dict()
for i in range(len(set_A)):
    hexdigest = hashlib.sha256(set_A[i].encode()).hexdigest()
    dict_A[hexdigest] = set_A[i]


M = input()
list_B = list(input().split(' '))

for i in range(len(list_B)):
    hexdigest = hashlib.sha256(list_B[i].encode()).hexdigest()
    if hexdigest in dict_A:
        print('1')
    else:
        print('0')
