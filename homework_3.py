# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])
#
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# # print(sum([x for x in list_1 if isinstance(x, int)])) #принадлежит ли объект определенному типу или нет
# def print_numbers():
#     for i in range(len(list_1)):
#         if (type(list_1[i]) == int):
#             print(sum(list_1[i]))

# print_numbers()

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
def print_words_with_letter(): #задаем функцию напечатать слова с буквами просто так назвала
    for i in range(len(list_1)):
        # для i- это индекс в цикле, len-длинна списка (8 итереций-элементов)
        # в цикле прохожу по всем элементам (которых 8)
        # на каждой итерации проверяю тип - должен быть равен строке и если равен, то происходит проверка на 'a'
        if (type(list_1[i]) == str) and ('a' in list_1[i]):
            #то есть оба услувия должны быть True
            print(list_1[i]) #вывод если оба условия True

print_words_with_letter() #вызов функции!!!

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
#
# list_1 = ['cat', 'dog', 'horse', 'cow']
# tuple_1 = tuple(list_1)
# print(tuple_1)
# print(type(tuple_1))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input('Введите членов первой семьи через запятую: ')
# family_2 = input('Введите членов семьи второй через запятую: ')

# listFamily_1 = family_1.split(',')
# listFamily_2 = family_2.split(',') #разделяем запятой
# print(type(listFamily_1))
# print(type(listFamily_2))
# F1 = len(listFamily_1) #считаем кол-во
# F2 = len(listFamily_2)
# print(F1)
# print(F2)
# if F1<F2:
#     print('Family 2 is bigger than Family 1')
# elif F1>F2:
#     print('Family 1 is bigger than Family 2')
# else:
#     print('Equal')

#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# my_dict = {
#     'title': 'Лара Крофт',
#     'director': '?',
#     'year': '?',
#     'budget': '100000000',
#     'main_actor': 'Анджелина Джоли',
#     'slogan': 'Вперед!'}
# print(my_dict)
# for key in my_dict.keys():
#     print(key)
# for value in my_dict.values():
#     print(value)



# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# total = sum(my_dictionary.values())
# print(total)
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# ints_list = [1, 2, 3, 4, 5, 3, 2, 1]
# ints_list1 = list(set(ints_list))
# print(ints_list1)
#
# ints_list = [1, 2, 3, 4, 3, 2]
# temp = []
# for x in ints_list:
#     if x not in temp:
#         temp.append(x)
# ints_list = temp
# print(f'Updated List after removing duplicates = {temp}')


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))