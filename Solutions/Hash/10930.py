import hashlib

input_data = input()
# .encode() -> 문자열을 바이트 객체로 바꿈
print(input_data.encode())
hexdigest = hashlib.sha256(input_data.encode()).hexdigest()
print(hexdigest)
