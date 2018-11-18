stds = [
    {"name" : "小明"},
    {"name" : "小美"}
]
find_std = "小李"
# for循环的完整结构:for...else
# 当循环正常终止时，else分支会执行且被执行一次
# 如果循环未正常终止（在循环中break退出），else分支不执行
for std in stds:
    print("in for, std:", std)
    if std["name"] == find_std:
        print("找到了, %s" % find_std)
        break
else:
    print("未找到！")

print("循环体外!")