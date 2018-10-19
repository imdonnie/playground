#！ _*_ encoding:utf-8

# <dd class="cpu">.*?</dd>
# <dd class="cpu_cores">.*?</dd>
# <dd class="cpu_mhz">.*?</dd>
# <dd class="flash_mb">.*?</dd>
# <dd class="ram_mb">.*?</dd>
# <dd class="ethernet_100m_ports">.*?</dd>
# <dd class="ethernet_gbit_ports">.*?</dd>
# <dd class="switch">.*?</dd>
# <dd class="wlan_hardware">.*?</dd>
# <dd class="wlan_24ghz">.*?</dd>
# <dd class="wlan_50ghz">.*?</dd>
# <dd class="wlan_driver">.*?</dd>
# <dd class="wlan_comments">.*?</dd>
# <dd class="detachable_antennas">.*?</dd>
# <dd class="power_supply">.*?</dd>

import time
import operator
import re
import sys
import http.cookiejar
from urllib	 import request

# 以字典的形式设置headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Connection": "keep-alive",
    "referer": "http://www.163.com"
}
#设置cookie
cjar = http.cookiejar.CookieJar()
proxy = request.ProxyHandler({'http': "127.0.0.1:8888"})
opener = request.build_opener(proxy, request.HTTPHandler, request.HTTPCookieProcessor(cjar))
# 建立空列表，为了以制定格式存储头信息
headall = []
for key,value in headers.items():
    item = (key, value)
    headall.append(item)
# 将制定格式的headers信息添加好
opener.addheaders = headall
# 将opener安装为全局
request.install_opener(opener)

def getContent(text, mask):
	raw_res = re.findall(mask, text)
	print(raw_res)
	if operator.eq(raw_res, []):
		return '-'
	mid_res = re.findall(r">.*<", raw_res[0])
	res = mid_res[0].replace('>', '').replace('<', '')
	return res

def getProductInfo(product_name, product_href):
	file_output = open('output.txt', 'a')
	file_raw = open('raw_text.txt', 'w')
	url_prefix = "https://openwrt.org"
	# product_name = "tp-link_archer_c60_v1"
	
	url = url_prefix + product_href

	http_response = request.urlopen(url)
	http_content = http_response.read()
	str_content = str(http_content)

	cpu = getContent(str_content, "<dd class=\"cpu\">.*?</dd>")
	cpu_cores = getContent(str_content, "<dd class=\"cpu_cores\">.*?</dd>")
	cpu_mhz = getContent(str_content, "<dd class=\"cpu_mhz\">.*?</dd>")
	switch = getContent(str_content, "<dd class=\"switch\">.*?</dd>")
	wlan_hardware = getContent(str_content, "<dd class=\"wlan_hardware\">.*?<span>?")
	wlan_24ghz = getContent(str_content, "<dd class=\"wlan_24ghz\">.*?</dd>")
	wlan_50ghz = getContent(str_content, "<dd class=\"wlan_50ghz\">.*?</dd>")
	# wlan_driver = getContent(str_content, "<dd class=\"wlan_driver\">.*?</dd>")
	wlan_driver = '-'
	flash_mb = getContent(str_content, "<dd class=\"flash_mb\">.*?</dd>")
	ram_mb = getContent(str_content, "<dd class=\"ram_mb\">.*?</dd>")
	wlan_comments = getContent(str_content, "<dd class=\"wlan_comments\">.*?</dd>")
	detachable_antennas = getContent(str_content, "<dd class=\"detachable_antennas\">.*?</dd>")
	power_supply = getContent(str_content, "<dd class=\"power_supply\">.*?</dd>")
	ethernet_100m_ports = getContent(str_content, "<dd class=\"ethernet_100m_ports\">.*?</dd>")
	ethernet_gbit_ports = getContent(str_content, "<dd class=\"ethernet_gbit_ports\">.*?</dd>")

	output = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\n'.format(
			product_name,
			cpu, cpu_cores, cpu_mhz, switch, 
			wlan_hardware, wlan_24ghz, wlan_50ghz, wlan_driver, 
			flash_mb, ram_mb, wlan_comments, detachable_antennas,
			power_supply, ethernet_100m_ports, ethernet_gbit_ports)

	print(output)
	file_raw.write(str_content)
	file_output.write(output)

	file_raw.close()
	file_output.close()
	return

# def getStart():
# 	file_output = open('start_raw.txt', 'w')
# 	url = "https://openwrt.org/toh/hwdata/tp-link/start"
# 	http_response = request.urlopen(url)

# 	http_content = http_response.read()
# 	str_content = str(http_content)

# 	file_output.write(str_content)
# 	file_output.close()

# 	return
# 	# re.findall()	

if __name__ == '__main__':
	# getStart()
	start = str(sys.argv[1])
	start = int(start)
	file_product_list = open('product_list.txt', 'r')
	file_href_list = open('href_list.txt', 'r')

	product_list = file_product_list.read()
	product_list = product_list.split('\n')
	href_list = file_href_list.read()
	href_list = href_list.split('\n')

	for i in range(start, len(product_list)):
		print('{0}: {1}'.format(product_list[i], href_list[i]))
		getProductInfo(product_list[i], href_list[i])
		# time.sleep(10)

	file_product_list.close()
	file_href_list.close()