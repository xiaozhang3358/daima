# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
# driver.get("file:///D:/webAutoTest/page/%E6%B3%A8%E5%86%8CA.html")
# driver.get("D:\\webAutoTest\\page\\注册A.html")
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 1>定位用户名输入框，输入：admin
element = driver.find_element_by_id("userA")
element.send_keys("admin")

# 2>定位密码输入框，输入：123456
driver.find_element_by_id("passwordA").send_keys("123456")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
