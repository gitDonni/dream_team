# #1
#
# text = input('Введите текст на анлийском: ')
#
# glasnye = ['e', 'y', 'u', 'i', 'o', 'a']
# def del_glas(text):
#     text2 = ''
#     for i in text:
#         if i.lower() not in glasnye:
#             text2 += i
#     return text2
#
#
#
# print(del_glas(text))



##3

#
# list_1 = ['123', 'abc', 'de']
# list_2 = ['1', '23', 'abcde']
#
# def lst_func(list_1, list_2):
#     new_lst1 = ''
#     new_lst2 = ''
#     for a in list_1:
#         new_lst1 += a
#     for b in list_2:
#         new_lst2 += b
#     if new_lst1 == new_lst2:
#         print(new_lst1, 'равен', new_lst1)
#     else:
#         print(new_lst1, 'не равен', new_lst2)
#
# lst_func(list_1, list_2)



#5



# uniques = {3, 13, 15, 27, 1, 4, 8, 23, 19, 12, 9, 2, 17}
#
# def sorted_set(uniques):
#     uniques = {i for i in uniques if i % 2 != 0}
#     sorted_uniques = sorted(uniques, reverse=True)
#     print(sorted_uniques)
#
#
# sorted_set(uniques)


#7


keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6, 'six', 7, 'seven', 'eight', 8, 'nine', 9, 10, 'ten', 11, '11', 12, '13')


pairs = {}


for i in range(0, len(keys_values), 2):
        key = keys_values[i]
        value = keys_values[i + 1]

        if isinstance(key, str):
            pairs[key] = value


print(pairs)


