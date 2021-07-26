#csv 파일 작성하기 
import csv
f = open('./example.csv', 'w', newline = '')
wtr = csv.writer(f)
wtr.writerow(['이름', '나이', '언어'])

all_name = ['길동', '철수', '영희']
all_age = [10, 20, 30]
all_language = ['파이썬', 'C', '자바']

for i in range(3):
    name = all_name[i]
    age = all_age[i]
    language = all_language[i]
    wtr.writerow([name, age, language])

f.close()

#csv 파일 읽기 
import csv

f = open('./example.csv', 'r')
rdr = csv.reader(f)

next(rdr)

for row in rdr:
    print(row)

f.close()

#저장된 csv파일에 행 추가 import csv

# 추가 모드 옵션 'a' 사용
f = open('./example.csv', 'a', newline = '')

wtr = csv.writer(f)

wtr.writerow(['바둑', 40, '파이썬'])
wtr.writerow(['오목', 50, 'C'])

f.close()



