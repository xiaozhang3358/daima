# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Chrome()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 使用绝对路径和相对路径分别实现，账号A：admin; 然后输入：123
# 绝对路径
# driver.find_element_by_xpath("/html/body/div/fieldset/p[1]/input").send_keys("admin")
# 相对路径
# driver.find_element_by_xpath("//input").send_keys("123")


# 使用相对路径分别实现，账号A：admin;密码A：123456；
driver.find_element_by_xpath("//input[@name='userA']").send_keys("admin")
driver.find_element_by_xpath("//*[@type=\"password\"]").send_keys("123456")


# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
