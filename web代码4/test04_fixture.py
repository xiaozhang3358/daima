# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时长
# time.strftime("%Y-%m-%d %H:%M:%S")
import time
import unittest

class TestFixture(unittest.TestCase):

    def before(self):
        print("start time=", time.strftime("%Y-%m-%d %H:%M:%S"))

    def after(self):
        print("end   time=", time.strftime("%Y-%m-%d %H:%M:%S"))

    def test01(self):
        self.before()
        print("test01")
        self.after()


    def test02(self):
        self.before()
        print("test02")
        self.after()
