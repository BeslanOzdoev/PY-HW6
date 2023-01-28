#22: 
#Напишите программу, которая найдёт сумму элементов списка, \
#стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12.

lst = [2, 3, 5, 9, 3]
lst_index = [i for i in range (len(lst))]

lst_zip = list(zip(lst_index, lst))
print(lst_zip)

sum = 0

for i in range(len(lst_zip)):
    if lst_zip[i][0]%2 != 0:
        sum += lst_zip[i][1]
        print(lst_zip[i][1], end =" ")

print(f'сумма элементовб стоящих на нечетных позициях равна: {sum}')