#------------------------Python 循环语句----------------------------
# 本章节将向大家介绍Python的循环语句，程序在一般情况下是按顺序执行的。
# 编程语言提供了各种控制结构，允许更复杂的执行路径。
# 循环语句允许我们执行一个语句或语句组多次

# Python      提供了 for 循环和 while 循环（在 Python 中没有 do..while 循环）:
# while 循环	  在给定的判断条件为 true 时执行循环体，否则退出循环体。
# for 循环	  重复执行语句
# 嵌套循环	  你可以在while循环体中嵌套for循环

# ------循环控制语句------
# 循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：
# break 语句	    在语句块执行过程中终止循环，并且跳出整个循环
# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
# pass 语句	    pass是空语句，是为了保持程序结构的完整性。


# ---------------------------------------Python While 循环语句-----------------------------

# Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
# while 判断条件(condition)：
#     执行语句(statements)……

# a=0
# count = 0
# while (a<11):
# 	count=count+a
# 	a = a + 1
# print(count)

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
# continue 用于跳过该次循环，
# break 则是用于退出循环，
# 此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：

# ------continue 和 break 用法------
 
# i = 1
# while i < 10:   
#     i += 1
#     if i%2 > 0:     # 非双数时跳过输出
#         continue
#     print (i)         # 输出双数2、4、6、8、10
 
# i = 1
# while 1:            # 循环条件为1必定成立
#     print (i)         # 输出1~10
#     i += 1
#     if i > 10:     # 当i大于10时跳出循环
#         break

# ------无限循环------
# 如果条件判断语句永远为 true，循环将会无限的执行下去，如下实例：

# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#    num = input("Enter a number  :")
#    print ("You entered: ", num)
# print ("Good bye!")

# 注意：以上的无限循环你可以使用 CTRL+C 来中断循环。

# ------循环使用 else 语句------
# 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：

# count = 0
# while count < 5:
#    print (count, " is  less than 5")
#    count = count + 1
# else:
#    print (count, " is not less than 5")


 # ------简单语句组------
 # 类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

# flag = 1
# while (flag): print ('Given flag is really true!')
# print ("Good bye!")



# ------------------------------------Python for 循环语句------------------------------------

# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# ------for循环的语法格式------

# for letter in 'Python':     # 第一个实例
#    print ('当前字母 :', letter)
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # 第二个实例
#    print ('当前水果 :', fruit)
# print ("Good bye!")

# ------通过序列索引迭代------

# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#    print ('当前水果 :', fruits[index])
# print ("Good bye!")

# ------循环使用 else 语句------

# for num in range(10,20):  # 迭代 10 到 20 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          j=num/i          # 计算第二个因子
#          print ('%d 等于 %d * %d' % (num,i,j))
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       print (num, '是一个质数')

# ------Python 循环嵌套------
# 以下实例使用了嵌套循环输出2~100之间的素数：
# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j): break
#       j = j + 1
#    if (j > i/j) : print (i, " 是素数")
#    i = i + 1
 
# print ("Good bye!")



# # ------Python break 语句------
# # Python break语句，就像在C语言中，打破了最小封闭for或while循环。
# # break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
# # break语句用在while和for循环中。
# # 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       break
#    print ('当前字母 :', letter)
  
# var = 10                    # 第二个实例
# while var > 0:              
#    print ('当前变量值 :', var)
#    var = var -1
#    if var == 5:   # 当变量 var 等于 5 时退出循环
#       break
 
# print ("Good bye!")



# # ------Python continue 语句------
# # Python continue 语句跳出本次循环，而break跳出整个循环。
# # continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# # continue语句用在while和for循环中。
# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       continue
#    print ('当前字母 :', letter)
 
# var = 10                    # 第二个实例
# while var > 0:              
#    var = var -1
#    if var == 5:
#       continue
#    print ('当前变量值 :', var)
# print ("Good bye!")
# # continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:
# var = 10
# while var > 0:
#     var = var -1
#     if var == 5 or var == 8:
#         continue
#     print ('当前值 :', var)
# print ("Good bye!")
# # 我们想只打印0-10之间的奇数，可以用continue语句跳过某些循环：
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:      # 如果n是偶数，执行continue语句
#         continue        # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)



# # ------Python pass 语句------
# # Python pass 是空语句，是为了保持程序结构的完整性。
# # pass 不做任何事情，一般用做占位语句。
# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print ('这是 pass 块')
#    print ('当前字母 :', letter)
# print ("Good bye!")
