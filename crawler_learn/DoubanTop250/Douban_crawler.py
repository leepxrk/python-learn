import re,csv
import requests
import pymysql
from requests.exceptions import RequestException

def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<li>.*?<em class="">(\d+).*?href="(.*?)">.*?alt="(.*?)".*?</a>.*?<p class="">.*?:(.*?)[^A-Za-z.]'
			 '[<br>|&nbsp;&nbsp;&nbsp;].*?(\d+)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\n.*?:average">([1-9]\d*\.\d*|0\.\d*[1-9]\d*]+)''.*?'
			+'<span>(\d+).*?class="inq">(.*?)</span>.*?</li>', re.S)

    items = re.findall(pattern, html)
    movie =[]
    for item in items:
        rank = item[0]
        name= item[2]
        score = item[7]
        num_of_votes = item[8]
        director = item[3]
        release_year = item[4]
        country = item[5]
        theme = item[6]
        summary = item[9]
        movie_url = item[1]
        data = [rank, name, score, num_of_votes, director, release_year, country, theme, summary, movie_url]
        movie.append(data)
    with open('douban_top250.csv', 'a+',newline = '', encoding = 'utf-8-sig') as csvfile:  
        writer = csv.writer(csvfile)   
        for info in movie: 
            print(info) 
            writer.writerow(info)

    #将获得的信息写入本地数据库
    conn = pymysql.connect(host = '127.0.0.1',user = 'root',password = '19900807',db = "DoubanTop250",port = 3306,charset='utf8')
    data = [rank, title, score, num_of_votes, director, release_year, country, summary, movie_url, theme]

    with conn.cursor() as cur:
        sql = '''INSERT INTO movie_info (rank, title, score, num_of_votes, director, release_year, country, summary, movie_url, theme (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(sql, data)
        # 提交
        conn.commit()
        cur.close()
        conn.close()
        log(url)  # 将已经写入的电影链接存入log文件备用
        print("此url已写入log文件" + '\n' + '-' * 60 + '\n\n\n')


def write_headers():
    with open('douban_top250.csv', 'a+',newline = '', encoding = 'utf-8-sig') as csvfile:  
        writer = csv.writer(csvfile)   
        writer.writerow(['rank', 'title', 'score', 'num_of_votes', 'director', 'release_year', 'country', 'theme', 'summary', 'movie_url'])   
        
def main(i):
    url = 'https://movie.douban.com/top250?start='+str(i)+'&filter='
    html =get_one_page(url)
    parse_one_page(html)

if __name__ == '__main__':
    write_headers()   
    for i in range (10):
        main(i * 25)
