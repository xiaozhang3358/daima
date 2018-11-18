# 实现加法操作
def add(x, y):
    return x + y


# 导包
import unittest


# 定义测试类，必须要继承TestCase
# 类的名称建议以Test开头
class TestAdd(unittest.TestCase):

    def test_add02(self):
        result = add(1, 2)
        print("result222=", result)

    # 方法名称必须以test开头
    def test_add01(self):
        result = add(1, 1)
        print("result111=", result)




if __name__ == '__main__':
    unittest.main()
