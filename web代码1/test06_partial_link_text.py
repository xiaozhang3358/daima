# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 使用partial_link_text定位(访问 新浪 网站)超链接，并点击
# 传递的参数必须要是连续的，尽量保证是唯一的
driver.find_element_by_partial_link_text("访问 新浪").click()

# 错误写法
# driver.find_element_by_partial_link_text("访问 网站").click()


# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
