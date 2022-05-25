import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#print(soup)

#마우스오른쪽>검사>copy>copy selector
#하나 가져오기(밥정)
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title)
print(title['href'])
print(title['title'])
print(title.text)

#여러개 가져오기(그린복, 가버나움)
# 구문 분석
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a

# 반복행 Parsing
movies = soup.select('#old_content > table > tbody > tr')
print('===movie===')
print(movies)

# 순위 가져오기
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
rank = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img')
print('rank')
print(rank)
print(rank['alt'])
# 평점 가져오기
#old_content > table > tbody > tr:nth-child(2) > td.point
star = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.point')
print('star')
print(star)
print(star.text)

# 반복문 돌려보기
for movie in movies:
    # Tag 추출
    a = movie.select_one('td.title > div > a')
    # 규칙 위반 행 제거(None)
    if(a is not None):
        # print(a)
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        print(rank, title, star)

