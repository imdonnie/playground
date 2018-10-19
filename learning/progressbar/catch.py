import sys
import os
import re
import shutil
import pdb

def getStdFileName(src_text, reverse=False):
	# if reverse is True, return raw file name, else(default) return std file name
	if reverse:
		res = src_text.replace('+', '\\').replace('#', ':').replace(',', '.').replace('~', '*')
	else:
		res = src_text.replace('\\', '+').replace(':', '#').replace('.', ',').replace('*', '~')
	return res

def getJudgeres(judgeres_path):
	print(judgeres_path)
	f_judgeres = open(judgeres_path, 'r', encoding='gb18030', errors='replace')
	c_judegres = f_judgeres.readlines()
	print(c_judegres)
	f_judgeres.close()
	return c_judegres


if __name__ == '__main__':
	judgeres = getJudgeres(r'.\tmp\judgeres.txt')
	for res in judgeres:
		res_list = res.split('\t')
		dir_name = r'{0}-{1}-{2}'.format(res_list[0].replace('.c', ''), res_list[2].replace('.c', ''), res_list[4].strip().replace('%', '').strip())
		dir_name = r'.\jail\{0}'.format(getStdFileName(dir_name))
		print(dir_name)
		# print(dir_name)
		if not os.path.exists(dir_name):
			os.mkdir(dir_name)
		file_1 = r'.\tmp\allfuncs\{0} '.format(getStdFileName(res_list[0]).replace(',c','.c'))
		file_2 = r'.\tmp\allfuncs\{0} '.format(getStdFileName(res_list[2]).replace(',c','.c'))
		print('{0}\t{1}'.format(file_1, file_2))
		cmd_cp_1 = r'cp {0} -destination {1}'.format(file_1, dir_name)
		cmd_cp_2 = r'cp {0} -destination {1}'.format(file_2, dir_name)
		with open('cmd_cp', 'w', encoding='gb18030', errors='replace') as f_test:
			print('{0}->{1}'.format(file_1, dir_name))
			f_test.write(cmd_cp_1)
			shutil.copyfile(file_1, dir_name+r'\func1.c')
			shutil.copyfile(file_2, dir_name+r'\func2.c')
		print(os.path.exists(dir_name))
		print(os.path.exists(file_1))
		# os.popen()