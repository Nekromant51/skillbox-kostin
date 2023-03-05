new_list = []
number = int(input("Введите число: "))
for i in range (1,number):
    if i%2 != 0:
        new_list.append(i)
print(f'Список из нечётных чисел от одного до N: {new_list}')
