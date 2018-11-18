# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 1>通过脚本执行输入 用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com;
driver.find_element_by_id("userA").send_keys("admin")
driver.find_element_by_id("passwordA").send_keys("123456")
driver.find_element_by_id("telA").send_keys("18611111111")
driver.find_element_by_id("emailA").send_keys("123@qq.com")

# 2>间隔3秒后，修改电话号码为：18600000000
time.sleep(3)
# 注意：修改操作==先清空再输入新的内容
driver.find_element_by_id("telA").clear()
driver.find_element_by_id("telA").send_keys("1860000000")

# 3>间隔3秒，点击 注册用户A 按钮
time.sleep(3)
driver.find_element_by_tag_name("button").click()

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
