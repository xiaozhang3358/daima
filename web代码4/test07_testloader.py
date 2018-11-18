import unittest


# 使用TestLoader自动加载测试套件
# suite = unittest.defaultTestLoader.discover("./case/", pattern="test*.py")
suite = unittest.TestLoader().discover("./case/", pattern="test*.py")

unittest.TextTestRunner().run(suite)








