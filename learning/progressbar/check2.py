import sys
import os
import re
import shutil
import pdb

func_src_dict = {}

# return some global vars
def getGlobalVars(option, get_all=False):
	work_dir = os.path.abspath(os.curdir)
	var_dict = {'mydir':work_dir,
				'tmp':work_dir+'\\tmp',
				'allfuncs':work_dir+'\\tmp\\allfuncs\\',
				'allfiles':work_dir+'\\tmp\\allfiles.txt',
				'allfuncbopath':work_dir+'\\tmp\\allfuncbopath.txt',
				'judgeres':work_dir+'\\tmp\\judgeres.txt',
				'test_dir':'D:\\route_project\\atpbuild',
				'origin_dir':'D:\\route_project\\package',
				'route_project':'D:\\route_project'}
	if get_all:
		var_dict.pop('mydir')
		var_dict.pop('origin_dir')
		var_dict.pop('test_dir')
		var_dict.pop('route_project')
		return var_dict
	else:
		return var_dict[option]

def getStdFileName(src_text, reverse=False):
	# if reverse is True, return raw file name, else(default) return std file name
	if reverse:
		res = src_text.replace('+', '\\').replace('#', ':').replace(',', '.').replace('~', '*')
	else:
		res = src_text.replace('\\', '+').replace(':', '#').replace('.', ',').replace('*', '~')
	return res

# as the function name indicates...
def parseFileIntoFunctions(file_text):
	regex_function_body = r'^[0-9a-zA-Z\**_*&*]+([\s][0-9a-zA-Z\**_*&*]*){1,2}\((.*\n)*?^}'
	result = []
	function_bodies = re.finditer(regex_function_body, file_text, re.MULTILINE)
	for index, function_body in enumerate(function_bodies):
		body_text = function_body.group()
		result.append(body_text)
	return result

def judgeFunctionBysim(judged_file, compare_file):
	judged_file = judged_file.replace('\\', '/')
	compare_file = compare_file.replace('\\', '/')
	cmd_judge_code = 'sim_c.exe -p -a -R -e -T -s -t 100 {0} / {1}'.format(judged_file, compare_file)
	# print(cmd_judge_code)
	judge_result = os.popen(cmd_judge_code)
	judge_result = judge_result.readlines()

	f_output = open(getGlobalVars('judgeres'), 'a', encoding='gb18030', errors='replace')
	for line in judge_result:
		raw_ouput = line.strip()
		# get useful info from std output device
		if 'consists for' in raw_ouput:
			output_list = raw_ouput.split('consists for')
			# print(output_list)
			src_func = re.findall(r'FUNCTION@.*', output_list[0])
			tgt_half = output_list[1].split('of')
			similarity = tgt_half[0]
			
			tgt_func = re.findall(r'FUNCTION@.*', tgt_half[-1])
			src_func = getStdFileName(src_func[0].strip(), reverse=True)
			tgt_func = getStdFileName(tgt_func[0].replace('material', '').strip(), reverse=True)
			if not src_func == tgt_func:
				output_strct = '{0}\t{1}\t{2}\t{3}\t{4}\n'.format(src_func, func_src_dict[src_func], tgt_func, func_src_dict[tgt_func], similarity)
				print(output_strct)
				f_output.write(output_strct)
			else:
				pass
		else:
			pass
	f_output.close()

def judgeFunctionBySSdeep(judged_path):
	cmd_judge_code = 'ssdeep -r -d -v -c -t 95 tmp >ssdeep_judge_result.csv'
	judge_result = os.popen(cmd_judge_code)
	judge_result = judge_result.readlines()
	# for line in judge_result:
	# 	line = line.replace('tmp\\allfuncs', '')
	# 	print(line)

def parseFunctions():
	f_input = open(getGlobalVars('allfiles'), 'r', encoding='gb18030', errors='replace')	
	c_input = f_input.readlines()
	i = 0
	for file_name in c_input:
		if i%10 == 0:
			print('{0} of {1}'.format(i, len(c_input)))

		file_name = file_name.strip()
		f_file = open(file_name, 'r', encoding='gb18030', errors='replace')
		c_file = f_file.read()
		function_bodies = parseFileIntoFunctions(c_file)
		for function_body in function_bodies:
			writeFunctionIntoFile(file_name, function_body)
		c_file = f_file.readlines()
		i += 1
	f_input.close()

def judgeAllFunctions(method):
	if method == 'sim':
		f_funcinfo = open(getGlobalVars('allfuncbopath'), 'r', encoding='gb18030', errors='replace')
		c_funcinfo = f_funcinfo.readlines()
		i = 0
		for funinfo in c_funcinfo:
			# if i%10 == 0:
			# 	print('{0} of {1}'.format(i, len(c_input)))
			judgeFunctionBysim(funinfo.strip(), getGlobalVars('allfuncs'))
			i += 1
	elif method == 'ssdeep':
		judgeFunctionBySSdeep(getGlobalVars('tmp'))

def catchJudgeresIntoJail(method='ssdeep'):
	if method == 'ssdeep':
		with open('ssdeep_judge_result.csv', 'r', encoding='gb18030', errors='replace') as ssdeep_judge_res:
			lines = ssdeep_judge_res.readlines()
			for line in lines:
				line_list = line.split(',')
				print(line_list)
				# dir_name = r'.\jail'
				# cmd_cp_1 = r'cp {0} -destination {1}'.format(file_1, dir_name)
				# cmd_cp_2 = r'cp {0} -destination {1}'.format(file_2, dir_name)



if __name__ == '__main__':
	# judgeAllFunctions(method='ssdeep')
	catchJudgeresIntoJail()
