#!/usr/bin/env python3
# *-* coding: utf-8 *-*

#下载电影排行榜的电影宣传图片

import sys,requests,bs4

def get_html(url):
	try:
		r=requests.get(url, timeout=30)
		r.raise_for_status
		#r.encoding=r.apparent_encoding
		r.encoding="gbk"
		return r.text
	except:
		return 'Something Wrong'

def get_content(url):
	html=get_html(url)
	soup=bs4.BeautifulSoup(html, 'lxml')
	match_tag=soup.find('ul', attrs={'class':'picList clearfix'})
	#match_tag=soup.find('ul', class_="picList clearfix")
	print(match_tag)

	films_list=match_tag.find_all('li')
	i=0
	for film in films_list:
		i+=1
		#film_name=film.find('span', attrs={'class':'sTit'}).a.text
		#print(film_name)
		pic_url=film.find('div', class_="pic").img['src']
		pic_url="http:"+pic_url
		pic_name="/root/download_pic/"+"picture_"+str(i)
		print(pic_name)

		with open(pic_name, "wb+") as f:
			f.write(requests.get(pic_url).content)

if __name__ == "__main__":
	url="http://dianying.2345.com/top/"
	get_content(url)
	

