from selenium import webdriver

broswer=webdriver.Chrome()
broswer.get("https://www.douban.com")
app=broswer.find_element_by_xpath("//a[contains(@href,'https://www.douban.com/doubanapp/app?channel=nimingye')]")
app.click()