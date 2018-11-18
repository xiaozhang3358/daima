# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()

# 3. 打开网站
driver.get(r"http://www.baidu.com")
time.sleep(2)

# 4. 业务操作
# 登陆百度，获取cookie
# 使用获取的cookie，在WebDriver中，添加Cookie，达到登陆目的
# itest2018 test123456
cookie = {
    "name": "BDUSS",
    "value": "TVac3VNcWIxN2tsV0JGdjU1bXJicDBYUVNTckdGcURNVWV6bGF3d2ZpZENGZGhiQVFBQUFBJCQAAAAAAAAAAAEAAAAlASDSaXRlc3QyMDE4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEKIsFtCiLBbZ",
    "path": "/"
}
driver.add_cookie(cookie)

driver.refresh()

print("cookie=", driver.get_cookie("BAIDUID"))
print("cookies=", driver.get_cookies())



# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动对象
driver.quit()
