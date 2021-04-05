s = int (input('Введите число от 1 до 20: '))
n1 = " процент "
n2 = " процента "
n3 = " процентов "
if s == 1:
    print(str(s) + n1)
elif s > 1 and s < 5:
    print(str(s) + n2)
elif s > 5 and s <= 20:
    print(str(s) + n3)
else:
    print('Вы загадали число выше 20')
