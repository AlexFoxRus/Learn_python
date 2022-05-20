a = int(input())
b_max = a % 10
b_min = a % 10
while a != 0:
    b = a % 10
    if b_min < b >= b_max:
        b_max = b
        b_min = b_min
    elif b_min > b < b_max:
        b_min = b
        b_max = b_max      
    a = a // 10
print("Максимальная цифра равна ", b_max)
print("Минимальная цифра равна ", b_min)

#альтернативное решение:
#a = int(input())
#a = str(a)
#print(max(a))
#print(min(a))