import requests
from lxml import etree
import re
import time
import socket

def get_country_codes(filename):
    with open(filename,'r') as f:
        data = f.read()
    pattern = re.compile(r'[a-z]{2}')
    new = pattern.findall(data)
    return new

def get_html(url,pgn):
    # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    # 'referer': 'https://www.google.com/'}
    response = requests.get(url=url)
    html = response.text.encode('utf8')
    with open('pages/page%d.html'%pgn,'wb') as f:
        f.write(html)
    return html

def read_file(filename):
    with open(filename,'r') as f:
        html = f.read()
    return html

def fetch_pdfurl(filename):
    html = etree.parse(filename, etree.HTMLParser())
    result = html.xpath('//div[@id="main"]//a[contains(@href,"/url?q")]/@href')
    res = []
    for i in range(10):
        t = result[i][7:]
        t = t[:t.find('&sa=')]
        res.append(t)
    return res

def download_pdf(url,filename):
    print('now',filename)
    start = time.time()
    response = requests.get(url=url,timeout=3)
    finish = time.time()
    content = response.content
    print(url,end = ':')
    print(len(content))
    print(response.status_code)
    throughput = len(content)/(finish-start)
    if response.status_code == 200:
        return throughput
    else:
        return False

def generate_txt(data,filename):
    for i in data:
        with open(filename,'a+') as f:
            f.write(i)
            f.write('\n')

def url_to_ip(url):
    url = url[url.find('//')+2:]
    domain = url[:url.find('/')]
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return -1

# def ip_and_tp(filename):
#     with open