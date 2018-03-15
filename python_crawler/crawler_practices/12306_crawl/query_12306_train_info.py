#!/usr/bin/env python
# *-* coding: utf-8 *-*

import requests,json,sys
from stations import station_dict

requests.packages.urllib3.disable_warnings()

code_dict = {v: k for k,v in station_dict.items()}

def get_query_url():

	date = raw_input("Pls input train starting date: ")
	from_station_name = raw_input("Pls input from station name: ")
	to_station_name = raw_input("Pls input to station name: ")
	from_station = station_dict[unicode(from_station_name)]
	to_station = station_dict[unicode(to_station_name)]

	url = (
			"https://kyfw.12306.cn/otn/leftTicket/queryZ?" +
			"leftTicketDTO.train_date={}&" +
			"leftTicketDTO.from_station={}&" + 
			"leftTicketDTO.to_station={}&" + 
			"purpose_codes=ADULT"
		).format(date, from_station, to_station)

	return url

def query_train_info(url):

	info_list = []
	try:
		r = requests.get(url, verify=False)
		raw_trains = r.json()['data']['result']

		for raw_train in raw_trains:

			data_list = raw_train.split('|')

			train_no = data_list[3]

			from_station_code = data_list[6]
			from_station_name = code_dict[from_station_code].encode('utf-8')

			to_station_code = data_list[7]
			to_station_name = code_dict[to_station_code].encode('utf-8')

			start_time = data_list[8]
			arrive_time = data_list[9]
			time_fucked_up = data_list[10]

			first_class_seat = data_list[31] or '--'
			second_class_seat = data_list[30] or '--'

			soft_sleep = data_list[23] or '--'
			hard_sleep = data_list[28] or '--'
			hard_seat = data_list[29] or '--'
			no_seat = data_list[26] or '--'

			info = ('车次:{}\n出发站:{} 目的地:{}\n出发时间:{} 到达时间:{} 消耗时间:{}\n座位情况:\n一等座：[{}] \n二等座：[{}]\n软卧: [{}]\n硬卧: [{}]\n硬座: [{}]\n无座: [{}]\n\n'.format(train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat, second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))
			info_list.append(info)
		return info_list
	except:
		return '输出信息有误，请重新输入！'

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding("utf-8")
	query_url = get_query_url()
	train_info = query_train_info(query_url)
	for msg in train_info:
		print msg
		print '==============================================================================='

