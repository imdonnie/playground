import os
import shutil
import argparse

def parseArgs():
   parser = argparse.ArgumentParser(description='manual to this script')
   parser.add_argument('-i', '--init', type=int, default = None)
   parser.add_argument('-d', '--delete', type=int, default = None)
   parser.add_argument('-c', '--clear', type=int, default = None)
   args = parser.parse_args()
   return args


def genProblemDir(number):
   # generate dir
   l_number = len(str(number))
   print(l_number)
   if l_number == 1:
      number = '00{0}'.format(str(number))
   elif l_number == 2:
      print(number)
      number == '0{0}'.format(str(number))
      print(number)
   elif l_number == 3:
      number = str(number)
   else:
      print('invalid problem number')
      return None 
   project_path = os.getcwd()
   problem_path = '{0}\\problem{1}'.format(project_path,number)
   print(problem_path)
   return problem_path

def initProblemDir(number):
   problem_path = genProblemDir(number)
   print('making dir of problem{0}:{1}...'.format(number, problem_path))
   if os.path.exists(problem_path):
      shutil.rmtree(problem_path)
      os.mkdir(problem_path)
      return True
   else:
      os.mkdir(problem_path)
      return True

def deleteProblemDir(number):
   problem_path = genProblemDir(number)
   print('deleting dir of problem{0}:{1}...'.format(number, problem_path))
   if not os.path.exists(problem_path):
      return False
   else:
      # os.remove() delete file
      # os.rmdir() delete empty dir
      shutil.rmtree(problem_path)
      return True

def claerProblemDir(number):
   problem_path = genProblemDir(number)
   print('clearing dir of problem{0}:{1}...'.format(number, problem_path))
   if not os.path.exists(problem_path):
      return False
   else:
      # os.remove() delete file
      # os.rmdir() delete empty dir
      shutil.rmtree(problem_path)
      os.mkdir(problem_path)
      return True


if __name__ == '__main__':
   args = parseArgs()
   
   if args.init:
      if initProblemDir(args.init):
         print('init successfully!')
      else:
         print('directory exists')
   if args.delete:
      if deleteProblemDir(args.delete):
         print('delete successfully!')
      else:
         print('directory does not exists')
   if args.clear:
      if deleteProblemDir(args.clear):
         print('clear successfully!')
      else:
         print('directory does not exists')