# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
import time

while True:

	content = input('请输入需要翻译的内容(输入"wq"退出程序)：')
	if content == 'wq':
		break
	#使用有道词典翻译
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
	''' 法1：在Request之前，生成header
	# head = {}   
	# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
	#req = urllib.request.Request(url, data, head)
	'''
	data = {} #字典
	data['type'] = 'AUTO'
	data['i'] = content
	data['doctype'] = 'json'
	data['xmlVersion'] = '1.8'
	data['keyfrom'] = 'fanyi.web'
	data['ue'] = 'UTF-8'
	data['action'] = 'FY_BY_CLICKBUTTON'
	data['typoResult'] = 'true'
	#如果是post请求，则data必须是application/x-www-form-urlencoded类型的
	data = urllib.parse.urlencode(data).encode('utf-8') #将Unicode转成UTF-8

	req = urllib.request.Request(url, data)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
	response = urllib.request.urlopen(req)

	html = response.read().decode('utf-8') #转成unicode
	#print(html)

	target = json.loads(html)
	print("翻译结果为: %s" % target['translateResult'][0][0]['tgt'])
	time.sleep(5)  #休息5秒中

