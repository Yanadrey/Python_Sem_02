# Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.

N = int(input("Введите число-ограничитель:"))
k=0
print(f"Степени числа 2, не превосходящие {N}: ")
while 2**k<N:
    print(2**k)
    k+=1
