# import random
# import os
# import timeit
# with open("Sum.txt", "w") as out:
#     # out.seek((1024 * 1024 * 1024) - 1) # 1 gb
#     # out.seek((1024 * 1024 * 50) - 1) # 50 mb
#     # size = (1024 * 1024 * 1) - 1
#     # sizeFile = 0
#     # while True:
#     #     if out.seek(sizeFile) != out.seek(size):
#     #         out.write(f"{random.randint(0, 10)}\n")
#     #         sizeFile += 1
#     #     else:   break
#     while (os.path.getsize('Sum.txt') / (1000 * 1000)) < 50:
#         out.write(f"{random.randint(0, 10)}\n")
#
# s = ""
# with open('Sum.txt', 'r') as myfile:
#
#     lines = myfile.readlines() # метод дерьмо, работает коряво
#     # загружает оперативку
#
# sum = 0
# for line in lines:
#     if line.strip().isdigit():
#         sum += 1
# myfile.close()
# print(timeit.timeit(s, num=10))


import os
import timeit
from random import randint


def readlines():
    s = 0
    with open('Sum.txt', 'r') as read:
        lines = read.readlines(52428800)
        for line in lines:
            if line.strip().isdigit():
                s += int(line.strip())


def isstrip():
    s = 0
    with open('Sum.txt', 'r') as file:
        for line in file:
            if line.strip().isdigit():
                s += int(line.strip())


def gener():
    s = sum((int(row.strip()) for row in open('Sum.txt') if row.strip().isdigit()))


def main():
    # with open('digits.txt', 'a') as out:
    #     while os.path.getsize("Sum.txt") < 52428800:
    #         out.write(str(randint(0, 1000000)) + '\n')
    print(timeit.timeit(readlines, number=1))
    print(timeit.timeit(isstrip, number=1))
    print(timeit.timeit(gener, number=1))


main()