# 1.	从键盘上获取信息，
#       判断是否可转换为数字，
#       如果是，转换为整数。

# 从键盘接收一个字符串数据
s = input("输入数据:")
print("type(s)", type(s)) #"abcd", "1234"

print("isdecimal:", s.isdecimal())
# 判断字符串是否可转换为整数
if s.isdecimal() == True:
    # 完成类型转换：转成整数 int(s)
    n = int(s)
    print("type(n) = ", type(n))
    print("n = %d" % n)
else:
    print("输入的数据不可转换为整数！")