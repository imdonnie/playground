def findHorizon(y, nums):
	# if y >= max(nums):
	# 	return 0, 0, 0
	l = []
	for index, num in enumerate(nums):
		if num == y:
			l.append(index)
	# print(l)
	return l[0], l[-1], l[-1]-l[0]

s = '((((()()()(((())))))))(((((()()()()((((((((((()))))))))))()()()()()'
s = list(s)
while s[0] != '(':
	s.remove(')')
	print(s)
while s[-1] != ')':
	s.pop() 
	print(s)
stk = []
rcd = []
for c in s:
	rcd.append(len(stk))
	if c == '(':
		stk.append(c)
	elif c == ')':
		stk.pop()
max_stk = []
for i in range(max(rcd)):
	if i > max(rcd):
		break
	start, end, l = findHorizon(i, rcd)
	new_rcd = rcd[:start] + rcd[end:] if l != 0 else rcd
	print('{0} {1} {2}'.format(str(rcd), i, str(findHorizon(i, rcd))))
	print(str(new_rcd))
	# rcd = new_rcd


