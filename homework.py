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





my_str1= "My name is Vova. I am a teacher !"
for symbol in my_str1:
    if not symbol.isupper() and symbol.isalpha():
        print(symbol)