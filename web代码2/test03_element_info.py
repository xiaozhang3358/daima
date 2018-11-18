# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Chrome()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 获取元素大小--获取用户名输入框的元素大小
size = driver.find_element_by_id("userA").size
print("size=", size)

# 获取元素的文本--获取超链接元素的文本内容
text = driver.find_element_by_id("fw").text
print("text=", text)

# 获取属性值--获取用户名输入框的placeholder属性值
placeholder = driver.find_element_by_id("userA").get_attribute("placeholder")
print("placeholder=", placeholder)

# 判断元素是否可见--判断页面中的span标签是否可见
is_displayed = driver.find_element_by_tag_name("span").is_displayed()
print("is_displayed=", is_displayed)

# 判断元素是否可用--判断页面中的‘取消A’按钮是否可用
is_enabled = driver.find_element_by_id("cancelA").is_enabled()
print("is_enabled=", is_enabled)

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
