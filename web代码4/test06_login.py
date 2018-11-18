"""
需求：使用UnitTest框架对tpshop项目的登录功能测试
1. 点击登录，进入登录页面
2. 输入用户名和密码，不输入验证码，直接点击登录按钮
3. 获取错误提示信息
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
