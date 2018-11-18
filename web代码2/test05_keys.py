# 1. 导包
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 1)输入用户名：admin1，暂停2秒 删除1
element = driver.find_element_by_id("userA")
element.send_keys("admin1")
time.sleep(2)
element.send_keys(Keys.BACK_SPACE)

# 2)全选用户名：admin，暂停2秒
element.send_keys(Keys.CONTROL, 'a')
time.sleep(2)

# 3)复制用户名：admin，暂停2秒
element.send_keys(Keys.CONTROL, 'c')
time.sleep(2)

# 4)粘贴到密码框
driver.find_element_by_id("passwordA").send_keys(Keys.CONTROL, 'v')

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
