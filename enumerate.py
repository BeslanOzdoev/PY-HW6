#Задача №22: 
#Напишите программу, которая найдёт сумму элементов списка, \
#стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12.

lst = [2, 3, 5, 9, 3]

lst = list(enumerate(lst))
print(lst)

lst1=[]
for i in range(len(lst)):
    if lst[i][0]%2 != 0:
        lst1.append(lst[i][1])
print(f'сумма элементов на нечетных позициях равна: {sum(lst1)}')