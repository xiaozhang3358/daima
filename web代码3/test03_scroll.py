# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 滚动条操作
# 打开页面2秒后，滚动条拉倒最底层
time.sleep(2)
# 定义js脚本
js = "window.scrollTo(0, 1000000)"
# 调用执行js脚本的方法
driver.execute_script(js)

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
