"""
#妈夸，打了半天还是有bug搞不下去了
#有没有大佬帮帮改改
#我弄一个简易版的，应该可以爬到一些热门的漫画漫（社团学姐
"""
"""import requests
from lxml import etree
import os


url_zu = "https://hkmh.site"

url_qian_bu = "https://hkmh.site/plus/search.php?q="

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}

url_wei_bu = input("漫画名\n")

page_number = input("第几章\n")

url = url_qian_bu + url_wei_bu

get_url_home = requests.get(url=url, headers=headers).text

tree1 = etree.HTML(get_url_home)

get_url_book = tree1.xpath("/html/body/div[3]/div/div/ul[1]/li[2]/span[2]/a/@href")

get_url_book = ','.join(str(i) for i in get_url_book)

get_url_book_was_do = url_zu + get_url_book

get_url_book_was_do_html = requests.get(url=get_url_book_was_do, headers=headers).text


tree2 = etree.HTML(get_url_book_was_do_html)

book_t_url = tree2.xpath("/html/body/div[3]/div[2]/div/div[2]/ul/li")

for book_t_urled in book_t_url:
    url_asd = book_t_urled.xpath(".a/@href")
    get_url_asd = requests.get(url=url_asd, headers=headers).text
    tree_ls = etree.HTML(get_url_asd)
    book_qwe = tree_ls.xpath('//*[@id="content"]/div')
    title = tree_ls.xpath('//*[@id="container"]/div/div/div[2]/h1')
    for li in book_qwe:
        img_src = li.xpath('.img/@scr')
        img_data = requests.get(url=img_src,headers=headers).content
        img_Path = title + "/" + img_src
        if not os.path.exists(title):
            os.mkdir(title)
        with open(img_Path, "wb") as fp:
            fp.write(img_data)
        print(img_src, "已下载")"""
import requests
import os
import time

url_zu = "https://img.pic-server.com"

book_name = input("叫啥（秘密教学等等）")

book_page = input("多少页（最多爬10页）")


headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}


start = time.time()

x = 0

title = book_name + book_page
if not os.path.exists(title):
            os.mkdir(title)
while x != 60:
    x += 1

    url = url_zu + "/" + book_name + "/" + book_page + "/" + str(x) + ".jpg"
    session = requests.Session()
    re = session.get(url=url, headers=headers)
    t = title + "/" + str(x) + ".jpg"
    html_text = re.content
    with open(t, "wb") as fp:
        fp.write(html_text)
    print(x, "ok")

end = time.time()

print(f'耗时：{end - start}')
