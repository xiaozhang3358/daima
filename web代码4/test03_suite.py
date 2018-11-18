# 导包
import unittest
from day05.test01_testcase import TestAdd
from day05.test02_testcase2 import TestSub

# 实例化测试套件对象
suite = unittest.TestSuite()

# 添加测试用例
# 第一种方式
suite.addTest(TestSub("test_sub01"))
suite.addTest(TestAdd("test_add01"))
suite.addTest(TestAdd("test_add02"))


# 第二种方式
# suite.addTest(unittest.makeSuite(TestAdd))
# suite.addTest(unittest.makeSuite(TestSub))

# 创建测试用例的运行器
unittest.TextTestRunner().run(suite)
