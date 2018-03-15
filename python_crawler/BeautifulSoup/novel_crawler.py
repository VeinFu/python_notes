#!/usr/bin/env python3
# *-* coding: utf-8 *-*

import sys,requests,bs4

def get_html(url):
	try:
		r=requests.get(url, timeout=30)
		r.raise_for_status
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "ERROR"

def get_content(url):	
	url_list = []
	html = get_html(url)
	print html
	soup = bs4.BeautifulSoup(html, 'lxml')
    # 由于小说排版的原因，历史类和完本类小说不在一个div里
	category_list = soup.find_all('div', class_='index_toplist mright mbottom')
	history_finished_list = soup.find_all('div', class_='index_toplist mbottom')

	for cate in category_list:
		name = cate.find('div', class_='toptab').span.string
		print name
		with open('novel_list.csv', 'a+') as f:
			f.write("\n小说种类：{} \n".format(name.encode('utf-8')))

        # 我们直接通过style属性来定位总排行榜
		general_list = cate.find(style='display: block;')
        # 找到全部的小说名字，发现他们全部都包含在li标签之中
		book_list = general_list.find_all('li')
        # 循环遍历出每一个小说的的名字，以及链接
		for book in book_list:
			link = 'http://www.qu.la/' + book.a['href']
			title = book.a['title']
            # 我们将所有文章的url地址保存在一个列表变量里
			url_list.append(link)
            # 这里使用a模式，防止清空文件
			with open('novel_list.csv', 'a') as f:
				f.write("小说名：{:<} \t 小说地址：{:<} \n".format(title.encode('utf-8'), link.encode('utf-8')))

	for cate in history_finished_list:
		name = cate.find('div', class_='toptab').span.string
		with open('novel_list.csv', 'a') as f:
			f.write("\n小说种类：{} \n".format(name.encode('utf-8')))

		general_list = cate.find(style='display: block;')
		book_list = general_list.find_all('li')
		for book in book_list:
			link = 'http://www.qu.la/' + book.a['href']
			title = book.a['title']
			url_list.append(link)
			with open('novel_list.csv', 'a') as f:
				f.write("小说名：{:<} \t 小说地址：{:<} \n".format(title.encode('utf-8'), link.encode('utf-8')))

	return url_list

if __name__ == "__main__":
#	reload(sys)
#	sys.setdefaultencoding('utf-8')
	url='https://www.qu.la/paihangbang/'
	get_content(url)
