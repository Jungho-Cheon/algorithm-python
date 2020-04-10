input_data = int(input())

minus_val = 1
count = 0
while input_data > 0:
    if input_data < minus_val:
        minus_val = 1
    input_data -= minus_val
    minus_val += 1
    count += 1

print(count)
