# 实现加法操作
def add(x, y):
    return x - y


import unittest


class TestAssert(unittest.TestCase):

    def test_add01(self):
        result = add(1, 1)
        print("result111=", result)

        self.assertEqual(2, result)

    def test_add02(self):
        result = add(1, 2)
        print("result222=", result)

        # 判断两个参数是否相等
        # self.assertEqual(3, result)

        # 判断第一个参数是否为第二个参数的子串
        # self.assertIn("admin2", "你好admin")

        # 判断参数是否存在在列表中
        self.assertIn("5", ["1", "2", "3"])
