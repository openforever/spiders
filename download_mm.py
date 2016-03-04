# -*- coding: utf-8 -*-

import urllib.request
import os  #创建文件夹模块
import random

def url_open(url):  #使用代理之后，爬出来的图片居然不是原来的图片
	req = urllib.request.Request(url) #timeout=10 设置超时，防止有些网站访问不了或某些代理IP不起作用
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
	
	# proxies = ['218.87.116.149:9000', '183.141.69.184:3128', '120.83.68.116:8090', '115.223.221.254:9000']
	# proxy = random.choice(proxies)
	# print(random.choice(proxies))
	# proxy_support = urllib.request.ProxyHandler({'http':proxy})
	# opener = urllib.request.build_opener(proxy_support)
	# urllib.request.install_opener(opener)

	response = urllib.request.urlopen(req)
	html = response.read()  #.decode('utf-8')图片是二进制，所以decode不鞥放入函数
	print(url)
	return html

def get_page(url):
	html = url_open(url).decode('utf-8')

	a = html.find('current-comment-page') + 23
	b = html.find(']', a)#从a开始，找到第一个]，返回索引
	print(html[a:b])
	return html[a:b]

def find_imgs(page_url):
	html = url_open(page_url).decode('utf-8')
	img_addrs = []

	a = html.find('img src=')
	while a != -1:
		b = html.find('.jpg', a, a + 255) #现在可能不是jpg格式，防止可能找到下一个url去
		if b != -1: #找到url，没有找到返回-1
			img_addrs.append(html[a + 9:b + 4])
		else:
			b = a + 9 #如果没有找到，可能是其他图片格式，所以不直接跳
		a = html.find('img src=', b)

	for each in img_addrs:
		print(each)

	return img_addrs


def save_imgs(folder, img_addrs):
	for each in img_addrs:
		filename = each.split('/')[-1] #最后一个/分割的就是名字
		with open(filename, 'wb') as f:
			img = url_open(each)
			f.write(img)


def download_mm(folder='OOXX', pages=10): #文件夹名，默认是OOXX,默认前10页
	os.mkdir(folder)
	os.chdir(folder) #改变目录到这个文件夹

	url = 'http://jiandan.net/ooxx/' #注意，末尾有个/
	page_num = int(get_page(url))

	for i in range(pages):
		page_num -= i
		page_url = url + 'page-' + str(page_num) + '#comments'
		#将所有的图片url返回，保存为一个列表
		img_addrs = find_imgs(page_url)
		save_imgs(folder, img_addrs)

if __name__ == '__main__':
	download_mm()
