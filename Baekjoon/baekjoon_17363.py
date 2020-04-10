char_change = {
    '.': '.',
    'O': 'O',
    '-': '|',
    '|': '-',
    '/': '\\',
    '\\': '/',
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^'
}


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
res = [[] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        c = arr[j][M-i-1]
        res[i].append(char_change[c])


[print(''.join(line)) for line in res]
