import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# print(data.text)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

song_info = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 0
# print(song_info)

for song_info in song_info:
    # print('*' * 100)
    # print(song_info.select('a'))
    title_el = song_info.select('a.title')
    singer_el = song_info.select('a.artist.ellipsis')

    if title_el:
        rank = rank + 1
        title = title_el[0].text
        singer = singer_el[0].text
        print(rank, title.strip(), singer)

# s = ' x '
# print(s.strip()) # => 'x'


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#############################
# (입맛에 맞게 코딩)
#############################
# < a href = "#" class ="title ellipsis" title="재생" onclick="fnPlaySong('89952547','1');return false;" > WANNABE < / a >