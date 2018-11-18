# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Chrome()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 通过css定位id选择器定位用户名输入框
# driver.find_element_by_css_selector("#userA").send_keys("admin")

# 通过css定位class选择器定位电话号码输入框
# driver.find_element_by_css_selector(".telA").send_keys("1861111111")

# 通过css定位元素选择器定位用户名输入框
# driver.find_element_by_css_selector("input").send_keys("123")

# 通过css定位属性选择器定位密码输入框
# driver.find_element_by_css_selector("input[type='password']").send_keys("123456")

# 通过css定位层级选择器定位用户名输入框
# driver.find_element_by_css_selector("p[id='p1']>input").send_keys("admin")
# driver.find_element_by_css_selector("p[id='p1'] input").send_keys("admin")
driver.find_element_by_css_selector("p#p1 input").send_keys("admin")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
