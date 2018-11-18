from time import sleep

from appium import webdriver
def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['automationName'] = 'Uiautomator2'
    # 设置中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app的信息 com.tencent.news/.activity.SplashActivity
    desired_caps['appPackage'] = 'com.tencent.news'
    desired_caps['appActivity'] = '.activity.SplashActivity'
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver=get_driver()
# 隐式等待
driver.implicitly_wait(30)
# 如何获取当前环境 是native还是webview
print("点击之前_获取当前环境为：",driver.context)
print("点击之前_获取所有环境：",driver.contexts)
# 点击第一条新闻
driver.find_element_by_xpath("//*[contains(@text,'习近平出席首届中国国际进口博览会开幕式并发表主旨演讲')]").click()
# 获取所有的环境
print("点击之后_获取所有环境：",driver.contexts)
# 打印当前默认环境
print("点击之后_获取当前默认环境为：",driver.context)
# 切换方法
driver.switch_to.context("WEBVIEW_com.tencent.android.qqdownloader")
# 打印切换后的环境
print("切换后的环境为：",driver.context)
# 使用selenium定位文本元素  获取所有文本
print(driver.find_element_by_css_selector('p').text)
sleep(30)
driver.quit()