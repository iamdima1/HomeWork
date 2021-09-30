# www = 'www.google.com'
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")

# www = 'www.conquer_and_command.net'
# if ".com" in www:
#     print("com in www")
# else:
#     print("com not in www")


# value = "123456789"
# my_str = value if len(value) <= 5 else value [2:5:2]
# print(my_str[::-1])




#
# my_str1= "My name is Vova. I am a teacher !"
# for symbol in my_str1:
#     if not symbol.isupper() and symbol.isalpha():
#         print(symbol)
# #####################################################################################################################

# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число

# value = input("Укажите число:")
# value = int(value)
# new_value = int()
# new_value = value // 2 if value < 100 else -value
# print("Результат",new_value)

###################################

#2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0
# value = input("Укажите число:")
# value = int(value)
# new_value_1 = 1
# new_value_1 = int(new_value_1)
# new_value_0 = 0
# new_value_0 = int(new_value_0)
#
# if value < 100:
#     print("Результа:", new_value_1)
# else:
#     print(new_value_0)


###################################

# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False

# value = input("Укажите число:")
# value = int(value)
# new_value = bool()
# new_value =  if value < 100 else
# print("Результат",new_value)

###############################
# 4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
# my_str = "AaBbCc"
# my_str = str(my_str)
# print(my_str.upper())
##################################

#5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
# my_str = "AaBbCc"
# my_str = str(my_str)
# print(my_str.lower())
#########################

# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример:
# было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
# my_str = input()
# my_str = str(my_str)
# my_str_1 = str()
# my_str_1 = my_str * 2 if not len(my_str) > 5 else my_str
# print(my_str_1)

# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же. Пример:
# было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
# my_str = input()
# my_str = str(my_str)
# my_str_1 = str()
# my_str_1 = my_str * 2 if not len(my_str) <= 5 else my_str
# print(my_str_1)














