name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list = []
count = 0
for i in range (0, len(name_list) - 1,2):
    new_list.append(name_list[i])
print(new_list)