# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Chrome()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 最大化浏览器窗口
# driver.maximize_window()

# 设置浏览器窗口大小
# driver.set_window_size(200, 300)

# 设置浏览器窗口位置
# driver.set_window_position(200, 100)

# 后退
# driver.find_element_by_link_text("AA 新浪 网站").click()
# driver.back()

# 前进
# driver.forward()

# 刷新
# driver.refresh()

# 关闭当前窗口，只关闭一个窗口
# driver.close()

# 获取页面title
print("title=", driver.title)

# 获取当前页面URL
print("url==", driver.current_url)


# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
# 退出驱动，并关闭所有窗口
driver.quit()
