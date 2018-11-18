# 1. 导包
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")
# driver.get(r"D:\webAutoTest\page\drag.html")

# 4. 业务操作
# 鼠标右键
# 在用户名文本框上点击鼠标右键
# 实例化对象
# action = ActionChains(driver)
# # 调用鼠标右键方法
# action.context_click(driver.find_element_by_id("userA"))
# # 提交
# action.perform()
#
# ActionChains(driver).context_click(driver.find_element_by_id("userA")).perform()


# 鼠标双击
# 给用户名设置为admin,暂停3秒钟后双击鼠标左键，选中admin
# driver.find_element_by_id("userA").send_keys("admin")
# time.sleep(3)
# ActionChains(driver).double_click(driver.find_element_by_id("userA")).perform()


# 鼠标拖拽
# 把红色框拖拽到蓝色框上
# div1 = driver.find_element_by_id("div1")
# div2 = driver.find_element_by_id("div2")
# ActionChains(driver).drag_and_drop(div1, div2).perform()


# 鼠标悬停
# 将鼠标悬停在“注册用户A”按钮上
ActionChains(driver).move_to_element(driver.find_element_by_tag_name("button")).perform()

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
