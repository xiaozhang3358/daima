# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 使用tag_name获取第二个元素(密码框)
element_list = driver.find_elements_by_tag_name("input")
print(len(element_list))
element = element_list[1]
# element.send_keys("admin")

# 简单写法
driver.find_elements_by_tag_name("input")[1].send_keys("admin")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
