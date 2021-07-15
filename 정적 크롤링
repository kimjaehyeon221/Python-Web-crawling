import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드: ")
count = 0

for page in range(1, 3):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+ keyword +'&sort=DATE%2FDESC%2CRANK%2FDESC&period=ALL&area=ALL&mediaid_clust=HKPAPER&exact=&include=&except=&page=' + str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})
    all_title = box.find_all('em', {'class': 'tit'})
    all_time = box.find_all('span', {'class': 'date_time'})

    print('<' + str(page) + '페이지 뉴스 기사 제목>')
    for title in all_title:
        count += 1
        t = title.text
        for date_time in all_time:
            d = date_time.text
        print(count, '-', '[',d.strip(),']',t.strip())
