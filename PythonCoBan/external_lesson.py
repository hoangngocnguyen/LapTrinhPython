"""
    Python Dictionaries
"""
import pprint

person1 = {
    'name': 'hoàng',
    'age': 19,
    'isHandsome': True
}

person1['say'] = 'Tôi đẹp trai nhất thế giới'
print(person1)

print('--------------')
print('--------------Lấy giá trị thông qua key')
print(person1['say'])
print("Sử dụng .get() để in giá trị:", person1.get('say'))
print("Sử dụng .get() để in giá trị:", person1.get('speak'))
print("Sử dụng .get() để in giá trị:", person1.get('speak', 'english'))     # Nếu None thì lấy ra 'english'


print('--------------')
print('--------------')
print(person1.values())     # In ra mảng các [values] trong dictionary
print(person1.keys())       # In ra mảng các [keys]


print('--------------')
print('--------------')
for key in person1:         # Mặc định vòng lặp sẽ lặp qua các [keys].
    print(key)


print('--------------')
print('--------------')
print(person1.items())      # Trả về một tuple các [items] của dictionary


print('--------------Sử dụng tổng hợp, lặp và lấy ra key, item')
for key, value in person1.items():
    print(f'Key: {key}; value: {value}')


'''
    Adding items with setdefault(). Thêm một item vào dictionary (nếu chưa có)
'''
print('--------------')
print('--------------Adding items with setdefault(). Thêm một item vào dictionary (nếu chưa có)')
girlfriend = {'name': 'Cindy', 'age': 18}
# girlfriend['name'] = 'Jena'

if 'name' not in girlfriend:
    girlfriend['name'] = 'Sarah'

print(f'Girlfriend\'s name: {girlfriend}')

# Có thể dùng cái này:
girlfriend.setdefault('boyfriend', 'Hoàng')

print(f'Boyfriend cua {girlfriend.get("name")} là {girlfriend.get("boyfriend")}')


'''
    Removing Items
'''
print('--------------')
print('--------------Removing Items: pop, popitem, del, clear.')
girlfriend = {'name': 'Cindy', 'age': 18}

pop_age = girlfriend.pop('age')
print(pop_age)

#
girlfriend = {'name': 'Cindy', 'age': 18}

pop_item_age = girlfriend.popitem()
print(pop_item_age[0])

#
girlfriend = {'name': 'Cindy', 'age': 18}
pprint.pprint(girlfriend)


print('--------------')
"""
    Merge two dictionaries
"""
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
dict_c = {**dict_a, **dict_b}       # Giống như spread của js

print(dict_c)

    







