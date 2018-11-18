# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Chrome()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\xpath-层级与属性.html")

# 4. 业务操作
driver.find_element_by_xpath("//p[@id='login-t1']/input").send_keys("123456")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
