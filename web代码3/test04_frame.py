# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册实例.html")

# 4. 业务操作
# frame切换
# 先填写最上边注册信息
driver.find_element_by_id("user").send_keys("admin")

# 切换到注册A页面
# driver.switch_to.frame("idframe1")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# 其次填写注册A页面注册信息
driver.find_element_by_id("userA").send_keys("admin")

# 切换到主页面
driver.switch_to.default_content()

# 切换到注册B页面
driver.switch_to.frame("myframe2")

# 最后填写注册B页面信息
driver.find_element_by_id("userB").send_keys("admin")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
