# 1. 导包
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 通过find_element方法定位用户名输入框，输入：admin
# 快捷导包：alt + 回车
driver.find_element(By.ID, "userA").send_keys("admin")

# 查看源代码快捷键：按住ctrl，移动鼠标到方法名或类名上，然后点击
driver.find_element_by_id("userA")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
