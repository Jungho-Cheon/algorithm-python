# 두 개의 손

# S : 가위
# R : 바위
# P : 보

ML, MR, TL, TR = input().split()
MS = (ML, MR)
TK = (TL, TR)

win_cond = {"S": "P", "R": "S", "P": "R"}

# 1 : A win
# 0 : draw
# -1 : B win


def win(A, B):
    if A == B:
        return 0
    else:
        if win_cond[A] == B:
            return 1
        return -1


if MS[0] == MS[1]:
    res1 = win(MS[0], TK[0])
    res2 = win(MS[0], TK[1])
    if res1 == -1 or res2 == -1:
        print("TK")
    elif res1 == 0 or res2 == 0:
        print("?")
    else:
        print("MS")
elif TK[0] == TK[1]:
    res1 = win(TK[0], MS[0])
    res2 = win(TK[0], MS[1])
    if res1 == -1 or res2 == -1:
        print("MS")
    elif res1 == 0 or res2 == 0:
        print("?")
    else:
        print("TK")
else:
    print("?")
