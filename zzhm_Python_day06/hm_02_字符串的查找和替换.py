# 字符串的查找与替换:
# 1. 查找
#       a) s.startswith(子字符串):判断字符串s是否以参数指定的子字符串开头(区分大小写)
#                               方法的返回值为布尔值
#       b) s.endswith(子字符串):判断字符串s是否以参数指定的子字符串结尾
#                             方法的返回值为布尔值
#       c) s.find(子字符串): 从s中查找参数指定的子串
#                           如果存在，返回子串位于原串中的索引值；如果不存在，返回值为-1
#          注意：与index()的区别
# 2.替换:
#       s.replace(old_substr, new_substr)
#       方法的返回值为替换后的结果字符串。
#       注意：原串没有改变

s = "python is short, you need C!"
# 1> 判断s是否以life开头
print(s.startswith("life"))

# 2> 查看s中是否存在字符串python，如果存在将其替换为python3
print("s.find() = ", s.find("python"))

if s.find("python"):
    print("if...")
    print(s.replace("python", "python3"))
else:
    print("未找到python！")