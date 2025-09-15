############### Mixing Operators ##########
# expression = (1>2) and (3==4)
# expression = 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
# print(expression)

############## if statement ##################
# name = "hoang"
#
# if name == "stephen":
#     print("Hello, stephen")
# elif name == "hoang":
#     print("Hello, hoang")
# else:
#     print("Who are you?")

############# Ternary Conditional Operator ##########
# <expression1> if <condition> else <expression2>
# print("-----------")
# name = "hoang"
# print("stephen" if (name =="stephen") else "hoang" if (name =="hoang") else "Who are you?")



############  match - case #############
# response_code = 200
# isHandSome = False
# match response_code:
#     case 200 | 201:
#         print("OK handsome" if isHandSome else "OK ugly")
#     case 300 | 307:
#        print("Redirect")
#     case 400 | 401:
#         print("Bad Request")
#     case _:
#         print("Invalid Code")

# Matching Builtin Classes
# response_code = [1,2,4]
# match response_code:
#     case int(): print("Code is number")
#     case str(): print("Code is string")
#     case _: print("Code is neither a string not a number")


############## while Loop Statements #################
######### break
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1

######### continue
# i = 1
# while i <= 10:
#     if i < 5:
#         i+= 1
#         continue
#     print(i, end=" ")
#     i += 1

# while True:
#     name = input("Who are you?")
#     if name != "John":
#         continue
#     while True:
#         password = input("Enter the password")
#         if password == "1911":
#             print("Successful access!")
#             break
#     break

################# For loop ##############
# Duyệt list (array), string, dictionary, set, tuple

# countries = ["China", "USA", "ThaiLand", "HongKong"]
# for country in countries:
#     print(f"Hello {country}!")

#### The range(n) function: 0 -> n - 1
# for i in range(10):
#     print(i, end=" ")


#### The range(start, stop, step)

# for i in range(1, 8, 2):
#     print(i, end=" ")

###### loop count down
# for i in range(1, -8, -1):
#     print(i, end=" ")


############## For else statement ############
# else được thực hiện khi đã chạy hết vòng lặp, phù hợp khi tìm kiếm phần tử trong list.
# key = 8
# for i in [1, 2, 3, 4, 5, 6]:
#     if i == key:
#         break
# else:
#     print(f"only executed when no item is equal to 3. Not found item equals {key}")


################ Ending a Program with sys.exit() ################
# import sys
#
# while True:
#     feedback = input("Enter the feedback: ")
#     if feedback == "exit":
#         print("You type \"exit\"")
#         sys.exit()