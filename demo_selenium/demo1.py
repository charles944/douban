from selenium import webdriver
from lxml import html
from selenium.webdriver import ActionChains

broswer=webdriver.Chrome()
# url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
url='https://www.douban.com'
broswer.get(url)
# broswer.switch_to.frame('iframeResult')
print(broswer.get_window_position())
print(broswer.get_window_rect())
print(broswer.get_window_size())
# source=broswer.find_element_by_css_selector('#draggable')
# target=broswer.find_element_by_css_selector('#droppable')
actions=ActionChains(broswer)
# actions.drag_and_drop(source,target)
ActionChains(broswer).move_by_offset(900, 100).context_click().perform()
# actions.perform()
print('拖动任务完成')
