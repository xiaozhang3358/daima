# 导包
import unittest
from day05.test01_testcase import TestAdd
from day05.test02_testcase2 import TestSub
from day05.tools.HTMLTestRunner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()
suite.addTest(TestSub("test_sub01"))
suite.addTest(TestAdd("test_add01"))
suite.addTest(TestAdd("test_add02"))

# 定义测试报告存在路径
report_path = "./report/report.html"

# 打开文件
with open(report_path, "wb") as f:
    # 创建HTMLTestRunner运行器对象
    runner = HTMLTestRunner(f, title="TPshop自动化测试报告", description="Win10.Firefox")

    # 执行
    runner.run(suite)
