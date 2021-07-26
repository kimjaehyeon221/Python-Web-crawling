from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

# 영어 ↔ 한국어 버튼 한번만 클릭
driver.find_element_by_css_selector('button.btn_switch___x4Tcl').click()
time.sleep(1)

# CSV 파일의 한국어만 따로 저장
f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)
next(rdr)

korean_words = []
for row in rdr:
    korean = row[1]
    korean_words.append(korean)

f.close()

# 이전과 똑같이 <입력 - 번역 버튼 클릭 - 번역 결과 출력>
for korean in korean_words:

    driver.find_element_by_css_selector('textarea#txtSource').send_keys(korean)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    
    print(korean, ':', output)
    
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    
driver.close()
