# Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.
n = int(input('Введите  число:'))
k = 0
res = 2
print(res)
while res < n:
    res = res*2
    k += 1
    
    if res > n:
        break
    else:
        print(res)
