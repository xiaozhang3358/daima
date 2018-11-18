# 导包
import unittest


# 定义测试类，必须要继承TestCase
# 类的名称建议以Test开头
class TestSub(unittest.TestCase):

    # 方法名称必须以test开头
    def test_sub01(self):
        print("test_sub01")

    def test_sub02(self):
        print("test_sub02")