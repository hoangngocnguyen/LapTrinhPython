'''
    List comprehension
'''

names = ['Charles', 'Susan', 'Patrick', 'George']
new_list1 = names  # Tham chiếu cùng một vùng nhớ với [names]
print(new_list1)

# new_list2 = []      # Sử dụng một vùng nhớ mới
# for n in names:
#     new_list2.append(n)
# print(new_list2)
# print(new_list1 == new_list2)   # cách so sánh 2 list, so sánh theo thứ tự phần tử

new_list3 = [n for n in names]
print(f"list 3: {new_list3}")


name_start_with_c = [name for name in names if name.startswith('C')]
print(name_start_with_c)
