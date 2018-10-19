import sys
import os
import re
import shutil

def catchJudgeresIntoJail(method='ssdeep'):
	if method == 'ssdeep':
		with open('ssdeep_judge_result.csv', 'r', encoding='gb18030', errors='replace') as ssdeep_judge_res:
			lines = ssdeep_judge_res.readlines()
			for line in lines:
				if len(line) == 0:
					print('empty line')
				line_list = line.split(',')
				func1_path = line_list[0].strip()
				func2_path = line_list[1].strip()
				sim_percentage = line_list[2].strip()
				src1_path = ''
				src2_path = ''

				with open(func1_path, 'r', encoding='gb18030', errors='replace') as func1:
					src1_path = func1.readlines()
					src1_path = src1_path[0].replace('SOURCE@[', '').replace(']', '').strip()
					pro1_path = src1_path.split('\\')
					pro1_path = '\\'.join(pro1_path[:-1])
				with open(func2_path, 'r', encoding='gb18030', errors='replace') as func2:
					src2_path = func2.readlines()
					src2_path = src2_path[0].replace('SOURCE@[', '').replace(']', '').strip()
					pro2_path = src2_path.split('\\')
					pro2_path = '\\'.join(pro2_path[:-1])
				new_record = "{0},{1},{2},{3},{4},{5},{6}\n".format(func1_path, src1_path, pro1_path, func2_path, src2_path, pro2_path, sim_percentage)
				with open('ssdeep_new_record.csv', 'a', encoding='gb18030', errors='replace') as ssdeep_new_record:
					ssdeep_new_record.write(new_record)

if __name__ == '__main__':
	catchJudgeresIntoJail()