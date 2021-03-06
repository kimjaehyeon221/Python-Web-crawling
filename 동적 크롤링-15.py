from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드 : ')

driver = webdriver.Chrome('./chromedriver')
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)


count = 0
for i in range(3):
    if i != 0:
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[' + str(i) + ']').click()
        time.sleep(1)

    ten_articles = driver.find_elements_by_css_selector('em.tit')

    for article in ten_articles:
        title = article.text

        article.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[-1])

        try:
            content = driver.find_element_by_id('articletxt').text
        except:
            content = driver.find_element_by_id('newsView').text
            
        seperate = content.split('\n')

        count += 1
        print(f'< {count}번 뉴스 - {title} >')
        for sep in seperate:
            if sep != '':
                print(sep, end = ' ')
        print('\n')

        driver.close()

        driver.switch_to_window(driver.window_handles[0])
        time.sleep(1)

driver.close()
