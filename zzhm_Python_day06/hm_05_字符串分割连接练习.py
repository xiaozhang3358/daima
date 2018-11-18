s =  "\t  Life is short, you need python!   "

# 1> 去除字符串两端的空白字符strip()
s = s.strip()
print("去除两端空白字符:|%s|" % s)

# 2> 计算字符串中有多少单词（以空格分隔的为一个单词）
# 分割字符串:用空格
l_s = s.split()
print("分割后的结果:", l_s)
print("单词数量:", len(l_s))

# 3> 计算最后一个单词的长度
# 1.获取最后一个单词
length_list = len(l_s)
index_last = length_list - 1
print("最后一个词:", l_s[index_last])
# 2.求单词长度
print("最后一个词的长度:", len(l_s[index_last]))

# 4> 输出内容:"Lifeisshort,youneedpython!"
print("连接后的结果:",  " ".join(l_s))


