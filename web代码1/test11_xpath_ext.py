# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Chrome()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# //*[text()="xxx"]                            文本内容是xxx的元素
# driver.find_element_by_xpath("//*[text()='访问 新浪 网站']").click()

# //*[starts-with(@attribute,'xxx')]                属性以xxx开头的元素
# driver.find_element_by_xpath("//*[starts-with(@name, 'user')]").send_keys("123456")

# //*[contains(@attribute,'Sxxx')]                属性中含有xxx的元素
driver.find_element_by_xpath("//*[contains(@name, 'ser')]").send_keys("1234")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
