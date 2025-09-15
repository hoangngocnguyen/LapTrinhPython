
############ Tạo một function #############
# def say_hello(name, greeting):
#     print(f"{greeting}, {name}")
#
# # without keyword arguments
# say_hello("Jim", "Hello")
#
# # Sử dụng Keyword Arguments để cho code dễ đọc, rõ ràng
# say_hello(greeting="Hello", name="John")
#
#
# print('-------------------')
# def sum_two_numbers(a, b):
#     return a + b;
#
# print(sum_two_numbers(1, 2))


################## Local and Global Scope ##############
# global_variable = 1911
# def some_function():
#     global global_variable
#     global_variable += 1
#     print(f'Global variable is {global_variable}')
#
#
# some_function()     # 1912
# print(f'Global variable is {global_variable}')      #1912


# global_variable = 1911
# def some_function():
#     global_variable = 5
#     global_variable += 1
#     print(f'Global variable is {global_variable}')
#
#
# some_function()     # 6
# print(f'Global variable is {global_variable}')      #1911


#################### Lambda Functions ###########
# def add(a,b):
#     return a+b
# print(add(1, 2))
#
# # is equivalent
# add = lambda a, b: a+b
# print(add(1, 2))

# Hàm lồng nhau (closure)
# def make_adder(n):
#     def adder(x):
#         return n + x
#     return adder    # trả về một function adder(x)
#
# print(make_adder(3)(4))     # n = 3, x = 4
#
# # để dễ hiểu hơn, ta tách ra
# adder_3 = make_adder(3)
# print(adder_3(4))
