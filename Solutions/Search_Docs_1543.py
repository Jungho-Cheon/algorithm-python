input_data = input()
search_data = input()

count = 0
i = 0

# for문의 index를 수정해야하는 경우 while문을 쓰자...
while i <= (len(input_data) - len(search_data)):
    # 문자열의 범위 지정 [start:end]
    if input_data[i:i + len(search_data)] == search_data:
        count += 1
        i += len(search_data)

    i += 1
print(count)
