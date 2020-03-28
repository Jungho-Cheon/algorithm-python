import random


def Bubble_Sort(random_list):
    for i in range(0, len(random_list)):
        for j in range(0, len(random_list) - i - 1):
            if random_list[j] > random_list[j + 1]:
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
    return random_list


random_list = set()
while len(random_list) != 10:
    random_list.add(random.randint(0, 100))
random_list = list(random_list)

random_list = Bubble_Sort(random_list)
print(random_list)
