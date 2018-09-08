from selenium import webdriver
from lxml import etree
import time

userName = '用户名'
passWord = '密码'
driver = webdriver.Chrome()
driver.get('https://weibo.cn/1624923463/follow')
driver.implicitly_wait(10)


user = driver.find_element_by_id('loginName')
user.send_keys(userName)
pwd = driver.find_element_by_id('loginPassword')
pwd.send_keys(passWord)
driver.find_element_by_id('loginAction').click()
driver.find_element_by_xpath('/html/body/div[2]/a[3]').click()
search_people = driver.find_element_by_name('keyword')
search_people.send_keys('华晨宇yu') #微博ID
driver.find_element_by_css_selector('body > div:nth-child(4) > form > div > input[type="submit"]:nth-child(3)').click()
driver.find_element_by_css_selector('body > table:nth-child(9) > tbody > tr > td:nth-child(2) > a').click()
driver.find_element_by_css_selector('body > div.u > div > a:nth-child(2)').click()

while True:
    html = driver.page_source.encode('utf-8')
    e = etree.HTML(html)
    search = '/html/body/table/tbody/tr/td[2]/a[1]/text()'
    s2 = e.xpath(search)
    print(e.xpath(search))
    time.sleep(0.1)
    try:
        driver.find_element_by_link_text('下页').click()
    except:
        break


