# # ------Python 字典(Dictionary)------
# # 字典是另一种可变容器模型，且可存储任意类型对象。
# # 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# # d = {key1 : value1, key2 : value2 }
# # 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
# dict = {'a': 1, 'b': 2, 'b': '3'}
# print(dict['b'])
# print(dict)
# # 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# dict1 = { 'abc': 456 }
# dict2 = { 'abc': 123, 98.6: 37 }

# ------访问字典里的值------
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Alice']: ", dict['Alice'])