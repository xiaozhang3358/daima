"""
需求：
1. 打开tpshop网站
2. 点击登录，进入登录页面
3. 输入用户名和密码，不输入验证码，直接点击登录按钮
4. 获取错误提示信息
5. 断言错误提示信息是否为“验证码不能为空!”，如果断言失败则保存截图
"""

import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. 点击登录，进入登录页面
        driver = self.driver
        driver.find_element_by_link_text("登录").click()

        # 2. 输入用户名和密码，不输入验证码，直接点击登录按钮
        driver.find_element_by_id("username").send_keys("13012345678")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_name("sbtbutton").click()

        # 3. 获取错误提示信息
        msg = driver.find_element_by_class_name("layui-layer-content").text
        print("msg=", msg)
        time.sleep(2)

        # 5. 断言错误提示信息是否为“验证码不能为空!”，如果断言失败则保存截图
        try:
            self.assertIn("验证码不能为空666", msg)
        except AssertionError as e:
            # 截图操作
            driver.get_screenshot_as_file("./img/img.png")
            # 使用raise关键字继续向外抛出异常
            raise

        print("1111")