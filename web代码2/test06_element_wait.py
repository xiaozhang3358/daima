# 1. 导包
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"D:\webAutoTest\page\注册A.html")

# 4. 业务操作
# 显式等待
# 如果用户名文本框存在，就输入admin
# try:
#     print("start time=", time.strftime("%Y%m%d %H:%M:%S"))
#     locator = (By.ID, "userA666")
#     element = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(locator))
#     element.send_keys("admin")
# except Exception as e:
#     print(type(e))
#     print("end   time=", time.strftime("%Y%m%d %H:%M:%S"))

# 隐式等待
try:
    print("start time=", time.strftime("%Y%m%d %H:%M:%S"))
    driver.implicitly_wait(10)

    driver.find_element_by_id("userA666").send_keys("admin")
except Exception as e:
    print(type(e))
finally:
    print("end   time=", time.strftime("%Y%m%d %H:%M:%S"))


# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
