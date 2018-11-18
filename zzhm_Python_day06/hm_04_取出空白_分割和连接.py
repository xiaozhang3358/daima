# s.strip()
s = "   hello   world,   hello python!\t  \n"
print("|%s|" % s)
# print("|%s|" % s.lstrip())
s = s.strip()

# split():分割字符串，得到了一个列表数据
l_s = s.split()
for item in l_s:
    print("word:", item)
# join()
# 打印一个字符串“hello---world,---hello---python!"
# sep.join(可迭代数据) 可迭代数据中包含若干个子字符串

print("---".join(l_s))
print("*".join("hello"))
