# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 1>选择‘广州’
# 2>暂停2秒，选择‘上海’
# 3>暂停2秒，选择‘北京’

# 通过元素定位的方式来实现，即定位到要选择的option元素，然后执行点击操作
# driver.find_element_by_xpath("//option[@value='gz']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//option[@value='sh']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//option[@value='bj']").click()


# 通过Select类来实现
# 创建对象
select = Select(driver.find_element_by_id("selectA"))
# 调用方法
select.select_by_index(2)  # 通过索引选择
time.sleep(2)
select.select_by_value("sh")  # 通过option的value属性选择
time.sleep(2)
select.select_by_visible_text("A北京")  # 通过文本内容操作

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
