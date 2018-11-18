# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 首先点击alerta按钮，其次输入用户名：admin
driver.find_element_by_id("alerta").click()
time.sleep(2)

# 关闭弹出框
# 1>获取弹出框对象
alert = driver.switch_to.alert

# 获取弹出框的提示消息
print("text=", alert.text)

# 2>调用对象的关闭方法
# alert.accept()  # 点击确定按钮
alert.dismiss()  # 点击取消按钮

# 输入用户名
driver.find_element_by_id("userA").send_keys("admin")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
