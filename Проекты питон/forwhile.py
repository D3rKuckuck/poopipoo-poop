# a = 1
# while a < 10:
#     print(a)
#     a = a + 1
# print(a)
# while a > 1:
#     print(a)
#     a = a - 1
# print("Конец цикла", a)
a = []
while len(a) < 4:
    num = int(input("Целое число: "))
    a.append(num)
print("Сумма чисел:", sum(a))