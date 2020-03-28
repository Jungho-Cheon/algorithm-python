digits = input()

one_count = 0
zero_count = 0

if digits[0] == '0':
    one_count += 1
else:
    zero_count += 1

for i in range(len(digits) - 1):
    if digits[i] != digits[i + 1]:
        if digits[i] == '0':
            zero_count += 1
        else:
            one_count += 1

print(min(one_count, zero_count))
