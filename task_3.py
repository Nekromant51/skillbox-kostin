cards = int(input('Кол-во видеокарт: '))
nvidia = []
for i in range(1,cards+1):
    print(f'{i} видеокарта: ')
    number = int(input())
    nvidia.append(number)
print("Старый список видеокарт: ", nvidia)
max_number = max(nvidia)
stock = []
for c in range(0, len(nvidia)):
    if nvidia[c] != max_number:
        stock.append(nvidia[c])
print('Новый список видеокарт: ', stock, )