from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)
time.sleep(2)

my_id = 'id967'
my_pw = 'rlawogus9869'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

comu_url =  'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(1)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)

driver.switch_to.frame('cafe_main')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

for i in range(20):
    content = driver.find_element_by_css_selector('div.se-component-content').text
    print('<{}번째 글>'.format(i+1))
    print(content)
    print()

    next_button = driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default')
    next_button.click()
    time.sleep(2)

driver.close()
