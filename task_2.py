first = int(input('введите первое число прогрессии:'))
znamenatel = int(input('Введите знаменатель прогрессии:'))
colvo = int(input('введите количество числе в прогрессии:'))

for i in range(colvo):
    print(first, end = ' ')
    first = first * znamenatel
    