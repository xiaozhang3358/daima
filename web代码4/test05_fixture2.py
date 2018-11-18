# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时长
# time.strftime("%Y-%m-%d %H:%M:%S")
import time
import unittest


class TestFixture(unittest.TestCase):

    # 初始化、前置处理
    # 首先自动执行
    # 作用于测试类中的每一个测试方法
    def setUp(self):
        print("start time=", time.strftime("%Y-%m-%d %H:%M:%S"))

    # 销毁、后置处理
    # 最后自动执行
    # 作用于测试类中的每一个测试方法
    def tearDown(self):
        print("end   time=", time.strftime("%Y-%m-%d %H:%M:%S"))

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")
