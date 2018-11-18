# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 通过class_name定位电话号码A，并发送18611111111
driver.find_element_by_class_name("telA").send_keys("18611111111")

# 定位邮箱输入内容
# 错误写法
# driver.find_element_by_class_name("emailA dzyxA").send_keys("123@qq.com")
# 如果存在多个属性值的话，只能使用其中的一个
driver.find_element_by_class_name("emailA").send_keys("123@qq.com")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
